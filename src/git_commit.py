#!/usr/bin/env python
from src.util import mp_zero_text


def commit(args):
    if not args.state.use_mp(2):
        return mp_zero_text("commit"), True
    args.state.add_exp(10)
    args.se_manager.play_wav("kira06")
