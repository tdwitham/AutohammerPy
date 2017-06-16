#!/usr/local/bin/python3
__author__ = 'wookie'
import sys
import time
import os
import shutil
import datetime
import string
contextDirs = {'components', 'CONFIG', 'DOC', 'HTML', '__pycache__', 'PythonPackages'}
contextFiles = {'autohammer.py', 'FOR_TPCC.txt', 'TODO.txt', 'tpch_common_prime_factors.xlsx' }


traceIt = 'on'
indents = 0
logFile = None

def makeLogDir(rdbms, test, size):
    """

    :rtype : object
    """
    while True:
        timeNow = datetime.datetime.now().strftime('%Y-%m-%dh%Hm%Ms%S')
        logDir = "{0}_{1}_{2}_on_{3}".format(rdbms.upper(), test.upper(), size, timeNow)
        if not os.path.exists(logDir):
            os.makedirs(logDir,mode=0o770)
            return logDir
        time.sleep(1)


def initialLogDir(runConfig):
    global logFile
    global indents
    if runConfig['test'].lower() == 'tpcc':
        thisLog = makeLogDir(runConfig['rdbms'], runConfig['test'], runConfig['warehouses'])
    elif runConfig['test'].lower() == 'tpch':
        thisLog = makeLogDir(runConfig['rdbms'], runConfig['test'], runConfig['size'])
    elif runConfig['test'].lower() == 'tpcds':
        thisLog = makeLogDir(runConfig['rdbms'], runConfig['test'], runConfig['size'])
    copyfiles(thisLog)
    logFile = open(thisLog+'/run.log', mode='w')
    writeLog(1,"<autohammer>")
    writeLog(1,'<config>')
    putConfigParms(runConfig)
    writeLog(-1,'<config>')


def copyfiles(logDir):
    for d in contextDirs:
        shutil.copytree(d, '{}/{}'.format(logDir,d))
    for f in contextFiles:
        shutil.copy(f, logDir)

def writeTrace(sout):
    if traceIt == "on":
        writeLog(0,"TRACING==="+sout)

def writeLog(toChange, toWrite):
    global indents
    if toChange == 1 :
        logFile.write('\t'*indents + toWrite + '\n')
        indents = indents + 1
    elif toChange == -1:
        indents = indents - 1
        logFile.write('\t'*indents + toWrite + '\n')
    else:
        logFile.write('\t'*indents + toWrite + '\n')

def getSQLCode(runConfig, secParms):
    scriptDir = os.path.dirname(os.path.realpath(sys.argv[0]))
    writeTrace("ScripDir is {}".format(scriptDir))
    if (secParms.get('component') == 'yes'):
        compSQL = os.path.join(scriptDir,"components", secParms.get('file_in'))
        writeTrace("Trying SQL file {}".format(compSQL))
        if not os.path.exists(compSQL):
            compSQL = os.path.join(scriptDir, "components", runConfig.get('test').lower(), runConfig.get('rdbms').lower(), secParms.get('file_in'))
            writeTrace("Trying SQL file {}".format(compSQL))
            if not os.path.exists(compSQL):
                writeLog(0,"No component found by that name")
                exit()
    else:
        if os.path.exists(secParms('file_in')):
            compSQL = secParms('file_in')
        else:
            writeLog(0,"No file {} found".format(secParms['file_in']))
            exit()
    writeTrace("Using SQL file {}".format(compSQL))
    f = open(compSQL, 'r')
    sin = f.read()
    f.close
    return sin






def makeTrace(sin):
    if (traceIt == 'on'):
        print(sin)

def putConfigParms(runConfig):
    for k in runConfig:
        writeLog(0,'<{}>{}</{}>'.format(k,runConfig[k],k))

def putSectionParms(secParams):
    for k in secParams:
        writeLog(0,'<{}>{}</{}>'.format(k,secParams[k],k))

