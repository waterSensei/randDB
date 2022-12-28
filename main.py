from randclient import randcli
from randspec import randspec
from randorder import randorder
from randaddress import getaddress
from datetime import date
import csv

installdate = date(2022, 1, 1)

title = ['JN', 'FirstName', 'LastName', 'Mobile', 'Email', 'Address', 'Sales', 'Installer', 'InstallationDate',
         'SupplyPhase', 'InvModel', 'InvBrand', 'InvSize', 'InvPhase', 'BatModel', 'BatSize', 'Backup',
         'PanelBrand', 'PanelSize', 'PanelNum', 'SysSize', 'OptBrand', 'OptModel', 'OptNum', 'Smartmeter']

with open('test.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, title)
    writer.writeheader()
    for i in range(1000):
        temp = getaddress()
        result = {'JN': 1000 +
                  i} | randcli() | temp | randorder(installdate) | randspec()
        installdate = date(int(result['InstallationDate'][6:10]), int(
            result['InstallationDate'][3:5]), int(result['InstallationDate'][0:2]))
        writer.writerow(result)
        # print(result)
        print(i+1)
