#!/usr/bin/env python


def revert(args):
    args.state.add_exp(20)
    args.state.damage(3)
    args.se_manager.play_wav("hyurn")
