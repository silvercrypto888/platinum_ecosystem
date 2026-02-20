# Airdrops and Snapshots

This tutorial will cover very rudimentary snapshots and airdrops. Note that the airdrop tool is experimental, and it will not work for tokens launched on XDEX. The airdrop tool can only work for tokens launched via Solana CLI.

_Disclaimer: This project is still under active development, and some files are experimental._

It is relatively simple to take a snapshot of the top 20 holders of a token, by making a `getTokenLargestAccounts` JSON request to the X1 RPC in Python, then mapping the ATAs (Associated Token Addresses) to their personal wallets. The `get_holders.py` script does this with minimal configuration needed. Getting more than the top 20 holders typically requires a much more advanced scripting or programming environment.

_This tutorial requires Python to be installed, along with the pandas and requests modules._ [Python can be installed here](https://www.python.org/downloads/). After that, enter `pip install pandas requests` in Command Prompt, to install pandas and requests for Python.

This tutorial will also include a few scripts (not an all-in-one program), to increase modularity and versatility for new devs. For example, not all users may want to use all the scripts, they but could still find some of them useful.

## Systematic snapshot (requires Python)

1. Edit `get_holders.py`, replacing Platinum's mint address `ACor5a1JMRsnbMKcibnNZfbY5nfiBg3TwRvWSNUE2DVb` in `MINT_ADDRESS = "ACor5a1JMRsnbMKcibnNZfbY5nfiBg3TwRvWSNUE2DVb"` with _the mint address of the token whose snapshot you want to capture_.
2. Run `get_holders.py` in Python. This will generate `top20wallets.csv`, which contains wallet token amounts for the top 20 holders.
3. By default, the token supply is 1,000,000,000 for the total airdrop allocation (summed over all holders), the airdrop is proportional to holdings, and no addresses are excluded. If this is fine, skip the next step. Otherwise:
4. (optional, unless changes wanted) Edit `calculate_allocations.py` and set your desired total token supply for `TOTAL_AIRDROP_SUPPLY`. Proportional (default) or equal allocation calculations are supported. If you want an equal allocation, edit `calculate_allocations.py` to set `DISTRIBUTION_TYPE = "equal"`. There is also a possible exclude list `EXCLUDED_ADDRESSES` (empty by default), which must be filled in with any addresses you would want to exclude.
5. Run `calculate_allocations.py` in Python to generate allocations.csv. This contains the airdrop allocations.

Note: Keep in mind that the top 20 holders can include the incinerator address, LP addresses, team/ecosystem wallets, etc., of the token whose snapshot was taken. These may be optionally and manually excluded from the airdrop by editing `calculate_allocations.py`, as described above.

## Automatic airdrop (batch file)

**WARNING: `airdrop.bat` is extremely experimental and very early in development. `airdrop.bat` is _only_ intended for a _brand new minted token_, where no one yet holds any tokens. Otherwise, if there are existing holders, it will not work reliably at all.** This is because it attempts to create token accounts for each wallet address in `allocations.csv`. But if some of those wallets already have token balances (and therefore token accounts), then the script _will_ run into errors and/or unpredictable behavior. If you want to modify it for tokens with existing holders, you might want to code extensive extra logic, to check if users already have token accounts, while also making new token accounts for wallets without them. **You have been warned.**

1. _(Experimental)_ Edit `airdrop.bat` to replace `MINT_ADDRESS` with _your own token's mint address_. Also, edit `PAYER_KEYPAIR` and `INPUT_FILE` to set your own keypair file and input file (allocations.csv), possibly using full file paths.
2. _(Experimental)_ Run `airdrop.bat`.

## Alternative Manual Airdrop (no batch file)

This is a very crude, manual, tedious way to do the airdrop. It is only mentioned because some may want to trade off the time taken and risks (human error) of doing a manual airdrop vs. the technical risks of using a more experimental batch script, like the one shared here. The airdrop can be done manually by minting tokens into a single wallet, and then sending desired amounts of tokens to each address by sending them in the X1 Wallet. One can open the allocations.csv file in Excel as a reference.

## Finishing up

Double check the realized airdrop amounts. You can use an explorer such as [Fortiblox](https://explorer.fortiblox.com/) and enter your token's mint address. Ensure that it was done correctly. If it wasn't done correctly, then consider possible remedies, such as a re-launch with proper notice to your community. Alternatively, if only a handful of users had missed their airdrop, you could manually do a second mint / airdrop just to accomodate them.

## Revoking Mint Authority

Once you have minted and distributed all desired tokens, you can revoke the mint authority by opening Command Prompt and running this command: `spl-token authorize <MINT ADDRESS> mint --disable`, replacing `<MINT ADDRESS>` with your token's actual mint address. _Disclaimer: This will permanently and irreversibly remove your ability to mint more tokens for the mint address you provided._

Revoking mint authority is _extremely_ important for establishing trust with users. Mintable tokens are a huge red flag for many potential users. The only exception is an extremely compelling reason for allowing mints, such as custom logic for fair permissionless minting.

The game theory behind this: If a token is mintable, then an extractor can mint billions of tokens, and then sell them to the liquidity pool to instantly drain its funds, even if the LP tokens are burned. Revoking mint authority (when combined with burned liquidity) is a clear signal that you can no longer do a rug pull like that.

## Advanced Snapshots

*Note: This is recommended only for users who have at least some limited programming experience.*

There is a more advanced script, `multi_allocation.py`, that allows you to get the 20 holders of multiple different token communities, and then calculate a combined allocation across users of all those communities. This could be a very powerful tool, since it allows you to target the top participants of multiple projects. It will use the multi_allocation folder as its data workspace. It needs significantly more setup. More documentation is [there](/airdrop/multi_allocation).
