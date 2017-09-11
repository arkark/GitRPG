#!/usr/bin/env python
from src.util import mp_zero_text


def remote(args):
    if not args.state.use_mp(1):
        args.state.reset_combo()
        return mp_zero_text("remote"), True
    args.state.add_exp(20)
    args.se_manager.play_wav("remote")
