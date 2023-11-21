# Awesome-CTF

**【免责声明】本项目所涉及的技术、思路和工具仅供学习，任何人不得将其用于非法用途和盈利，不得将其用于非授权渗透测试，否则后果自行承担，与本项目无关。使用本项目前请先阅读 [法律法规](https://github.com/Threekiii/Awesome-Laws)。**

- [开源导航](#%E5%BC%80%E6%BA%90%E5%AF%BC%E8%88%AA)
- [Crypto](#crypto)
	- [综合工具](#%E7%BB%BC%E5%90%88%E5%B7%A5%E5%85%B7)
	- [密码学](#%E5%AF%86%E7%A0%81%E5%AD%A6)
	- [数学计算](#%E6%95%B0%E5%AD%A6%E8%AE%A1%E7%AE%97)
	- [编解码](#%E7%BC%96%E8%A7%A3%E7%A0%81)
- [Misc](#misc)
	- [综合工具](#%E7%BB%BC%E5%90%88%E5%B7%A5%E5%85%B7)
	- [图片分析](#%E5%9B%BE%E7%89%87%E5%88%86%E6%9E%90)
		- [图片隐写](#%E5%9B%BE%E7%89%87%E9%9A%90%E5%86%99)
		- [图片EXIF](#%E5%9B%BE%E7%89%87exif)
		- [二维码](#%E4%BA%8C%E7%BB%B4%E7%A0%81)
		- [图片杂项](#%E5%9B%BE%E7%89%87%E6%9D%82%E9%A1%B9)
	- [音视频分析](#%E9%9F%B3%E8%A7%86%E9%A2%91%E5%88%86%E6%9E%90)
	- [流量分析](#%E6%B5%81%E9%87%8F%E5%88%86%E6%9E%90)
	- [取证分析](#%E5%8F%96%E8%AF%81%E5%88%86%E6%9E%90)
	- [日志分析](#%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90)
	- [数据处理](#%E6%95%B0%E6%8D%AE%E5%A4%84%E7%90%86)
	- [密码破解](#%E5%AF%86%E7%A0%81%E7%A0%B4%E8%A7%A3)
	- [基线加固](#%E5%9F%BA%E7%BA%BF%E5%8A%A0%E5%9B%BA)
	- [应急响应](#%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94)
	- [物联网](#%E7%89%A9%E8%81%94%E7%BD%91)
	- [其他](#%E5%85%B6%E4%BB%96)
- [Web](#web)
	- [信息泄露](#%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2)
	- [绕过](#%E7%BB%95%E8%BF%87)
	- [其他](#%E5%85%B6%E4%BB%96)
- [Pwn](#pwn)
	- [Pwntools](#pwntools)
	- [IDA](#ida)
	- [GDB](#gdb)
	- [ROP Gadget](#rop-gadget)
- [Reverse](#reverse)
	- [ELF/EXE逆向](#elfexe%E9%80%86%E5%90%91)
	- [Android逆向](#android%E9%80%86%E5%90%91)
	- [Java逆向](#java%E9%80%86%E5%90%91)
	- [Python逆向](#python%E9%80%86%E5%90%91)
	- [Rust 逆向](#rust-%E9%80%86%E5%90%91)
	- [Go 逆向](#go-%E9%80%86%E5%90%91)
	- [查壳脱壳](#%E6%9F%A5%E5%A3%B3%E8%84%B1%E5%A3%B3)
	- [符号执行](#%E7%AC%A6%E5%8F%B7%E6%89%A7%E8%A1%8C)
	- [IDA签名库](#ida%E7%AD%BE%E5%90%8D%E5%BA%93)
	- [其他](#%E5%85%B6%E4%BB%96)



## 开源导航

- CTF Wiki：https://ctf-wiki.org/
- CTF Hub：https://www.ctfhub.com/
- CTF Time：https://ctftime.org/
- AWD-Guide：https://github.com/AabyssZG/AWD-Guide
- 攻防世界：https://adworld.xctf.org.cn/
- Hacker 101：https://www.hacker101.com/
- Cryptopals：密码学练习题目 https://cryptopals.com/
- Awesome-ctf：https://github.com/apsdehal/awesome-ctf
- CTF Tools：https://github.com/zardus/ctf-tools
- 近期赛事：https://su-sanha.cn/events/ API：http://event.ctf.probius.xyz/cn_CTF

## Crypto

### 综合工具

- CyberChef：综合编解码及加密，可本地部署 https://github.com/gchq/CyberChef
- OK Tools在线工具：https://github.com/wangyiwy/oktools
- CTF 在线工具：http://www.hiencode.com/
- ctfcode：随波逐流工作室 CTF编码工具 http://1o1o.xyz/bo_ctfcode.html
- XSSEE：在线综合编解码 https://evilcos.me/lab/xssee/
- MeTools：在线综合编解码 http://www.metools.info/code/quotedprintable231.html

### 密码学

- 摩斯电码：http://moersima.00cha.net/
- 摩斯电码：http://www.zhongguosou.com/zonghe/moersicodeconverter.aspx
- 栅栏密码：https://www.qqxiuzi.cn/bianma/zhalanmima.php
- 猪圈密码：http://www.hiencode.com/pigpen.html
- 零宽字符：http://330k.github.io/misc_tools/unicode_steganography.html
- quipqiup：在线古典密码词频爆破 https://www.quipqiup.com/

### 数学计算

- yafu：RSA解题中的因式分解 https://github.com/bbuhrow/yafu
- factordb：在线大数分解数据库 http://factordb.com/
- 在线求解线性方程组：http://www.yunsuan.info/matrixcomputations/solvelinearsystems.html  

### 编解码

- MD5 Hash：https://www.somd5.com/
- GB2312：http://code.mcdvisa.com/
- Unicode字符表：https://www.52unicode.com/enclosed-alphanumerics-zifu
- Unicode：https://www.compart.com/en/unicode/
- UUencode：http://web.chacuo.net/charsetuuencode
- XXencode：输入文本以每三个字节为单位进行编码 http://web.chacuo.net/charsetxxencode
- Escape/Unescape：https://tool.chinaz.com/tools/escape.aspx
- HTML实体编码：https://zh.rakko.tools/tools/21/
- Base64填充位隐写读取：https://github.com/cjcslhp/wheels/tree/master/b64stego

## Misc

### 综合工具

- PuzzleSolver：Misc工具 https://github.com/Byxs20/PuzzleSolver

### 图片分析

#### 图片隐写

- Stegsolve：图片隐写查看器 http://www.caesum.com/handbook/stego.ht
- Stegonline：Stegsolve在线版 https://stegonline.georgeom.net/upload
- F5-steganography：隐写工具 https://github.com/matthewgao/F5-steganography
- OutGuess：隐写工具 https://github.com/crorvick/outguess
- Silenteye：隐写工具 https://achorein.github.io/silenteye/
- zsteg：检测PNG和BMP图片隐写数据 https://github.com/zed-0xff/zsteg
- PNGDebugger：读取png文件头，检查CRC https://github.com/rvong/png-debugger#pngdebugger

#### 图片EXIF

- 图虫在线EXIF查看器：https://exif.tuchong.com/
- EXIF查看器：exiftool https://exiftool.org/
- Magicexif元数据编辑器：https://www.magicexif.com/
- TweakPNG：png图像编辑器，修改元数据 https://entropymine.com/jason/tweakpng/

#### 图片杂项

- Ezgif：在线分帧 https://ezgif.com/split
- 盲水印提取：https://github.com/chishaxie/BlindWaterMark
- OCR在线识别：https://web.baimiaoapp.com/
- 解决拼图问题：montage+gaps https://github.com/nemanja-m/gaps

#### 二维码

- 在线绘制二维码/汉信码：https://www.pixilart.com/draw?ref=home-page
- 在线绘制二维码：https://merricx.github.io/qrazybox/
- 在线扫描一维码：https://online-barcode-reader.inliteresearch.com/

### 音视频分析

- Audacity：音频隐写 https://www.audacityteam.org/
- Mp3Stego：Mp3音频隐写 https://www.petitcolas.net/steganography/mp3stego/

### 流量分析

- Pcap流量包在线修复：http://f00l.de/hacking/pcapfix.php
- knm：鼠标键盘流量包取证 https://github.com/FzWjScJ/knm

### 取证分析

#### 磁盘取证

- DiskGenius：磁盘取证工具 https://www.diskgenius.cn/
- Sleuth Kit：磁盘取证工具 https://github.com/sleuthkit/sleuthkit
- Autopsy：磁盘取证浏览器 https://www.autopsy.com/
- ElcomSoft Distributed Password Recovery：BitLocker解密 https://www.elcomsoft.com/edpr.html
- pyvmx-cracker：.vmx密码破解 https://github.com/axcheron/pyvmx-cracker
- VMwareVMX：.vmx配置数据解密 https://github.com/RF3/VMwareVMX

#### 内存取证

- Volatility：内存取证工具 https://github.com/volatilityfoundation/volatility
- Volatility3：https://github.com/volatilityfoundation/volatility3
- GIMP：开源图像编辑器 配合Volatility导出的.dmp使用 https://www.gimp.org/

#### 日志取证

- LogForensics：web日志取证分析工具 https://security.tencent.com/index.php/opensource/detail/15
- ProcessMonitor：进程监视器 https://learn.microsoft.com/zh-cn/sysinternals/downloads/procmon
- Event log explorer：日志查看器 https://www.eventlogxp.com/

### 木马分析

- CS_Decrypt：CobaltStrike流量解密 https://github.com/5ime/CS_Decrypt
- godzilla_decryptor：Godzilla流量解密https://github.com/Threekiii/Awesome-Redteam/blob/master/scripts/Godzilla_Decryptor/godzilla_decryptor.py
- BlueTeamTools：综合工具 冰蝎1.x-3.x Godzilla1.x-4.x流量解密 https://github.com/abc123info/BlueTeamTools

### 密码破解

- aircrack-ng：破解wifi密码 https://github.com/aircrack-ng/aircrack-ng
- Advanced Office Password Recovery（AOPR）：破解office文档密码 https://www.elcomsoft.com/aopr.html
- Advanced Archive Password Recovery（ARCHPR）：破解zip和rar文件密码 https://www.elcomsoft.com/archpr.html
- crc32：CRC32爆破 https://github.com/theonlypwner/crc32
- ZipCenOp：zip伪加密破解 
- Ziperello：zip压缩包密码破解
- c-jwt-cracker：JWT Token爆破 https://github.com/brendan-rius/c-jwt-cracker
- how-does-Xmanager-encrypt-password：Xmanager 密码解密 https://github.com/HyperSine/how-does-Xmanager-encrypt-password

### 基线加固

- Benchmarks：常用服务器、数据库、中间件安全配置基线 https://github.com/AV1080p/Benchmarks
- Shell_Script：Linux 系统检测和加固脚本 https://github.com/xiaoyunjie/Shell_Script

### 数据处理

- 010 Editor：https://www.sweetscape.com/010editor/
  - 010 Editor 插件模板下载：例如 ELF.bt https://www.sweetscape.com/010editor/repository/templates/
- Binwalk：https://github.com/ReFirmLabs/binwalk
- 在线正则表达式：https://c.runoob.com/front-end/854/
- 在线正则表达式：https://regex101.com/

### 物联网

- QEMU：https://wiki.qemu.org/Documentation

### 其他

- 在线正则英语单词：https://regdict.com/
- 数独求解器：https://shudu.gwalker.cn/

## Web

### 信息泄露

- .git 信息泄露：https://github.com/BugScanTeam/GitHack
- .svn/.hg/.cvs 信息泄露：https://github.com/kost/dvcs-ripper

### 绕过

- localhost绕过：127.0.0.1  >>> 2130706433 https://www.browserling.com/tools/ip-to-dec

### 其他

- D盾：Webshell查杀 https://www.d99net.net/

## Pwn

### Pwntools

- Pwntools：CTF框架和漏洞利用开发库 https://github.com/Gallopsled/pwntools

### IDA

- idaplugins-list：IDA 插件 https://github.com/onethawt/idaplugins-list

### GDB

- Pwndbg：GDB 插件 https://github.com/pwndbg/pwndbg

- gdb-dashboard：GDB 插件 https://github.com/cyrus-and/gdb-dashboard

### ROP Gadget

- ROPgadget：返回导向式编程 寻找 Gadget https://github.com/JonathanSalwan/ROPgadget
- Ropper：返回导向式编程 寻找 Gadget https://github.com/sashs/Ropper

## Reverse

### ELF/EXE逆向

- Cutter：https://cutter.re/
- IDA：https://hex-rays.com/ida-pro/
- x64DBG：https://x64dbg.com/
- Ollydbg：https://www.ollydbg.de/
- bindiff：二进制比对工具 https://www.zynamics.com/software.html
- angr：二进制分析 https://github.com/angr/angr

### Android逆向

- jadx：https://github.com/skylot/jadx
- JEB：https://www.pnfsoftware.com/
- GDA：https://github.com/charles2gan/GDA-android-reversing-Tool

### Java逆向

- jd-gui：https://github.com/java-decompiler/jd-gui

### Python逆向

- py2exe：打包工具 https://www.py2exe.org/
- pyInstaller：打包工具 https://pyinstaller.org/
- unpy2exe：py2exe 打包程序中提取 .pyc https://github.com/matiasb/unpy2exe
- pyinstxtractor：pyInstaller 打包程序中提取 .pyc https://github.com/extremecoders-re/pyinstxtractor
- uncompyle6：字节码文件（.pyc）反编译为源代码（.py） https://github.com/rocky/python-uncompyle6/

### Rust 逆向

- rust-reversing-helper：https://github.com/cha5126568/rust-reversing-helper

### Go 逆向

- golang_loader_assist：https://github.com/strazzere/golang_loader_assist
- IDAGolangHelper：https://github.com/sibears/IDAGolangHelper

### 查壳脱壳

- ExeinfoPE：查壳工具 https://github.com/ExeinfoASL/ASL/raw/master/exeinfope.zip
- PEiD：查壳工具 https://www.aldeid.com/wiki/PEiD
- UPX：UPX 脱壳工具 https://github.com/upx/upx

### 符号执行

- Angr：https://docs.angr.io/ 官方实例：https://docs.angr.io/en/latest/examples.html

### IDA签名库

- sig-database：IDA FLIRT 签名库 https://github.com/push0ebp/sig-database
- FLIRTDB：IDA FLIRT 签名库 https://github.com/Maktm/FLIRTDB

### 其他

- 挖矿收益计算器：https://minersns.com/tools/jsqlist

