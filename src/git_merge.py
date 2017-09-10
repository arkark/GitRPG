#!/usr/bin/env python
import pygame
import time
from mutagen.mp3 import MP3
from src.se_manager import play
from src.util import getColorString
from src.util import getColorText

def merge(cmd, se_path):
    play(se_path + "/ta/魔法的音11.mp3")