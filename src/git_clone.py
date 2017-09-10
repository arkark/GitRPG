#!/usr/bin/env python
from src.state_manager import State


def clone(args):
    args.state = State.reset_state()
    args.se_manager.play_wav("gogogo")
