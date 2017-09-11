#!/usr/bin/env python
import pygame
import time
from mutagen.mp3 import MP3
from src.se_manager import play
from src.util import getColorString
from src.util import getColorText

def rebase(args):
    if not args.state.use_mp(3):
        return
    args.se_manager.play_wav("R01")
