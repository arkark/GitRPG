#!/usr/bin/env python

import sys
from typing import List
from src.template import template
import pygame.mixer
import time, os, re
from src.git_add import add

from src import state_manager

state = state_manager.load_state()
se_path = os.path.dirname(__file__) + "/music"

handlers = {
    "add": add
}


def main(arg: List[str]):
    if len(arg) < 2:
        print("[debug] invalid arguments count")
    command = arg[1]
    if command == "gitrpg on":
        state_manager.gitrpg_on(state)
    elif command == "gitrpg off":
        state_manager.gitrpg_off(state)
    else:
        if not state.enable:
            return
        match = re.match("git (\w+)", command)
        if match:
            print("[debug] git command detect")
            subcmd = match.group(1)
            print(subcmd)
            if subcmd in handlers:
                handlers[subcmd](command, se_path)


if __name__ == "__main__":
    main(sys.argv)
