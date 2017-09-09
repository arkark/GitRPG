#!/usr/bin/env python

import sys
from typing import List
from src.template import template
import pygame.mixer
import time


def main(arg: List[str]):
    command = arg[1]
    if command.startswith("git"):
        template(arg[1])
        # mixerモジュールの初期化
        pygame.mixer.init()
        # 音楽ファイルの読み込み
        pygame.mixer.music.load("mondo_02.mp3")
        # 音楽再生、および再生回数の設定(-1はループ再生)
        pygame.mixer.music.play(-1)

        time.sleep(5)
        # 再生の終了
        pygame.mixer.music.stop()




if __name__ == "__main__":
    main(sys.argv)
