#!/usr/bin/env python
from src.util import mp_zero_text


def stash(args):
    if not args.state.use_mp(2):
        args.state.reset_combo()
        return mp_zero_text("stash"), True
    args.se_manager.play_wav("harisen01")
