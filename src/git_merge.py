#!/usr/bin/env python
from src.util import mp_zero_text


def merge(args):
    if not args.state.use_mp(4):
        args.state.reset_combo()
        return mp_zero_text("merge"), True
    args.se_manager.play_wav("mahou11")
