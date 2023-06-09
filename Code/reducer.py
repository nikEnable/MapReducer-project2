#! /usr/bin/env python

import sys
import datetime

cur_user  = None
cur_month = None
cur_hour  = None
sum_x = 0
sum_y = 0
sum_z = 0
count = 0

for line in sys.stdin:
    (user, month, hour, x_in, y_in, z_in) = line.strip().split("\t")
    x = float(x_in)
    y = float(y_in)
    z = float(z_in)
    if cur_user != user or cur_month != month or cur_hour != hour:
        if  cur_user is not None and cur_month is not None and cur_hour is not None:
            aver_x = sum_x / count
            aver_y = sum_y / count
            aver_z = sum_z / count
            sum_x = 0
            sum_y = 0
            sum_z = 0
            count = 0
            print(f'{cur_user}\t{cur_month}\t{cur_hour}\t{aver_x}\t{aver_y}\t{aver_z}')
    cur_user  = user
    cur_month = month
    cur_hour  = hour
    sum_x += x
    sum_y += y
    sum_z += z
    count += 1

if  cur_user is not None and cur_month is not None and cur_hour is not None:
    aver_x = sum_x / count
    aver_y = sum_y / count
    aver_z = sum_z / count
    print(f'{cur_user}\t{cur_month}\t{cur_hour}\t{aver_x}\t{aver_y}\t{aver_z}')







