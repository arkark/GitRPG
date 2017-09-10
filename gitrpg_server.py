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
import src.se_manager
from src.se_manager import SE_Manager

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
from src.git_help import help_
from src.git_fail import fail_command

all_git_commands = ["add", "merge-ours", "add--interactive", "merge-recursive", "am", "merge-resolve", "annotate",
                    "merge-subtree", "apply", "merge-tree", "archive", "mergetool", "bisect", "mktag", "bisect--helper",
                    "mktree", "blame", "mv", "branch", "name-rev", "bundle", "notes", "cat-file", "pack-objects",
                    "check-attr", "pack-redundant", "check-ignore", "pack-refs", "check-ref-format", "patch-id",
                    "checkout", "peek-remote", "checkout-index", "prune", "cherry", "prune-packed", "cherry-pick",
                    "pull", "clean", "push", "clone", "quiltimport", "column", "read-tree", "commit", "rebase",
                    "commit-tree", "receive-pack", "config", "reflog", "count-objects", "relink", "credential",
                    "remote", "credential-cache", "remote-ext", "credential-cache--daemon", "remote-fd",
                    "credential-gnome-keyring", "remote-ftp", "credential-store", "remote-ftps", "describe",
                    "remote-http", "diff", "remote-https", "diff-files", "remote-testpy", "diff-index", "repack",
                    "diff-tree", "replace", "difftool", "repo-config", "difftool--helper", "request-pull",
                    "fast-export", "rerere", "fast-import", "reset", "fetch", "rev-list", "fetch-pack", "rev-parse",
                    "filter-branch", "revert", "fmt-merge-msg", "rm", "for-each-ref", "send-pack", "format-patch",
                    "sh-i18n--envsubst", "fsck", "shell", "fsck-objects", "shortlog", "gc", "show", "get-tar-commit-id",
                    "show-branch", "grep", "show-index", "hash-object", "show-ref", "help", "stage", "http-backend",
                    "stash", "http-fetch", "status", "http-push", "stripspace", "imap-send", "submodule", "index-pack",
                    "subtree", "init", "symbolic-ref", "init-db", "tag", "instaweb", "tar-tree", "log", "unpack-file",
                    "lost-found", "unpack-objects", "ls-files", "update-index", "ls-remote", "update-ref", "ls-tree",
                    "update-server-info", "mailinfo", "upload-archive", "mailsplit", "upload-pack", "merge", "var",
                    "merge-base", "verify-pack", "merge-file", "verify-tag", "merge-index", "web--browse",
                    "merge-octopus", "whatchanged", "merge-one-file", "write-tree"]


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


class HandlerArgs:
    def __init__(self, command, se_path, se_manager, state):
        self.state = state
        self.se_manager = se_manager
        self.se_path = se_path
        self.command = command


def main():
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    port = 3456
    serversock.bind(("localhost", port))  # IPとPORTを指定してバインドします
    serversock.listen(10)  # 接続の待ち受けをします（キューの最大数を指定）

    pygame.mixer.init()

    state = state_manager.load_state()
    se_path = os.path.dirname(os.path.abspath(__file__)) + "/music"
    SE = SE_Manager()

    # register sound files
    SE.register_wav("obake", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/obake.wav")
    SE.register_wav("rev", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/リバースサウンド.wav")  # checkout
    SE.register_wav("warp", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/ワープ、瞬間移動04.wav")  # clean
    SE.register_wav("gogogo", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/ゴゴゴゴゴ・・・.wav")  # clone
    SE.register_wav("kira01", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/星・キラーン01.wav")  # add
    SE.register_wav("kira06", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/星・キラーン06.wav")  # commit
    SE.register_wav("quiz", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/クイズ・出題03.wav")  # help
    SE.register_wav("hora", os.path.dirname(os.path.abspath(__file__)) + "/music/attack/ホラ貝02.wav")  # init
    SE.register_wav("marimba", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/サンザ・マリンバ03.wav")  # reset
    SE.register_wav("syun", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/シューン.wav")  # reset
    SE.register_wav("quiz", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/クイズ・間違い03.wav")  # fail

    # register handlers
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
        , "help": help_
    }

    while True:
        print('Waiting for connections...')
        clientsock, client_address = serversock.accept()

        while True:
            rcvmsg = clientsock.recv(1024)
            if rcvmsg == b'':
                continue
            # Se(os.path.dirname(os.path.abspath(__file__)) + "/music/ta/流れ星01.mp3").start()

            command = rcvmsg.decode('utf-8')
            print("Received -> " + command)
            match = re.match("git (\w+)", command)
            if match:
                print("[debug] git command detect")
                subcmd = match.group(1)
                if subcmd in handlers:
                    args = HandlerArgs(command, se_path, SE, state)
                    res = handlers[subcmd](args)
                    if res is not None:
                        clientsock.sendall((args.state.showStr() + "\n" + res).encode("utf-8"))
                    else:
                        clientsock.sendall(args.state.showStr().encode("utf-8"))
                else:
                    if subcmd not in all_git_commands:
                        args = HandlerArgs(command, se_path, SE, state)
                        fail_command(args)
                        pass

            clientsock.close()

            break


if __name__ == '__main__':
    main()
