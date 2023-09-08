# Pwn cheatsheets

## Pwntools

### Pwntools

导入包：

```
> from pwn import *
```

建立/关闭连接：

```
# 本地连接
sh = process("./code")
```

```
# 远程连接
sh = remote("127.0.0.1",6666)
```

```
# 关闭连接
sh.close()
```

I/O操作：

```
# 发送数据
sh.send(data)

# 发送一行数据
sh.sendline(data)
```

```
# 接收数据，numb指定接收字节
sh.recv(numb=1024, timeout = default)

# 接收一行数据，keepends表示是否保留行尾\n
sh.recvline(keepends = True)

# 接收数据直到设置的标志出现
sh.recvutil("Hello\n", drop=false)

# 持续接收数据直到EOF
sh.recvall()

# 持续接收数据直到EOF或timeout
sh.recvrepeat(timeout = default)
```

```
# 直接进行交互，在取得shell后使用
sh.interactive()
```

