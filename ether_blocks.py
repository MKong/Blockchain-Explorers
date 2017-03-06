#!/usr/bin/python2.7
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import datetime
import csv
from dateutil import parser

def getBlockChainInfo():
    index = 0
    lastBlock = 2749659
    earliest_date = parser.parse("2016-01-01T00:00:00Z")
    new_year = parser.parse("2017-01-01T00:00:00Z")
    latest_date = parser.parse("2017-01-01T07:47:49Z")
    #Get the initial mined blocks
    q = requests.get("https://etherchain.org/api/blocks/count", verify=False)
    initial_data_blocks = q.json()
    initial_mined_blocks = initial_data_blocks["data"][0]["count"]
    while (latest_date >= earliest_date):
        s = requests.get("https://etherchain.org/api/blocks/count", verify=False)
        data_blocks = s.json()
        mined_blocks = data_blocks["data"][0]["count"]
        if (index ==0):
            listOne = ['nb', "time","nb_txs","gasUsed",
            "size", "difficulty"]
            with open("ethereum_blocks_two.csv", "a") as fp:
              wr = csv.writer(fp, dialect='excel')
              wr.writerow(listOne)
        else:
            #calc the additional blocks since query startded
            diff_initial_mined_blocks = mined_blocks - initial_mined_blocks
            # offset is diff between the current mined blocks - sum of the initial difference since query started and last block.
            offset = mined_blocks - (diff_initial_mined_blocks + lastBlock)
            #return the next 100 blocks
            url = "https://etherchain.org/api/blocks/"+ str(offset)+"/"+str(100)
            r = requests.get(url, verify=False)
            data = r.json()
            # loop over all 100 blocks, inserting each one as row in csv.
            for item in data["data"]:
                print(item["number"])
                latest_date = parser.parse(item["time"])
                print(latest_date)
                if (latest_date <= new_year):
                    listOne = [item["number"], item["time"], item["tx_count"], item["gasUsed"], item["size"], item["difficulty"]]
                    with open("ethereum_blocks_two.csv", "a") as fp:
                      wr = csv.writer(fp, dialect='excel')
                      wr.writerow(listOne)
        index = index +1
        lastBlock = lastBlock - 100

while True:
    getBlockChainInfo()
