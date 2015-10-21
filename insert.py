import os
import sys

with open(sys.argv[1], 'r') as h:
  s = h.read()
  t = sys.stdin.read()
  sys.stdout.write(s % t)
