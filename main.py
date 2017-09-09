#!/usr/bin/env python

import sys
from typing import List
from src.template import template


def main(arg: List[str]):
    command = arg[1]
    if command.startswith("git"):
        template(arg[1])


if __name__ == "__main__":
    main(sys.argv)
