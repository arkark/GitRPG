#!/usr/bin/env python
import pygame
import time
from mutagen.mp3 import MP3
from src.se_manager import play
from src.util import getColorString
from src.util import getColorText
def init(cmd, se_path):
    play(se_path + "/ta/ホラ貝02.mp3")