#!/usr/bin/env python
import sys

filename = "test.txt"
try:
  with open(filename, "r") as fh:
    lines = fh.readlines()
    [print(line, end="") for line in lines]
except IOError as err:
  print(err, file=sys.stderr)
