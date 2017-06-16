__author__ = 'wookie'

from components.FileOps import initialLogDir
def configProc(dbConf):
    if (dbConf['test'].upper() == 'TPCC'):
        initialLogDir(dbConf['rdbms'].upper(), dbConf['test'].upper(), dbConf['warehouses'])
    elif (dbConf['test'].upper() == 'TPCH'):
        initialLogDir(dbConf['rdbms'].upper(), dbConf['test'].upper(), dbConf['db_scale'])
