
__author__ = 'wookie'
import pprint
from components.FileOps import writeLog, initialLogDir, makeLogDir
from components.infrastructure import getSysInfo
from components.MySQL import MySQLOps
global DBOP


runConfig = dict()
secParms = dict()

def ckheader(cEvent, cTag, cText):
    if (cEvent == 'start'):
        setTo = cTag
    else:
        setTo = None
    if (cTag == 'autohammer'):
        return True
    elif (cTag == 'config'):
        return True
    elif (cTag == 'connect'):
        return True
    elif cTag == 'import_code':
        return True
    elif cTag == 'run_code':
        return True
    elif (cTag == 'run_sql'):
        return True
    elif (cTag == 'sys_info'):
        return True
    return False


def finishSection(thisSection):
    if (thisSection == 'config'):
        initialLogDir(runConfig)
    elif (thisSection == 'connect'):
        writeLog(1, '<connect>')
        connectDB(runConfig)
        writeLog(-1,'</connect>')
    elif (thisSection =='sys_info'):
        writeLog(1, '<sys_info>')
        getSysInfo()
        writeLog(-1, '</sys_info>')
    elif (thisSection =='run_sql'):
        runSQL(runConfig, secParms)
    elif (thisSection =='run_code'):
        runCode(runConfig, secParms )
    elif (thisSection =='load_code'):
        loadCode()
    elif (thisSection =='autohammer'):
        finishIt()


def doSection(thisSection, cEvent, cTag, cText):
    if thisSection == None:
        return
    elif thisSection == 'config':
        runConfig[cTag] = cText
    elif thisSection == 'run_sql':
        secParms[cTag] = cText
    elif thisSection == 'run_code':
        secParms[cTag] = cText
    elif thisSection == 'load_code':
        runConfig[cTag] = cText


def validateConfig():
    global runConfig
    global dbConfig
    print("runConfig")
    pprint.pprint(runConfig, width=1)
    print("dbConfig")
    pprint.pprint(dbConfig, width=1)
    print('Validate config')
    if dbConfig['test'].upper() == 'TPCC':
        runConfig['logDir'] = makeLogDir(dbConfig['rdbms'], dbConfig['test'], dbConfig['warehouses'])
        copyFiles(runConfig['logDir'])
    elif dbConfig['test'].upper() == 'TPCH':
        runConfig['logDir'] = makeLogDir(dbConfig['rdbms'], dbConfig['test'], dbConfig['db_scale'])
        copyFiles(runConfig['logDir'])


def validateTest():
    print('Validate test')

def setupCode():
    #validateCode()
    print('setting up code section - I think that this is a do not care')


def runCode():
   # validateCode()
    print('Running a code section ')


def validateSQL():
    print('Validate SQL config')


def validateCode():
    print('Validate Code config')

def loadCode():
    print("Inside of load code")


def finishIt():
    print("Done with Autohammer")


def runSQL(runConfig, secParms):
    global DBOP
    if (secParms['use_db'] == 'system'):
        DBOP.connectAdmin(runConfig)
        DBOP.nowDoSQL(runConfig, secParms)
        DBOP.disconnectAdmin()
    else:
        DBOP.connectUser(runConfig)
        DBOP.nowDoSQL(runConfig, secParms)
        DBOP.disconnectUser()

def connectDB(runCOnfig):
    global DBOP
    if runConfig['rdbms'].lower() == 'oracle':
        adminOracle(runConfig)
    elif runConfig['rdbms'].lower() == 'mysql':
        DBOP = MySQLOps()
    elif runConfig['rdbms'].lower() == 'mssql':
        DBOP = MSSQLDB()
    elif runConfig['rdbms'].lower() == 'pgsql':
        adminMSSQL(runConfig)
    else:
        writeLog("ERROR: Unknown RDBMS {}i\n".format(runConfig['rdbms']))