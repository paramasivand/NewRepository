################################################################
# Prgram Name      : Migration Validation
# Author           : Paramasivan Dorai
# Date             : 5-June-2019
# Input Parameters : Deployment Folder and date of deployment
# Description      : The program validates the migration folder
#                    for file types, validation of code modules
###############################################################

import sys
import time
import datetime
import os
import cx_Oracle

# Parameter Defenition

SuccessReturnCode = 0
ErrorReturnCode   = 255
WarningReturnCode = -255
DeploymentFolder  = sys.argv[1:]
SysDate           = datetime.datetime.now()
tmstmp = str(SysDate.strftime("%Y%m%d%H%M"))
LogFile           = 'LogFile_'+tmstmp+'.log'



os.system('cls')

print (LogFile)
print ("\n \t\t Deployment Validation Script ")
print ("\n\t Deployment Folder : %s " % DeploymentFolder )
print ("\n\t SysDate : %s " % SysDate )
print ("\n\t LogFIle : %s " % LogFile )

dsn_tns = cx_Oracle.makedsn ('localhost', '1527', service_name = 'XE' )
conn = cx_Oracle.connect (user= r'param_dorai', password ='Test123', dsn=dsn_tns)

c = conn.cursor()

c.execute('select * from comphead') # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[0],'-',row[1],'-',row[2]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
conn.close()
