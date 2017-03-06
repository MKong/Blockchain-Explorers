#!/usr/bin/python2.7
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import datetime
import csv
from dateutil import parser

def getBlockChainInfo():
    index = 0
    lastBlock = 2760580
    earliest_date = parser.parse("2016-01-01T00:00:00Z")
    new_year = parser.parse("2017-01-01T00:00:00Z")
    latest_date = parser.parse("2017-01-01T07:47:49Z")
    while(latest_date >= earliest_date):
        if (index ==0):
            listOne = ['nb', "time","nb_txs","gasUsed",
            "size", "difficulty"]
        else:
            url = "https://etherchain.org/api/block/" + str(lastBlock)
            r = requests.get(url, verify=False)
            data = r.json()
            print(data["data"][0]["number"])
            latest_date = parser.parse(data["data"][0]["time"])
            print(latest_date)
            if (latest_date <= new_year):
                listOne = [data["data"][0]["number"], data["data"][0]["time"], data["data"][0]["tx_count"], data["data"][0]["gasUsed"], data["data"][0]["size"],data["data"][0]["difficulty"]]
        if (index ==0 or latest_date <= new_year):
            with open("ethereum_blocks_two.csv", "a") as fp:
              wr = csv.writer(fp, dialect='excel')
              wr.writerow(listOne)
        index = index +1
        lastBlock = lastBlock - 1

while True:
    getBlockChainInfo()
