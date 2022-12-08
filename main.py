from randclient import randcli
from systeminfo import sys_spec
from randorder import randorder
from randaddress import getaddress
from pprint import pprint
from random import randrange
import datetime
import csv

installdate = datetime.date(2022,1,1)
# pprint(cliinfo())
# print(getaddress())
# pprint(orderinfo(1,1,2022))
# pprint(sys_spec(), sort_dicts=False)
# FirstName,LastName,Mobile,Email,Address,Sales,Installer,InstallationDate,SupplyPhase,InvModel,InvBrand,InvSize,InvPhase,BatModel,BatSize,Backup,PanelBrand,PanelSize,PanelNum,SysSize,OptBrand,OptModel,OptNum,Smartmeter

title = ['FirstName', 'LastName', 'Mobile', 'Email', 'Address', 'Sales', 'Installer', 'InstallationDate', 
         'SupplyPhase', 'InvModel', 'InvBrand', 'InvSize', 'InvPhase', 'BatModel', 'BatSize', 'Backup',
         'PanelBrand', 'PanelSize', 'PanelNum', 'SysSize', 'OptBrand', 'OptModel', 'OptNum', 'Smartmeter']

with open('test.csv','w',newline='') as file:
    result = randcli()|getaddress()|randorder(installdate)|sys_spec()
    # print(result.keys())
    writer = csv.DictWriter(file,title)
    writer.writeheader()


    # for i in range(0):
    #     result = cliinfo()|getaddress()|orderinfo(installdate)|sys_spec()
    #     installdate = datetime.date(int(result['InstallationDate'][6:10]),int(result['InstallationDate'][3:5]),int(result['InstallationDate'][0:2]))
    #     writer.writerow(result)
    #     print(installdate)
    #     pprint(result, sort_dicts=False)