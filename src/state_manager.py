#!/usr/bin/env python

import sys
from typing import List
import pickle
import os

state_path = os.path.dirname(__file__) + "/../state"


class State:
    def __init__(self, lv, max_mp, mp, max_hp, hp):
        self.hp = hp
        self.max_hp = max_hp
        self.mp = mp
        self.max_mp = max_mp
        self.lv = lv

    def __repr__(self):
        return f"lv:{self.lv}\nmax_mp: {self.max_mp}\n max_hp: {self.max_hp}"

    def lv_up(self, hp_delta, mp_delta):
        self.max_hp += hp_delta
        self.max_mp += mp_delta
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.lv += 1
        self.save()

    def use_mp(self, amount):
        self.mp -= amount
        self.save()

    def damage(self, amount):
        self.hp -= amount
        self.save()

    def showStr(self):
        return f"LV: {self.lv} HP: {self.hp}/{self.max_hp} MP: {self.mp}/{self.max_mp}"

    def save(self):
        with open(state_path + '/state.pickle', 'wb') as f:
            pickle.dump(self, f)


def load_state():
    if not os.path.exists(state_path):
        os.mkdir(state_path)
    if not os.path.exists(f"{state_path}/state.pickle"):
        return State(1, 10, 10, 10, 10)

    with open(state_path + '/state.pickle', 'rb') as f:
        return pickle.load(f)
