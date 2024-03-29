from datetime import datetime, timedelta

import math
import sys
import csv
import numpy as np

mu = 3.986e+5


def dateconvert(timeset):
    year = 2000 + int(timeset[0:2])
    decimal_days = float(timeset[2:])
    datetimeconvert = datetime(year, 1, 1) + timedelta(decimal_days - 1)
    
    return datetimeconvert
    
def altitudeconvert(meanmotion):
    sma = (mu/4*(24*60*60/ float(meanmotion) / math.pi)**2)**(1/3) - 6371
    
    return sma



if __name__ == '__main__':
    args = sys.argv


    # open sample TLE file
    # specify TLE file directly 
    # f = open('TLE-file/ISS-20200101-20200201.tle')
    # specify TLE file by ARGV
    f = open(args[1])

    line = f.readlines()
    f.close

    lineToList = np.array(line).reshape(-1,2).tolist()

    # print data or write to CSV
    with open('./datetime-and-altitude.csv', 'w', newline="") as f:

        writer = csv.writer(f)

        for l in lineToList:
            # print(dateconvert(l[0].split()[3]), altitudeconvert(l[1].split()[7][0:11]))

            # if you want to write to a CSV file, uncomment below line
            writer.writerow([dateconvert(l[0].split()[3]), altitudeconvert(l[1].split()[7][0:11])])