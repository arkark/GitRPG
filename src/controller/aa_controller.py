#!/usr/bin/env python
import os


def game_over_aa():
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../../ascii_art/game_over.txt", "r") as file:
        return file.read()


def level_up_aa():
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../../ascii_art/level_up.txt", "r") as file:
        return file.read()
