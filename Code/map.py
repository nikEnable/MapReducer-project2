#!/usr/bin/env python
import datetime
import sys

for line in sys.stdin:
        Index, Arrival_Time, Creation_Time, x_in, y_in, z_in , user, Model, Device, gt = line.strip().split(',')
        if Arrival_Time != 'Arrival_Time':
                timestamp = int(float(Arrival_Time) / 10**9)
                x = float(x_in)
                y = float(y_in)
                z = float(z_in)
                hour = datetime.datetime.fromtimestamp(timestamp).hour
                mon  = datetime.datetime.fromtimestamp(timestamp).month
                print(f'{user}\t{mon}\t{hour}\t{x}\t{y}\t{z}')

