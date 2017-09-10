#!/usr/bin/env python
import pygame
import time
from mutagen.mp3 import MP3
from src.se_manager import play
from src.util import getColorString
from src.util import getColorText
import os

def log(cmd, se_path):
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    play(se_path + "/ta/ビヨォン.mp3")
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/../text.txt', 'r')
    string = f.read()
    string = getColorString(string, 5, 30, 41)
    return string
