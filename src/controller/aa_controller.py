#!/usr/bin/env python
import os


def game_over_aa():
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../../ascii_art/game_over.txt", "r") as file:
        return file.read()
