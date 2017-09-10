import pygame
import time
from mutagen.mp3 import MP3
from src.se_manager import play
from src.util import getColorString
from src.util import getColorText

def branch(args):
    args.se_manager.play_wav("metro")

#def branch(cmd, se_path):
    #play(se_path + "/ta/流れ星01.mp3)