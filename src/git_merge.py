#!/usr/bin/env python
import pygame
import time
from mutagen.mp3 import MP3
from src.se_manager import play
from src.util import getColorString

def merge(cmd, se_path):
    play(se_path + "/ta/ビヨォン.mp3")