#!/usr/bin/env python

import sys
from typing import List
from src.template import template

from src import state_manager

state = state_manager.load_state()


def main(arg: List[str]):
    # print("[debug]gitrpg hooking")
    # print(state)
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

        if command.startswith("git"):
            template(arg[1])


if __name__ == "__main__":
    main(sys.argv)
