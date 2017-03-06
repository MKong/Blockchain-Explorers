#!/usr/bin/python2.7
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import datetime
import csv
from dateutil import parser

def getBlockChainInfo():
    index = 0
    lastBlock= 1166522
    earliest_date = datetime.datetime.fromtimestamp(1451606400)
    new_year = datetime.datetime.fromtimestamp(1483228800)
    latest_date = datetime.datetime.fromtimestamp(1483228800)
    while(latest_date >= earliest_date):
        if (index ==0):
            listOne = ['nb', "time","nb_txs"]
        else:
            url = "http://moneroblocks.info/api/get_block_header/" + str(lastBlock)
            r = requests.get(url, verify=False)
            data = r.json()
            latest_date = datetime.datetime.fromtimestamp(data['block_header']['timestamp'])
            print(latest_date)
            print(lastBlock)
            nb_txs = 0
            if ("tx_hashes" in data):
                nb_txs = len(data['block_header']['tx_hashes'])
            if (latest_date <= new_year):
                listOne = [lastBlock, latest_date, nb_txs]
        if (index ==0 or latest_date <= new_year):
            with open("monero_blocks.csv", "a") as fp:
              wr = csv.writer(fp, dialect='excel')
              wr.writerow(listOne)
        index = index +1
        lastBlock = lastBlock - 1

getBlockChainInfo()
