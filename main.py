#!/usr/bin/env python

import sys
from typing import List
from src.template import template
import pygame.mixer
import time

from src import state_manager

state = state_manager.load_state()


def main(arg: List[str]):
    # print("[debug]gitrpg hooking")
    # print(state)
    if len(arg) < 2:
        print("[debug] invalid arguments count")
    command = arg[1]
    if command == "gitrpg on":
        state_manager.gitrpg_on(state)
    elif command == "gitrpg off":
        state_manager.gitrpg_off(state)
    else:
        if not state.enable:
            return

        if command.startswith("git"):
            template(arg[1])
            # mixerモジュールの初期化
            pygame.mixer.init()
            # 音楽ファイルの読み込み
            pygame.mixer.music.load("music/attack/ゴング.mp3")
            # 音楽再生、および再生回数の設定(-1はループ再生)
            pygame.mixer.music.play(-1)
            f = open('text.txt', 'r')
            string = f.read()
            print(string)
            time.sleep(5)
            # 再生の終了
            pygame.mixer.music.stop()



if __name__ == "__main__":
    main(sys.argv)
