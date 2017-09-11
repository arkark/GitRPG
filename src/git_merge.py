#!/usr/bin/env python


def merge(args):
    if not args.state.use_mp(4):
        return
    args.se_manager.play_wav("mahou11")
