#!/usr/bin/env python

import sys
from typing import List
from datetime import datetime
import pickle
import os
from src.util import base_color, yellow, red

import time

from src.util import getColorText
from src.util import getColorString

state_path = os.path.dirname(__file__) + "/../state"

lv_exp = [0, 80, 200, 400, 800, 1200, 1600, 3200, 6400, 12800]
lv_extends = [
    (5, 5),
    (10, 10),
    (15, 15),
    (20, 20),
    (25, 25),
    (35, 35),
    (45, 45),
]


# 現在のレベル取得
def get_level(lv_exp, exp):
    a = [(i + 1, v, exp) for i, v in enumerate(lv_exp)]
    b = [i for i, v, exp in a if exp >= v]
    return b[-1]


class State:
    def __init__(self, lv, max_mp, mp, max_hp, hp):
        self.hp = hp
        self.max_hp = max_hp
        self.mp = mp
        self.max_mp = max_mp
        self.lv = lv
        self.exp = 0
        self.combo = []
        self.last_command_time = int(time.mktime(datetime.now().timetuple()))

    def __repr__(self):
        return f"lv:{self.lv}\nmax_mp: {self.max_mp}\n max_hp: {self.max_hp}"

    # コマンドを実行したことを通知、コンボ用。
    def command(self, command):
        now = int(time.mktime(datetime.now().timetuple()))
        delta = now - self.last_command_time
        self.last_command_time = now

        # 時間回復
        self.use_mp(-1 * (delta // 3))
        if delta < 5:
            self.combo.append(command)
        else:
            self.reset_combo()

    def reset_combo(self):
        self.combo = []

    def lv_up(self):
        hp, mp = lv_extends[self.lv - 1]
        self.lv += 1
        self.max_hp += hp
        self.max_mp += mp
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.save()

    def add_exp(self, exp):
        self.exp += exp
        lv = get_level(lv_exp, self.exp)
        if lv != self.lv:
            for _ in range(lv - self.lv):
                self.lv_up()
            return True
        return False

    def use_mp(self, amount):
        self.mp -= amount
        if self.mp > self.max_mp:
            self.mp = self.max_mp
        self.save()
        return self.mp >= 0

    def damage(self, amount):
        self.hp -= amount
        self.save()

    def normalize(self):
        if self.hp < 0:
            self.hp = 0
        if self.mp < 0:
            self.mp = 0
            self.save()

    def showStr(self):
        pre = base_color(f"LV: {self.lv} HP: ")

        if float(self.hp / self.max_hp) <= 0.1:
            middle = red("{0}/{1}".format(self.hp, self.max_hp))
        elif float(self.hp / self.max_hp) <= 0.3:
            middle = yellow("{0}/{1}".format(self.hp, self.max_hp))
        else:
            middle = base_color("{0}/{1}".format(self.hp, self.max_hp))

        if float(self.mp / self.max_mp) <= 0.1:
            mp = base_color(" MP: ") + red("{0}/{1}".format(self.mp, self.max_mp))
        elif float(self.mp / self.max_mp) <= 0.3:
            mp = base_color(" MP: ") + yellow("{0}/{1}".format(self.mp, self.max_mp))
        else:
            mp = base_color(" MP: ") + base_color("{0}/{1}".format(self.mp, self.max_mp))
        return pre + middle + mp

    def save(self):
        with open(state_path + '/state.pickle', 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def reset_state():
        save_path = os.path.dirname(os.path.abspath(__file__)) + "/../state/state.pickle"
        if os.path.exists(save_path):
            os.remove(save_path)
        s = State.initial_state()
        s.save()
        return s

    @staticmethod
    def initial_state():
        return State(1, 10, 10, 10, 10)


def load_state():
    if not os.path.exists(state_path):
        os.mkdir(state_path)
    if not os.path.exists(f"{state_path}/state.pickle"):
        return State.initial_state()

    with open(state_path + '/state.pickle', 'rb') as f:
        return pickle.load(f)
