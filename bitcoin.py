#!/usr/bin/python2.7
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import datetime
import csv
from dateutil import parser

def getBlockChainInfo():
    index = 0
    lastBlock= 438602
    earliest_date = parser.parse("2016-01-01T00:00:00Z")
    latest_date = parser.parse("2017-01-01T10:13:00Z")
    while(latest_date >= earliest_date):
        if (index ==0):
            listOne = ['nb', "confirmations", "time","nb_txs","fee",
            "size", "difficulty"]
        else:
            url = "http://btc.blockr.io/api/v1/block/info/" + str(lastBlock)
            r = requests.get(url, verify=False)
            data = r.json()
            listOne = [data["data"]["nb"], data["data"]["confirmations"], data["data"]["time_utc"], data["data"]["nb_txs"],data["data"]["fee"],
            data["data"]["size"], data["data"]["difficulty"]]
            latest_date = parser.parse(data["data"]["time_utc"])
            print(latest_date)
        index = index +1
        lastBlock = lastBlock - 1
        with open("bitcoin_blocks.csv", "a") as fp:
          wr = csv.writer(fp, dialect='excel')
          wr.writerow(listOne)

getBlockChainInfo()
