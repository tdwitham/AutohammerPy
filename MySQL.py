__author__ = 'wookie'
# (c) 2016,2017 - Timothy D. Witham tim.wookie.witham@gmail.com
# Licensed under BSD 2-Clause
from components.FileOps import writeLog, putSectionParms, putConfigParms, getSQLCode, writeTrace
from components.infrastructure import subSQL
import pymysql
import sys
import re
class MySQLOps:

    aCur = None
    aCon = None

    
    def connectAdmin(self, runConfig):
        global aCur
        global aCon
        DEFPORT = "3306"
        DEFHOST = 'localhost'
        DEFUSER =  "root"
        DEFPASSWORD = ""
        DEFDB = "system"
        writeLog(0,"admin_pass is {}".format(runConfig.get('admin_pass', "WTF")))
        try:
            aCon =  pymysql.connect(host=runConfig.get('hostname', 'localhost'),
                                   port=runConfig.get('port', 3306),
                                   user=runConfig.get('user', 'root'),
                                   password=runConfig.get('admin_pass', "") )
        except all:
            writeLog(0,"ERROR: Unable to connect to mysql database as admin")
            putConfigParms(runConfig)
            exit()

        aCur = aCon.cursor()
        writeLog(0,"Connected to MySQL as {}".format(runConfig['admin']))
    
    def disconnectAdmin(self):
        global aCur
        global aCon
        aCur.close()
        #thisCon.close()
        writeTrace("Disconnect from MySQL as admin")
    
    
    def connectUser(self, runConfig):
        global aCur
        global aCon
        DEFPORT = 3306
        DEFHOST = 'localhost'
        DEFUSER =  "root"
        DEFPASSWORD = ""
        DEFDB = "system"
        try:
            aCon = pymysql.connect(host=runConfig.get('hostname', DEFHOST),
                                   port=runConfig.get('port', DEFPORT),
                                   user=runConfig.get('user', DEFUSER),
                                   password=runConfig.get('user_pass', DEFPASSWORD),
                                   db=runConfig.get('database_name','mysql'))
        except all:
            writeLog(0,"ERROR: Unable to connect to user database")
            putConfigParms(runConfig)
            exit()
        aCur = aCon.cursor()
        writeLog(0,"Connected to MySQLi as {}".format(runConfig['user']))
    
    def disconnectUser(self):
        global aCur
        global aCon
        aCur.close()
        aCon.close()
        writeTrace("Disconnect from MySQLi as user")

    def nowDoSQL(self, runConfig, secParms):
        global aCur
        global aCon
        inSQL = getSQLCode(runConfig, secParms)
        writeTrace("Read in SLQ ==={}===".format(inSQL))
        if secParms.get('sql_sub') != 'yes':
            writeTrace("No substitutions")
            outSQL = inSQL
        else:
            writeTrace("Will substitute")
            outSQL = subSQL(secParms, inSQL)
        writeTrace("Will Execute ==={}".format(outSQL))
        try:
            aCur.execute(outSQL)
        except pymysql.DataError as e:
            raise e
            writeLog(0, "DataError with query ==={}===".format(outSQL))
        except pymysql.IntegrityError as e:
            raise e
            writeLog(0, "IntegrityError with query ==={}===".format(outSQL))
        except pymysql.InternalError as e:
            raise e
            writeLog(0, "InternalError with query ==={}===".format(outSQL))
        except pymysql.NotSupportedError as e:
            raise e
            writeLog(0, "NotSupportedError with query ==={}===".format(outSQL))
        except pymysql.OperationalError as e:
            raise e
            writeLog(0, "OperationError with query ==={}===".format(outSQL))
        except pymysql.ProgrammingError as e:
            raise e
            writeLog(0, "ProgrammingError with query ==={}===".format(outSQL))
        aCon.commit()



