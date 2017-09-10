#!/usr/bin/env python


import pygame
import time
from mutagen.mp3 import MP3
from src.se_manager import play
from src.util import getColorString


def add(args):
    args.se_manager.play_wav("kira01")
    # play(se_path + "/ta/流れ星01.mp3")
    # play(se_path + "/ta/星・キラーン01.mp3")

    # # mixerモジュールの初期化
    # pygame.mixer.init()
    # # 音楽ファイルの読み込み
    # pygame.mixer.music.load(se_path + "/attack/ゴング.mp3")
    # # 音楽再生、および再生回数の設定(-1はループ再生)
    # while pygame.mixer.music.get_busy():
    #     pygame.time.Clock().tick(10)
    # pygame.mixer.music.play(1)
    # # pygame.mixer.music.play(-1)
    # sound = MP3(se_path + "/attack/ゴング.mp3")
    #
    # print("length",sound.info.length)
    # time.sleep(2)
