#!/usr/bin/env python
import re

from src.controller.aa_controller import push_force_aa


def push(args):
    if args.command.find(" -f") != -1 or args.command.find(" --force") != -1:
        if not args.state.use_mp(11):
            args.state.reset_state()
            return
        args.se_manager.play_wav("pushf")
        return push_force_aa()
    else:
        if not args.state.use_mp(7):
            args.state.reset_state()
            return
        args.state.add_exp(50)
        args.se_manager.play_wav("moriagari")


invalid_escape = re.compile(r'\\[0-7]{1,3}')  # up to 3 digits for byte values up to FF


def replace_with_byte(match):
    return chr(int(match.group(0)[1:], 8))


def repair(brokenjson):
    return invalid_escape.sub(replace_with_byte, brokenjson)
