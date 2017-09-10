#!/usr/bin/env python
import os


def game_over_aa():
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../../ascii_art/game_over.txt", "r") as file:
        return file.read()


def level_up_aa():
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../../ascii_art/level_up.txt", "r") as file:
        return file.read()


def push_force_aa():
    # with open(os.path.dirname(os.path.abspath(__file__)) + "/../../ascii_art/explosion.ansi", "r") as file:
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../../ascii_art/explosion_100.txt", "r") as file:
        return file.read()
