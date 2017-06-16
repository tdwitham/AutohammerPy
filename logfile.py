__author__ = 'wookie'
import datetime
def createLog():
    print("Creating the log file using parameters and timestamp")
    now = datetime.datetime.now
    print(now.isoformat())

