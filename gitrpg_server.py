#!/usr/bin/env python

import sys
from typing import List

import socket, os

import pygame
import re
from mutagen.mp3 import MP3
import time

import sys
import threading
import time
from subprocess import Popen

import pygame
from mutagen.mp3 import MP3


#
from src import state_manager
from src.git_add import add
from src.git_commit import commit
from src.git_init import init
from src.git_log import log
from src.git_push import push
from src.git_merge import merge
from src.git_status import status
from src.git_show import show
from src.git_branch import branch
from src.git_clone import clone
from src.git_checkout import checkout
from src.git_reset import reset
from src.git_fetch import fetch
from src.git_config import config
from src.git_diff import diff
from src.git_clean import clean
from src.git_rebase import rebase


class Se(threading.Thread):
    def __init__(self, se_full_path):
        super(Se, self).__init__()
        self.se_full_path = se_full_path

    def run(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.se_full_path)
        pygame.mixer.music.play(1)
        sound = MP3(self.se_full_path)

        # print("length", sound.info.length)
        time.sleep(sound.info.length)





def main():
    host = "localhost"  # お使いのサーバーのホスト名を入れます
    port = 3456  # クライアントと同じPORTをしてあげます

    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversock.bind((host, port))  # IPとPORTを指定してバインドします
    serversock.listen(10)  # 接続の待ち受けをします（キューの最大数を指定）

    pygame.mixer.init()

    state = state_manager.load_state()
    se_path = os.path.dirname(__file__) + "/music"

    handlers = {
        "add": add
        , "commit": commit
        , "init": init
        , "log": log
        , "push": push
        , "merge": merge
        , "status": status
        , "show": show
        , "branch": branch
        , "clone": clone
        , "checkout": checkout
        , "reset": reset
        , "fetch": fetch
        , "config": config
        , "diff": diff
        , "clean": clean
        , "rebase": rebase
    }

    while True:
        print('Waiting for connections...')
        clientsock, client_address = serversock.accept()  # 接続されればデータを格納

        while True:
            rcvmsg = clientsock.recv(1024)
            print('Received -> %s' % (rcvmsg))
            if rcvmsg == b'':
                continue
            Se(os.path.dirname(os.path.abspath(__file__)) + "/music/ta/流れ星01.mp3").start()

            command = rcvmsg.decode('utf-8')
            match = re.match("git (\w+)", command)
            if match:
                print("[debug] git command detect")
                subcmd = match.group(1)
                if subcmd in handlers:
                    handlers[subcmd](command, se_path)

            clientsock.sendall(b"hoge")  # メッセージを返します
            clientsock.close()

            break


if __name__ == '__main__':
    main()