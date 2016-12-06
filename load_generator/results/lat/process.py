#!/usr/bin/env python

import sys

filename = sys.argv[1]

messages = {}

with open(filename) as f:
 for line in f.readlines():
  seq, send, recv = line.strip().split()
  sendf = float(send)
  recvf = float(recv)
  messages[int(seq)] = (sendf, recvf-sendf)

sequences = sorted(messages.keys())

for seq in sequences:
 msg = messages[seq]
 print "%.6f %.6f" % (msg[0], msg[1]*1000000)
