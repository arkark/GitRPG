#!/usr/bin/env python


def log(args):
    args.state.use_mp(1)
    args.se_manager.play_wav("goukaku")
