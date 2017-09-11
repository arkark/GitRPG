#!/usr/bin/env python


def status(args):
    if not args.state.use_mp(1):
        return
    args.se_manager.play_wav("pi")
    args.state.add_exp(10)
