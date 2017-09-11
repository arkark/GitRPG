#!/usr/bin/env python


def diff(args):
    if not args.state.use_mp(1):
        return
    args.se_manager.play_wav("attack01")
