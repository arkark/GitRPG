#!/usr/bin/env python

import sys
from typing import List

import socket

host = "localhost"  # お使いのサーバーのホスト名を入れます
port = 3456  # 適当なPORTを指定してあげます

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # オブジェクトの作成をします

client.connect((host, port))

client.send(b"from nadechin")

response = client.recv(4096)  # レシーブは適当な2進数にします（大きすぎるとダメ）

print(response)


def main(arg):
    if len(arg) < 2:
        return

    cmd = arg[1]
    print(cmd)


if __name__ == '__main__':
    main(sys.argv)
