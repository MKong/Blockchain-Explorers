#Blockchain Explorer Information

##Overview

These scripts connected to blockchain explorers with open APIs on the following cryptocurrencies:

1. Bitcoin
2. Ether
3. Litecoin
4. Monero
5. Zcash

Each block is appended into a `.csv` file with the appropriate attributes as described below.

###bitcoin.py

Processes the number of transactions `nb_txs`, fee, date, size, confirmations and difficulty  for each block.

To determine the range of blocks to gather, set the `earliest_date` and `latest_date` variables. Set the 'lastBlock' to be the first block to return (as it goes in reverse chronological order).

###ether.py

Processes the number of transactions `tx_count`, gas consumed `gasUsed`, size of the block `size`, difficulty and the block number.

To determine the range of blocks to gather, set the `earliest_date` and `latest_date` variables. Remove the 'new_year' variable and its references in order to gather blocks from past the new year of 2017. `lastBlock` is the first block that the script will gather (as it goes in reverse chronological order).

###litecoin.py

Processes the block number, block time, the number of transactions, the number of confirmations, the fee payed and the difficulty of the block.

To determine the range of blocks to gather, set the `earliest_date` and `latest_date` variables. Remove the 'new_year' variable and its references in order to gather blocks from past the new year of 2017. `lastBlock` is the first block that the script will gather (as it goes in reverse chronological order).

###monero.py

Processes the block header, the block timestamp and the number of transactions per block.

To determine the range of blocks to gather, set the `earliest_date` and `latest_date` variables (these dates need to be specified using a unix timestamp). Remove the 'new_year' variable and its references in order to gather blocks from past the new year of 2017. `lastBlock` is the first block that the script will gather (as it goes in reverse chronological order).

###zcash

Processes the block header, the block timestamp, the block size and the number of transactions per block.

To determine the range of blocks to gather, set the `earliest_date` and `latest_date` variables (these dates need to be specified using a unix timestamp). Remove the 'new_year' variable and its references in order to gather blocks from past the new year of 2017. `lastBlock` is the first block that the script will gather (as it goes in reverse chronological order).
