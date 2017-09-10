#!/usr/bin/env python

import sys
from typing import List
import json


class Data:
    def __init__(self, message, abort):
        self.abort = abort
        self.message = message

    def encode(self):
        return json.dumps({"abort": self.abort, "message": self.message}).encode("utf-8")

    @staticmethod
    def decode(s):
        obj = json.loads(s)
        return Data(obj["message"], obj["abort"])
