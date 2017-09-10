#!/usr/bin/env python

import os
import re
import sys
from typing import List
from src import state_manager
from src.git_add import add
from src.git_commit import commit
from src.git_init import init
from src.git_log import log
from src.git_push import push
from src.git_merge import merge
from src.git_status import status
from src.git_show import show
from src.git_branch import branch

state = state_manager.load_state()
se_path = os.path.dirname(__file__) + "/music"

handlers = {
    "add": add
    ,"commit": commit
    ,"init": init
    ,"log": log
    ,"push": push
    ,"merge": merge
    ,"status": status
    ,"show": show
    ,"branch": branch
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
            if subcmd in handlers:
                handlers[subcmd](command, se_path)


if __name__ == "__main__":
    main(sys.argv)
