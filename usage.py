#!/usr/bin/python3

from pwn import process

target = process("./example")

print(target.recvline())
print(target.recvuntil(b">> "))

target.sendline(b'2')
#print(target.recvuntil(b">> "))

target.interactive()
