#!/usr/bin/python3

from os import fork, execv, read, write
import pty, tty, sys

class process():
    def __init__(self, filename):
        self.filename = filename
        self.child_fd = None
        self.spawn()

    def spawn(self):
        command = [ self.filename ]

        child_pid, child_fd = pty.fork()
        if not child_pid:
            execv(command[0], command)

        self.child_fd = child_fd

    def recv(self, num_bytes):
        data = b''
        try:
            data = read(self.child_fd, num_bytes)
        except Exception as e:
            print(e)
        return data

    def recvuntil(self, needle):
        data = b''
        while True:
            try:
                byte = read(self.child_fd, 1)
                data += byte
                if data.find(needle, 0, len(data)) > -1:
                    break
            except Exception as e:
                print(e)
                break
        
        return data

    def recvline(self):
        line = b''
        while True:
            try:
                byte = read(self.child_fd, 1)
                line += byte
                if byte == b'\n':
                    break
            except Exception as e:
                print(e)
                break
        return line

    def sendline(self, data):
        write(self.child_fd, data + b'\n')

    def interactive(self):
        print('Switching to interactive mode')
        mode = tty.tcgetattr(sys.stdin)
        tty.setraw(sys.stdin)
        try:
            pty._copy(self.child_fd, pty._read, pty._read)
        except Exception as e:
            print(e)

import socket, time, telnetlib

class remote():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()

    def connect(self):
        self.sock.connect((self.host, self.port))

    def recv(self, num_bytes):
        data = b''
        try:
            data = self.sock.recv(num_bytes)
        except Exception as e:
            print(e)
        return data

    def recvuntil(self, needle):
        data = b''
        while True:
            try:
                byte = self.sock.recv(1)
                data += byte
                if data.find(needle, 0, len(data)) > -1:
                    break
            except Exception as e:
                print(e)
                break
        
        return data

    def recvline(self):
        line = b''
        while True:
            try:
                byte = self.sock.recv(1)
                line += byte
                if byte == b'\n':
                    break
            except Exception as e:
                print(e)
                break
        return line

    def sendline(self, data):
        self.sock.send(data + b'\n')

    def interactive(self):
        tsock = telnetlib.Telnet()
        tsock.sock = self.sock
        tsock.interact()
