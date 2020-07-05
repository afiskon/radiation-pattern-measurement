#!/usr/bin/env python3 -u
# vim: set ai et ts=4 sw=4:

from math import pi
import matplotlib.pyplot as plt
import csv

xs = []
ys = []
with open('raw-data.csv', newline = '') as f:
    for row in csv.reader(f, delimiter = ',', quotechar = '"'):
        xs += [ 2*pi*float(row[0])/360 ]
        ys += [ float(row[1]) ]

max_y = max(ys)
ys = [ y - max_y for y in ys ]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )

ax = plt.subplot(111, projection='polar')
ax.set_theta_offset(2*pi*90/360) 
ax.plot(xs, ys, linestyle = 'solid', linewidth=3)
ax.set_rmax(0)
ax.set_rticks([-6*i for i in range(0,7)])
ax.set_yticklabels([''] + [str(-6*i) for i in range(1,7)])
ax.set_rlabel_position(0)
ax.set_thetagrids(range(0, 360, 15))
ax.set_theta_direction(-1)
ax.grid(True)

fig.savefig('measured.png')
