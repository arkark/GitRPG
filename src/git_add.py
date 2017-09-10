#!/usr/bin/env python


import pygame


def add(cmd, se_path):
    print(cmd + cmd)
    print(se_path)

    # mixerモジュールの初期化
    pygame.mixer.init()
    # 音楽ファイルの読み込み
    pygame.mixer.music.load(se_path + "/attack/ゴング.mp3")
    # 音楽再生、および再生回数の設定(-1はループ再生)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.play(1)
    # pygame.mixer.music.play(-1)
    print("aaa.")
