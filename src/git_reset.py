#!/usr/bin/env python
import pygame
import time
from mutagen.mp3 import MP3
from src.se_manager import play
from src.util import getColorString
from src.util import getColorText


def reset(args):
    args.state.add_exp(20)
    args.state.damage(1)
    args.se_manager.play_wav("syun")
