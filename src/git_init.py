#!/usr/bin/env python
import os

from src.state_manager import State
from src.util import getColorString


def init(args):
    args.state = State.reset_state()
    args.se_manager.play_wav("hora")
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../ascii_art/kuma_and_git_rpg.txt", "r") as file:
        string1 = file.read()
        string1 = getColorString(string1, 1, 37, 44)
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../ascii_art/game_start.txt", "r") as file:
        string2 = file.read()
        string2 = getColorString(string2, 5, 37, 40)
        return string1 + '\n' + string2
