#!/usr/bin/env python

import sys
from typing import List

import socket

from src.data.data import Data


def main(arg):
    if len(arg) < 2:
        return
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = 3456
    client.connect(("localhost", port))

    cmd = arg[1].strip()

    client.send(cmd.encode('utf-8'))

    response = client.recv(8192)  # レシーブは適当な2進数にします（大きすぎるとダメ）
    if response != b"":
        raw = response.decode("utf-8")
        data = Data.decode(raw)
        print(data.message)
        if data.abort:
            exit(1)



if __name__ == '__main__':
    main(sys.argv)
