# Airdrops and Snapshots

This tutorial (NOT complete) will cover very rudimentary snapshots (and possibly airdrop scripts later).

It is quite simple to take a snapshot of the top 20 holders of a token natively, by making a JSON request to the X1 RPC using Command Prompt. Getting more than the top 20 holders typically requires a significantly more advanced setup.

This tutorial includes optional but highly recommended Python code. [Python can be installed here](https://www.python.org/downloads/). Then enter `pip install pandas` in Command Prompt, to install pandas for Python.

_There are two sections in this tutorial, based on whether Python is installed or not._ The first section involves Python, and the second does not. This is to accomodate users with different levels of technical literacy.

Note: Keep in mind that the top 20 holders can include the incinerator address, LP addresses, ecosystem wallets, etc., of the token whose snapshot was taken. These may be optionally and manually excluded from the airdrop.

## Systematic snapshot and airdrop (using Python and batch files)
1. Edit the getTop20Holders.bat file and replace Platinum's mint address `ACor5a1JMRsnbMKcibnNZfbY5nfiBg3TwRvWSNUE2DVb` with the _mint address_ of the token whose top 20 holders you want to take a snapshot of.
3. Run getTop20Holders.bat in Command Prompt
4. Run json2csv.py in Python. This will generate top20_holders.csv.
5. Proportional (default) or equal-weighted allocation calculations are supported. There is also a possible exclude list (empty by default, to not exclude any address). If you want a proportional allocation with no excluded addresses: skip to step 6. If you want an equal-weighted allocation, Edit calculate_allocations.py, to make proportional=0. If you want to excude addresses, edit calculate_allocations.py and fill in the `excluded_addresses` list using proper Python syntax.
6. Run calculate_allocations.py to generate allocations.csv. (Tentative, to be continued)
7. Edit airdrop.bat to replace `MINT_ADDRESS` with your own token's mint address, and edit `PAYER_KEYPAIR` and `INPUT_FILE` to set your own kepair file and input file (allocations.csv), using _full_ file paths.
8. Run airdrop.bat

**WARNING: Airdrop.bat is extremely experimental.** It is intended only for a _brand new minted token_, where no one yet holds any tokens. Otherwise, it will not work reliably at all. This is because it attempts to create token accounts for each wallet address in allocations.csv. But if some of those wallets already have token balances (and therefore token accounts), then the script _will_ run into errors and/or highly unpredictable behavior. If you want to modify it for tokens with existing holders, you will likely need to code extensive extra logic, to check if users already have token accounts, while also making new ones for wallets without them. **You have been warned.**

## _Very_ crude, manual way to get snapshot and airdrop (no Python)

1. Edit the getTop20Holders.bat file
2. Replace Platinum's mint address `ACor5a1JMRsnbMKcibnNZfbY5nfiBg3TwRvWSNUE2DVb` with the _mint address_ of the token whose top 20 holders you want to take a snapshot of.
3. Run getTop20Holders.bat in Command Prompt
4. Get the file top20_holders.json. Use an json to csv converter to convert it to a csv file (there are many online and software tools for this).
5. Load the csv file into Excel as a spreadsheet.
6. Calculate a particular airdrop allocation (equal weight, proportional to holdings, etc.) in the spreadsheet.
7. Airdrops can be done _very_ manually by minting tokens into a single wallet, and then sending desired amounts of tokens to each address by sending them in the X1 Wallet, using the spreadsheet as a reference.

## Finishing up

Double check the actual airdrops using an explorer such as [Fortiblox](https://explorer.fortiblox.com/) and entering your token's mint address. Ensure that it was done correctly. If it wasn't, then consider possible remedies such as a relaunch.

Once you have minted and distributed all desired tokens, you can revoke the mint authority by running the command: `spl-token authorize <MINT ADRRESS> mint --disable`, replacing `<MINT ADRRESS>` with your token's actual mint address.

Revoking mint authority is _extremely_ important for establishing trust with users. This is because tokens that are mintable (without an _extremely_ clear compelling reason, such as custuom logic for fair permissionless minting) are a huge red flag for many potential buyers.
