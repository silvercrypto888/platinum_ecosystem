# Airdrops and Snapshots

This tutorial (NOT complete) will cover very rudimentary snapshots (and possibly airdrop scripts later).

It is quite simple to take a snapshot of the top 20 holders of a token natively, by making a JSON request to the X1 RPC. Getting more than the top 20 holders typically requires a significantly more advanced setup.

This tutorial includes optional but highly recommended Python code. [Python can be intalled here](https://www.python.org/downloads/). There are two sections in this tutorial, based on whether python is installed or not.

Note: Keep in mind that the top 20 holders can include the incinerator address, LP addresses, ecosystem addresses, etc., of the token whose snapshot was taken. These may be manually excluded from the airdrop.

_Very_ crude, manual way to get snapshot and airdrop (no Python)

1. Edit the getTop20Holders.bat file
2. Replace Platinum's mint address `ACor5a1JMRsnbMKcibnNZfbY5nfiBg3TwRvWSNUE2DVb` with the _mint address_ of the token whose top 20 holders you want to take a snapshot of.
3. Run getTop20Holders.bat in Command Prompt
4. Get the file top20_holders.json. Use an json to csv converter (there are many online and software tools for this).
5. Load the csv file into Excel as a spreadsheet.
6. Calculate a particular airdrop allocation (equal weight, proportional to holdings, etc.) in the spreadsheet.
7. Airdrops can be done _very_ manually by minting tokens into a single wallet and then sending desired amounts of tokens to each address, using the spreadsheet as a reference.

Systematic snapshot and airdrop (using Python and batch files)
1. Edit the getTop20Holders.bat file
2. Replace Platinum's mint address `ACor5a1JMRsnbMKcibnNZfbY5nfiBg3TwRvWSNUE2DVb` with the _mint address_ of the token whose top 20 holders you want to take a snapshot of.
3. Run getTop20Holders.bat in Command Prompt
4. Run json2csv.py in Python. This will generate top20_holders.csv.
5. (To Be continued)
