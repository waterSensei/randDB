from randclient import randcli
from randspec import randspec
from randorder import randorder
from randaddress import getaddress
from pprint import pprint
from datetime import date
import csv

installdate = date(2022, 1, 1)
# pprint(cliinfo())
# print(getaddress())
# pprint(orderinfo(1,1,2022))
# pprint(sys_spec(), sort_dicts=False)
# FirstName,LastName,Mobile,Email,Address,Sales,Installer,InstallationDate,SupplyPhase,InvModel,InvBrand,InvSize,InvPhase,BatModel,BatSize,Backup,PanelBrand,PanelSize,PanelNum,SysSize,OptBrand,OptModel,OptNum,Smartmeter

title = ['FirstName', 'LastName', 'Mobile', 'Email', 'Address', 'Sales', 'Installer', 'InstallationDate',
         'SupplyPhase', 'InvModel', 'InvBrand', 'InvSize', 'InvPhase', 'BatModel', 'BatSize', 'Backup',
         'PanelBrand', 'PanelSize', 'PanelNum', 'SysSize', 'OptBrand', 'OptModel', 'OptNum', 'Smartmeter']

with open('test.csv', 'w', newline='') as file:
    # print(result.keys())
    writer = csv.DictWriter(file, title)
    writer.writeheader()
    for i in range(10):
        temp = getaddress()
        result = randcli() | temp | randorder(installdate) | randspec()
        installdate = date(int(result['InstallationDate'][6:10]), int(
            result['InstallationDate'][3:5]), int(result['InstallationDate'][0:2]))
        writer.writerow(result)
        pprint(result, sort_dicts=False)
