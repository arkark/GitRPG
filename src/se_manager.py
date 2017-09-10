#!/usr/bin/env python


import sys
import threading
import time
from subprocess import Popen

import pygame
from mutagen.mp3 import MP3


#
# class Se(threading.Thread):
#     def __init__(self, se_full_path):
#         super(Se, self).__init__()
#         self.se_full_path = se_full_path
#
#     def run(self):
#         pygame.mixer.init()
#         pygame.mixer.music.load(self.se_full_path)
#         pygame.mixer.music.play(1)
#         sound = MP3(self.se_full_path)
#
#         print("length", sound.info.length)
#         time.sleep(sound.info.length)


def play(se_full_path):
    Popen([__file__, se_full_path], stdin=None, stdout=None, stderr=None, close_fds=True)


def _play(fp):
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play(1)
    sound = MP3(fp)

    time.sleep(sound.info.length)


def main():
    if len(sys.argv) < 2:
        return

    fp = sys.argv[1]
    _play(fp)


if __name__ == '__main__':
    main()
