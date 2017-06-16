# (c) 2016,2017 - Timothy D. Witham tim.wookie.witham@gmail.com
# Licensed under BSD 2-Clause
__author__ = 'wookie'
import datetime
def createLog():
    print("Creating the log file using parameters and timestamp")
    now = datetime.datetime.now
    print(now.isoformat())

