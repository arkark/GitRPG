import pygame
import time
from mutagen.mp3 import MP3
from src.se_manager import play


def branch(cmd, se_path):
    play(se_path + "/ta/流れ星01.mp3")