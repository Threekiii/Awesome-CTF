# Misc cheatsheets

## Command

私钥解密：

```
openssl rsautl -decrypt -in whoami.txt -inkey private.key out flag.txt
```

## 图片分析

### 步骤方法

1. 首先查看EXIF信息。
2. 如果图片在windows下能查看，kali下无法查看，说明格式数据错误，可以修改图片的长宽高来显示隐藏图像。
3. 通过binwalk或者foremost查看是否有隐藏文件（查看文件头，可能存在**隐藏文件**的情况，例如文件里包含一个 JPG 图片，则提取文件头 `FF D8 FF` 到文件尾 `FF D9` 即可提取出 JPG 文件）。
4. 通过stegsolve进行色差分析，查看zlib数据段。
5. 查看文件是否包含有损坏的其他文件，查找文件中是否有可疑字符串，例如flag、key、pass。
6. 验证是否存在隐写，例如LSB隐写。

### 图片隐写

```
# binwalk pic.jpg
 
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
382           0x17E           Copyright string: "Copyright (c) 1998 Hewlett-Packard Company"
3192          0xC78           TIFF image data, big-endian, offset of first image directory: 8
140147        0x22373         JPEG image data, JFIF standard 1.01
140177        0x22391         TIFF image data, big-endian, offset of first image directory: 8
```

```
# dd if=pic.jpg of=outfile.jpg skip=140147 bs=1
```

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

