#!/usr/bin/env python


def pull(args):
    args.state.use_mp(-1)
    args.state.add_exp(10)
    args.se_manager.play_wav("biyorn02")
