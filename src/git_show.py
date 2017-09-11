#!/usr/bin/env python
from src.util import mp_zero_text


def show(args):
    if not args.state.use_mp(1):
        args.state.reset_combo()
        return mp_zero_text("show"), True
    args.se_manager.play_wav("marimba")
