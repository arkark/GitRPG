#!/usr/bin/env python


def fail_command(args):
    args.se_manager.play_wav("quiz")
    args.state.damage(7)
