#!/usr/bin/env python
from src.util import mp_zero_text


def help_(args):
    if not args.state.use_mp(1):
        args.state.reset_combo()
        return mp_zero_text("help"), True
    args.se_manager.play_wav("question")
