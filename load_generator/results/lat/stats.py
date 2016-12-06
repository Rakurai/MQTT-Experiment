#!/usr/bin/env python

import sys
import numpy

fname = sys.argv[1]

timestamps = []
latencies = []

with open(fname) as f:
 for line in f.readlines():
  ts, lat = line.strip().split()
  timestamps.append(float(ts))
  latencies.append(float(lat))

rate = timestamps[-1] - timestamps[0]
lat_mean = numpy.mean(latencies)
lat_std = numpy.std(latencies)
lat_min = numpy.min(latencies)
lat_max = numpy.max(latencies)

#print "%.6f msgs/s, %.6f mean, %.6f std, %.6f min, %.6f max" % (rate, lat_mean, lat_std, lat_min, lat_max)
print "%.6f,%.6f,%.6f,%.6f,%.6f" % (rate, lat_mean, lat_std, lat_min, lat_max)
