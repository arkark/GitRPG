#!/usr/bin/env python


def log(args):
    if not args.state.use_mp(1):
        return
    args.se_manager.play_wav("goukaku")
