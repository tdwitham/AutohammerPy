# (c) 2016,2017 - Timothy D. Witham tim.wookie.witham@gmail.com
# Licensed under BSD 2-Clause
__author__ = 'wookie'
from sys import exit
import random
import string
import re
from components.FileOps import writeLog, writeTrace
#import xml.etree.ElementTree as ET
runConfig = dict(autohammer=None,
                 config=None,
                 test=None)
dbConfig = dict(rdbms=None,
                database_name=None,
                server=None,
                admin=None,
                admin_pass=None,
                test_user=None,
                test_user_pass=None,
                test_table_space=None,
                test_temp_space=None,
                warehouses=None)
globList = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

def putUsage():
    print("\n\tUsage:autohammer.py <configuration_file>\n\n")
    exit(1)

def openConfiguration(cfgFile):
    try:
        f = open(cfgFile, mode='rt', encoding='UTF-8')
    except FileNotFoundError:
        print("\nERROR: unable to open configuration file ---{0}---".format(cfgFile))
        print("\tSo no log directory/files have been produced")
        putUsage()
    return f

def validateCommand(argc):
    if argc < 2:
        print("Invalid Command Line --- no logs produced")
        putUsage()

def makeAlphaString(minLen, maxLen):
    stringSize = random.randint(minLen, maxLen)
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(stringSize))


def getSysInfo():
    writeLog(0,"Getting System Info")

def subSQL(secParms,inSQL):
    pString = re.sub('\s+', ' ', secParms.get('sql_params'.strip())).split()
    numArgs = len(pString)
    writeTrace(inSQL)
    writeTrace("Number of list elements are {}".format(numArgs))
    if numArgs == 1:
        return(inSQL.format(secParms.get(pString[0])))
    elif numArgs == 2:
        return(inSQL.format(secParms.get(pString[0]), secParms.get(pString[1])))
    elif numArgs == 3:
        return(inSQL.format(secParms.get(pString[0]), secParms.get(pString[1]), secParms.get(pString[2])))
    elif numArgs == 4:
        return(inSQL.format(secParms.get(pString[0]), secParms.get(pString[1]),
                            secParms.get(pString[2]), secParms.get(pString[3])))
    elif numArgs == 5:
        return(inSQL.format(secParms.get(pString[0]), secParms.get(pString[1]),
                            secParms.get(pString[2]), secParms.get(pString[3]),
                            secParms.get(pString[4])))
    elif numArgs == 6:
        return(inSQL.format(secParms.get(pString[0]), secParms.get(pString[1]),
                            secParms.get(pString[2]), secParms.get(pString[3]),
                            secParms.get(pString[4]), secParms.get(pString[5])))
    elif numArgs == 7:
        return(inSQL.format(secParms.get(pString[0]), secParms.get(pString[1]),
                            secParms.get(pString[2]), secParms.get(pString[3]),
                            secParms.get(pString[4]), secParms.get(pString[5]),
                            secParms.get(pString[6])))
    elif numArgs == 8:
        return(inSQL.format(secParms.get(pString[0]), secParms.get(pString[1]),
                            secParms.get(pString[2]), secParms.get(pString[3]),
                            secParms.get(pString[4]), secParms.get(pString[5]),
                            secParms.get(pString[6]), secParms.get(pString[7])))
    elif numArgs == 9:
        return(inSQL.format(secParms.get(pString[0]), secParms.get(pString[1]),
                            secParms.get(pString[2]), secParms.get(pString[3]),
                            secParms.get(pString[4]), secParms.get(pString[5]),
                            secParms.get(pString[6]), secParms.get(pString[7]),
                            secParms.get(pString[8])))
    elif numArgs == 10:
        return(inSQL.format(secParms.get(pString[0]), secParms.get(pString[1]),
                            secParms.get(pString[2]), secParms.get(pString[3]),
                            secParms.get(pString[4]), secParms.get(pString[5]),
                            secParms.get(pString[6]), secParms.get(pString[7]),
                            secParms.get(pString[8]), secParms.get(pString[9])))
    else:
        writeLog(0, "ERROR: Can only substitute between 1 and 10 parameters")
        exit()




if __name__ == '__main__':
    print("Number of characters in globList are {0}".format(len(globList)))
    print("Alpha string of 1 to 20 characters is {}".format(makeAlphaString(1,20)))
    print("Alpha string of 1 to 20 characters is {}".format(makeAlphaString(1,20)))
    print("Alpha string of 1 to 20 characters is {}".format(makeAlphaString(1,20)))


