#!/usr/bin/env python
import pygame
import time
from mutagen.mp3 import MP3
from src.se_manager import play
from src.util import getColorString
from src.util import getColorText

def fetch(args):
    args.state.use_mp(-1)
    args.se_manager.play_wav("pyui")
