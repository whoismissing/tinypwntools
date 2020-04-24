# tinypwntools
because 9MB is too big /s

A tiny, hacky, problematic reimagining of pwntools implementing:

```
target = process("./example")
target.recvline()
target.recvuntil(b">>")
target.sendline(b"3")
target.interactive()
```
