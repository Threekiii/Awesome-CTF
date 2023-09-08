# Misc cheatsheets

## Command

私钥解密：

```
openssl rsautl -decrypt -in whoami.txt -inkey private.key out flag.txt
```

伪加密：

## 图片分析

### 步骤方法

1. 首先查看EXIF信息。
2. 如果图片在windows下能查看，kali下无法查看，说明格式数据错误，可以修改图片的长宽高来显示隐藏图像。
3. 通过binwalk或者foremost查看是否有隐藏文件（查看文件头，可能存在**隐藏文件**的情况，例如文件里包含一个 JPG 图片，则提取文件头 `FF D8 FF` 到文件尾 `FF D9` 即可提取出 JPG 文件）。
4. 通过stegsolve进行色差分析，查看zlib数据段。
5. 查看文件是否包含有损坏的其他文件，查找文件中是否有可疑字符串，例如flag、key、pass。
6. 验证是否存在隐写，例如LSB隐写。

### 图片拼接

沿水平方向拼接：

```
convert -append *.png ../flag.png
```

沿垂直方向拼接：

```
convert +append *.png ../flag.png
```

分割图片恢复原图脚本：

- [image_merge1.py](https://github.com/Threekiii/Awesome-CTF/blob/master/scripts/misc/image_merge1.py)
- [image_merge2.py](https://github.com/Threekiii/Awesome-CTF/blob/master/scripts/misc/image_merge2.py)

### jpg长宽修改

```
修改图片高度， FF C0后的第4个字节和第5个字节
```

### png长宽修改

```
修改0x14到0x17的四个字节
```

![image-20221115155926964](images/202211151559069.png)

修改后：

![image-20221115160008245](images/202211151600283.png)

### 位深隐写

图片位深隐写脚本：

- [stega_8bit.py](https://github.com/Threekiii/Awesome-CTF/blob/master/scripts/misc/stega_8bit.py)

图片常见深度有：

- 8Bit（包含四个通道：RGBA，每个通道分别占有2bit）
- 12Bit（包含三个通道：RGB，每个通道分别占有4bit）
- 24Bit（包含三个通道：RGB，每个通道分别占有8bit）
- 32Bit（包含四个通道：RGB，每个通道分别占有8bit）

图片位深隐写特征：

- 图片→属性→详细信息，位深度可能为48bit
- 使用stegsolve时发现A通道空白（说明该图片只有三个通道RGB，每个通道深度是48/3=16bit。图片显示最高通道就只有8bit，得出该图片隐藏了另外8bit的信息）

### 二维码

二维码010101绘制：

- [qrcode_painter_1.py](https://github.com/Threekiii/Awesome-CTF/blob/master/scripts/misc/qrcode_painter_1.py)
- [qrcode_painter_2.py](

## 流量分析

### wireshark

过滤IP：

```
ip.src eq xxx.xxx.xxx.xxx or ip.dst eq xxx.xxx.xxx.xxx
```

```
ip.addr eq xxx.xxx.xxx.xxx
```

过滤端口：

```
tcp.port eq 80 or udp.port eq 80
```

```
tcp.dstport == 80 or tcp.srcport == 80
```

```
tcp.port >=1 and tcp.port <=80
```

过滤协议：

```
tcp/udp/arp/icmp/http/ftp/dns/ip
```

过滤MAC：

```
eth.dst == A0:04:C6:85:63:73
```

HTTP过滤：

```
http.request.method == "GET"
```

```
http.request.method == "POST"
```

```
http.request.uri == "/img/logo.png"
```

```
http contains "GET"
```

```
http contains "HTTP/1."
```

```
http.request.method == "GET" && http contains "User-Agent:"
```

### tshark

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

配合python使用：

```python
from os import system

system("tshark -r icmp_data.pcap -Y \"icmp && icmp.type==8\" -T fields -e data > flag.txt")
f = open('flag.txt', 'r')
flag = ''
for line in f.readlines():
    flag += chr(int(line[16:18], 16))
print(flag)
f.close()
```

## 压缩包分析

### 步骤方法

不同压缩包分析方法分别用于：

1. ZIP暴力破解：文件的密码为纯数字且位数不多时。
2. ZIP伪加密：ZIP文件的压缩源文件目录中09 00修改为00 00，可以成功解压时。
3. CRC32攻击：当文件数据少且文件大小较小时。
4. 明文攻击：加密文件中存在部分已知文件（>12字节）时。

Tips：文件打不开，显示“压缩文件已损坏”时，尝试winrar工具中的修复功能进行修复。

### zip伪加密

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

压缩文件源文件目录结束区：

```
50 4B 05 06：目录结束标记(0x06054b50)
00 00：当前磁盘编号
00 00：目录区开始磁盘编号
01 00：本磁盘上纪录总数
01 00：目录区中纪录总数
59 00 00 00：目录区尺寸大小
3E 00 00 00 00：目录区对第一张磁盘的偏移量
00 00：ZIP文件注释长度
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

判断伪加密：

```
java -jar ZipCenOp.jar xxx.zip
```

## 日志分析

### Windows常见安全事件

检索4624/4625登录事件，爆破时间点与登录事件点一一对应的可能是异常账户。

```
4624  --登录成功   
4625  --登录失败  
4634 -- 注销成功
4647 -- 用户启动的注销   
4672 -- 使用超级用户（如管理员）进行登录
```

## 取证分析

### 查看文件内容

```
$ file <filename>
```

```
$ mmls <filename>
```

### 分区挂载

先查看文件内容：

```
$ mmls <filename>  
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000000127   0000000128   Unallocated
002:  000:000   0000000128   0000198783   0000198656   NTFS / exFAT (0x07)
003:  -------   0000198784   0000204799   0000006016   Unallocated
```

偏移 128 挂载 NTFS 分区：

```
$ mkdir /mnt/foo ; mount <fielname> /mnt/foo -o offset=$((128*512))
```

### volatility2使用

查看内存镜像系统摘要：

```
python2 vol.py -f <filename.raw> imageinfo
```

扫描镜像进程：

```
python2 vol.py -f <filename.raw> --profile=<profile> psscan
```

```
python2 vol.py -f <filename.raw> --profile=<profile> pslist
```

导出进程数据（.dmp文件）：

```
python2 vol.py -f <filename.raw> --profile=<profile> memdump -p <pid> -D ./
```

扫描文件：

```
python2 vol.py -f <filename.raw> --profile=<profile> filescan | grep zip
```

```
python2 vol.py -f <filename.raw> --profile=<profile> filescan | grep txt
```

```
python2 vol.py -f <filename.raw> --profile=<profile> filescan | grep flag
```

导出文件：

```
python2 vol.py -f <filename.raw> --profile=<profile> dumpfiles -Q <文件地址0x00> -D outfile
```

### GIMP使用

volatility dump进程，将.dmp后缀改为.data，用GIMP打开，调整高度、位移、宽度。