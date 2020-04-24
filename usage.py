#!/usr/bin/python3

from pwn import process, remote

target = process("./example")
#target = remote("localhost", 6969)

print(target.recvline())
print(target.recv(20))
print(target.recvuntil(b">> "))

target.sendline(b'2')
#print(target.recvuntil(b">> "))

target.interactive()
