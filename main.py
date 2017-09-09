#!/usr/bin/env python

import sys
from typing import List


def main(arg: List[str]):
    print(arg[1:])


if __name__ == "__main__":
    main(sys.argv)
