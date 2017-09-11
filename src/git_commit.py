#!/usr/bin/env python


def commit(args):
    args.state.add_exp(10)
    args.se_manager.play_wav("kira06")
