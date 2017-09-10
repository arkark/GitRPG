#!/usr/bin/env python
import pygame
import time
from mutagen.mp3 import MP3
from src.se_manager import play
from src.util import getColorString
from src.util import getColorText
import os

def init(args):
    args.se_manager.play_wav("hora")
    with open(os.path.dirname(os.path.abspath(__file__))+ "/../ascii_art/game_start.txt", "r") as file:
    	string = file.read()
    	return string
