#!/usr/bin/env python


def config(args):
    if not args.state.use_mp(1):
        return
    args.se_manager.play_wav("attack43")
