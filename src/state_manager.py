#!/usr/bin/env python

import sys
from typing import List
import pickle
import os

state_path = os.path.dirname(__file__)+"/../state"


class State:
    def __init__(self, lv, max_mp, mp, max_hp, hp, enable):
        self.hp = hp
        self.max_hp = max_hp
        self.mp = mp
        self.max_mp = max_mp
        self.enable = enable
        self.lv = lv

    def __repr__(self):
        return f"lv:{self.lv}\nenable: {self.enable}"


def gitrpg_on(state):
    print("[debug]gitrpg turn on!")
    state.enable = True
    save_state(state)


def gitrpg_off(state):
    print("[debug]gitrpg turn off!")
    state.enable = False
    save_state(state)


def save_state(state):
    # print("[debug]gitrpg save state!")
    with open(state_path + '/state.pickle', 'wb') as f:
        pickle.dump(state, f)


def load_state():
    if not os.path.exists(state_path):
        os.mkdir(state_path)
    if not os.path.exists(f"{state_path}/state.pickle"):
        return State(1, 10, 10, 10, 10, True)

    with open(state_path + '/state.pickle', 'rb') as f:
        return pickle.load(f)
