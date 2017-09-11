#!/usr/bin/env python


def checkout(args):
    if not args.state.use_mp(1):
        return
    args.se_manager.play_wav("rev")
