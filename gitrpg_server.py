#!/usr/bin/env python

import sys
from typing import List

import socket
import os
import subprocess

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
from src.data.data import Data
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
from src.git_pull import pull
from src.git_revert import revert

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
    # initialize
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    port = 3456
    serversock.bind(("localhost", port))  # IPとPORTを指定してバインドします
    serversock.listen(10)  # 接続の待ち受けをします（キューの最大数を指定）
    pygame.mixer.init()
    state = state_manager.load_state()
    se_path = os.path.dirname(os.path.abspath(__file__)) + "/music"
    SE = SE_Manager()
    p = subprocess.Popen(['git', 'config', "-l"],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=False)
    # print('return: %d' % (p.wait(),))
    rerere = re.compile("user.name=(\w+)")
    usermanes = [re.match(rerere, a).group(1) for a in [a.decode("utf-8") for a in p.stdout.readlines()] if
                 "user.name" in a]
    if len(usermanes) == 1:
        username = usermanes[0]
    else:
        username = "unknown"

    # print(f'stdout: {}')
    # print('stderr: %s' % (p.stderr.readlines(),))
    print(username)

    # register sound files
    SE.register_wav("obake", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/obake.wav")
    SE.register_wav("rev", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/リバースサウンド.wav")  # checkout
    SE.register_wav("warp", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/ワープ、瞬間移動04.wav")  # clean
    SE.register_wav("gogogo", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/ゴゴゴゴゴ・・・.wav")  # clone
    SE.register_wav("kira01", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/星・キラーン01.wav")  # add
    SE.register_wav("kira06", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/星・キラーン06.wav")  # commit
    SE.register_wav("quiz", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/クイズ・出題03.wav")  # help
    SE.register_wav("hora", os.path.dirname(os.path.abspath(__file__)) + "/music/attack/ホラ貝02.wav")  # init
    SE.register_wav("marimba", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/サンザ・マリンバ03.wav")  # show
    SE.register_wav("syun", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/シューン.wav")  # reset
    SE.register_wav("quiz", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/クイズ・間違い03.wav")  # fail
    SE.register_wav("metro", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/メトロノーム（早）.wav")  # branch
    SE.register_wav("goukaku", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/合格！（キンコンカンコン）.wav")  # log
    SE.register_wav("pi", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/ピ！.wav")  # status
    SE.register_wav("pyui", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/引っ付くピュイ！.wav")  # fetch
    SE.register_wav("attack43", os.path.dirname(os.path.abspath(__file__)) + "/music/muci/単発音・アタック43.wav")  # config
    SE.register_wav("attack01", os.path.dirname(os.path.abspath(__file__)) + "/music/muci/単発音・アタック01.wav")  # diff
    SE.register_wav("biyorn02", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/びよーんと伸びる02.wav")  # pull
    SE.register_wav("pyurn", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/飛んでいく・ひゅ〜〜ん.wav")  # revert
    SE.register_wav("moriagari", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/盛り上がり02.wav")  # push
    SE.register_wav("mahou11", os.path.dirname(os.path.abspath(__file__)) + "/music/ta/魔法的音11.wav")  # merge
    SE.register_wav("R01", os.path.dirname(os.path.abspath(__file__)) + "/music/muci/BGM・ループ・軽快R01.wav")  # rebase
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
        , "pull": pull
        , "revert": revert
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
            if command == "gitrpg on" or command == "gitrpg off":
                continue
            if command == "gitrpg status":
                # TODO　状況表示
                continue
            if command == "gitrpg reset":
                # TODO　reset
                continue

            match = re.match("git (\w+)", command)
            if match:
                print("[debug] git command detect")
                subcmd = match.group(1)
                if subcmd in handlers:
                    args = HandlerArgs(command, se_path, SE, state)
                    obj = handlers[subcmd](args)
                    if obj is None:
                        res, abort = None, False
                    else:
                        if type(obj) == str:
                            res, abort = obj, None
                        else:
                            res, abort = obj[0], obj[1]
                    if res is not None:
                        data = Data(username + ": " + args.state.showStr() + "\n" + res, abort)
                        clientsock.sendall(data.encode())
                    else:
                        data = Data(username + ": " + args.state.showStr(), abort)
                        clientsock.sendall(data.encode())
                else:
                    if subcmd not in all_git_commands:
                        args = HandlerArgs(command, se_path, SE, state)
                        fail_command(args)
                        pass

            clientsock.close()

            break


if __name__ == '__main__':
    main()
