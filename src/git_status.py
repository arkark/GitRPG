#!/usr/bin/env python
from src.util import mp_zero_text


def status(args):
    if not args.state.use_mp(1):
        args.state.reset_combo()
        return mp_zero_text("status"), True
    args.se_manager.play_wav("pi")
    args.state.add_exp(10)
