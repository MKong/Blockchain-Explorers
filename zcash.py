#!/usr/bin/python2.7
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import datetime
import csv
from dateutil import parser

def getBlockChainInfo():
    index = 0
    lastBlock= 4548
    earliest_date = datetime.datetime.fromtimestamp(1451606400)
    new_year = datetime.datetime.fromtimestamp(1483228800)
    latest_date = datetime.datetime.fromtimestamp(1483228800)
    offset = 0
    previousBlock = '00040fe8ec8471911baa1db1266ea15dd06b4a8a5c453883c000b031973dce08'
    while(latest_date >= earliest_date):
        if (index ==0):
            listOne = ['nb', "time","nb_txs", "size", "time"]
            has_date = True
        else:
            url = "https://api.zcha.in/v1/mainnet/blocks/" + previousBlock
            r = requests.get(url, verify=False)
            data = r.json()
            has_date = False
            if ("timestamp" in data):
                has_date = True
                latest_date = datetime.datetime.fromtimestamp(data['timestamp'])
                print(latest_date)
                nb_txs = len(data['transactions'])
                if (latest_date <= new_year):
                    listOne = [data["height"] + 1, latest_date, nb_txs, data["size"], data["time"]]
            previousBlock = data['previousBlock']
            print (previousBlock)
            print(data['hash'])
        if ((index ==0 or latest_date <= new_year) and has_date==True):
            with open("zcash_blocks.csv", "a") as fp:
              wr = csv.writer(fp, dialect='excel')
              wr.writerow(listOne)
        index = index +1
        offset = offset + 20
getBlockChainInfo()
