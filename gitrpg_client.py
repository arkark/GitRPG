#!/usr/bin/env python

import sys
from typing import List

import socket


def main(arg):
    if len(arg) < 2:
        return
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = 3456
    client.connect(("localhost", port))

    cmd = arg[1]
    print(cmd)
    client.send(cmd.encode('utf-8'))

    response = client.recv(4096)  # レシーブは適当な2進数にします（大きすぎるとダメ）
    if response != "":
        print(response.decode("utf-8"))


if __name__ == '__main__':
    main(sys.argv)
