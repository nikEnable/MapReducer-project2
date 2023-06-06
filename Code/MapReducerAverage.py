# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 23:51:55 2023

@author: nikEnable
"""

import datetime
from mrjob.job import MRJob

class MRMobileStationData(MRJob):
    
    def mapper(self, _, line):
        (Index, Arrival_Time, Creation_Time, x_in, y_in, z_in , User, Model, Device, gt) = line.split(',')
        if Arrival_Time != 'Arrival_Time':  # skip the line
            timestamp = int(float(Arrival_Time) / 10**9)  # convert nanoseconds to seconds
            arrival_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            x = float(x_in)
            y = float(y_in)
            z = float(z_in)
            hour = datetime.datetime.fromtimestamp(timestamp).hour
            mon = datetime.datetime.fromtimestamp(timestamp).month
            yield (User, mon, hour), (x, y, z)

        
    def reducer(self, User, values):
        sum_x = 0
        sum_y = 0
        sum_z = 0
        count = 0
        for i in values:
            x, y, z = i
            sum_x+= x
            sum_y+= y
            sum_z+= z
            count+= 1
        aver_x = sum_x / (count)
        aver_y = sum_y / (count)  
        aver_z = sum_z / (count)  
        yield (User),  (aver_x, aver_y, aver_z)

if __name__ == '__main__':
    MRMobileStationData.run()
