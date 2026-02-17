# Airdrops and Snapshots

This tutorial will cover very rudimentary snapshots (and possibly airdrop scripts later). _Disclaimer: This tool is still under active development, and some files are experimental._

It is relatively simple to take a snapshot of the top 20 holders of a token natively even using Command Prompt, by making a JSON request to the X1 RPC. Getting more than the top 20 holders typically requires a much more advanced scripting or programming environment.

This tutorial includes optional but highly recommended Python code. _There are two sections in this tutorial, based on whether Python is installed or not. The first section requires Python, and the second does not._ This is to accomodate users with different levels of technical literacy.

_The first section of this tutorial requires Python and pandas to be installed._ [Python can be installed here](https://www.python.org/downloads/). After that, enter `pip install pandas` in Command Prompt, to install pandas for Python. This tutorial will also include a variety of scripts (not an all-in-one program), to increase modularity and versatility for new devs. For example, not all users may be able to use all the scripts, they but could still find some of them useful.

## Systematic snapshot and airdrop (requires Python)

**WARNING: these scripts are still under development. In particular, airdrop.bat is extremely experimental. airdrop.bat is _only_ intended for a _brand new minted token_, where no one yet holds any tokens. Otherwise, if there are existing holders, it will not work reliably at all.** This is because it attempts to create token accounts for each wallet address in allocations.csv. But if some of those wallets already have token balances (and therefore token accounts), then the script _will_ run into errors and/or highly unpredictable behavior. If you want to modify it for tokens with existing holders, you will likely need to code extensive extra logic, to check if users already have token accounts, while also making new token accounts for wallets without them. **You have been warned.**

1. Edit the getTop20Holders.bat file and replace Platinum's mint address `ACor5a1JMRsnbMKcibnNZfbY5nfiBg3TwRvWSNUE2DVb` with the _mint address_ of the token whose top 20 holders you want to take a snapshot of.
2. Run getTop20Holders.bat in Command Prompt. This will generate top20_holders.json.
3. Run json2csv.py in Python. This will generate top20_holders.csv.
4. By default, the token supply is 1,000,000,000 for the total airdrop (summed over all holders), the airdrop is proportional to holdings, and no addresses are excluded. If this is fine, skip the next step. Otherwise:
5. (optional, unless changes desired) Edit calculate_allocations.py and set your desired total token supply for `TOTAL_AIRDROP_SUPPLY`. Proportional (default) or equal allocation calculations are supported. If you want an equal-weighted allocation, edit calculate_allocations.py to set `DISTRIBUTION_TYPE = "equal"`. There is also a possible exclude list `EXCLUDED_ADDRESSES` (empty by default), which must be filled in with any addresses you would want to exclude.
6. Run calculate_allocations.py to generate allocations.csv.
7. _(Experimental)_ Edit airdrop.bat to replace `MINT_ADDRESS` with _your own token's mint address_. Also, edit `PAYER_KEYPAIR` and `INPUT_FILE` to set your own kepair file and input file (allocations.csv), possibly using full file paths.
8. _(Experimental)_ Run airdrop.bat.

Note: Keep in mind that the top 20 holders can include the incinerator address, LP addresses, team/ecosystem wallets, etc., of the token whose snapshot was taken. These may be optionally and manually excluded from the airdrop by editing calculate_allocations.py, as described above.

## Alternative (no Python)

This is a very crude, manual, tedious way to take the snapshot and do the airdrop. It is only shared because it requires minimal technical expertise, and it therefore does not involve Python. There is also more handholding here.

1. Edit the getTop20Holders.bat file. (You can do this in Notepad)
2. Replace Platinum's mint address `ACor5a1JMRsnbMKcibnNZfbY5nfiBg3TwRvWSNUE2DVb` with the _mint address_ of the token whose top 20 holders you want to take a snapshot of, then save it.
3. Run getTop20Holders.bat. You can do this easily by double-clicking it in the file explorer. An alternative is starting Command Prompt, then navigating to its folder using the `cd <folder path>` command with the right folder paths, then entering `getTop20Holders.bat`. Either way, this will create or overwrite top20_holders.json, in the same folder that getTop20Holders.bat is in.
4. Get the file top20_holders.json. Use a json to csv converter to convert it to a csv file (there are many online and software tools, [like this one](https://convertcsv.com/json-to-csv.htm)).
5. Load the csv file into Excel as a spreadsheet.
6. Calculate a particular airdrop allocation (equal, proportional, etc.) in the Excel spreadsheet. You can calculate a proportional airdrop by multiplying all token holder amounts by this number: _Desired total airdrop amount / sum of all token holdings across eligible top 20 holders_. Exclusions can also be done manually by dropping rows.
7. Airdrops can be done manually by minting tokens into a single wallet, and then sending desired amounts of tokens to each address by sending them in the X1 Wallet, using the spreadsheet as a reference.

## Finishing up

Double check the realized airdrop amounts. You can use an explorer such as [Fortiblox](https://explorer.fortiblox.com/) and enter your token's mint address. Ensure that it was done correctly. If it wasn't done correctly, then consider possible remedies, such as a re-launch with proper notice to your community.

Once you have minted and distributed all desired tokens, you can revoke the mint authority by running the command: `spl-token authorize <MINT ADDRESS> mint --disable`, replacing `<MINT ADDRESS>` with your token's actual mint address. _This will permanently and irreversibly remove your ability to mint new tokens._

Revoking mint authority is _extremely_ important for establishing trust with users. Tokens that are mintable are a huge red flag for many potential users. The only exception is an extremely compelling reason for allowing mints, such as custom logic for fair permissionless minting.
