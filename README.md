# Platinum Ecosystem on X1 Blockchain, and Newbie Dev Guide
This repo has two purposes:

1. To store open-source code for the Platinum Ecosystem on X1 Blockchain
2. To serve as a Newbie Dev Guide for aspiring new X1 devs

The guide will be very simple and assume minimal prior skills, with moderate handholding. :\) The topics covered may go through Token-2022 Extensons and airdrops/snapshots, but likely no further. This guide can allow aspiring X1 Builders to easily launch nontrivial token ecosystems of their own design, while possibly also performing highly generous and competitive industry practices (airdrops and burned LP) to help attract a following in the X1 community!

Familiarity (but not much knowledge) is expected:
1. Basic familiarity with Windows and Command prompt. This tutorial is primarily intended for Windows users.
2. Basic familiarity with blockchains, sending funds, etc.
(Linux or Windows Subsystem for Linux is very useful for making advanced dApps, but not necessary for this tutorial)

To get started wih the CLI:

1. [Install the Solana CLI](https://docs.solanalabs.com/cli/install) using instructions for your OS.
2. Verify installation: Start Command Prompt (or Linux bash) and type `solana --version`.
3. Set RPC for X1: `solana config set --url https://rpc.mainnet.x1.xyz`
4. Generate a keypair: `solana-keygen new`. Do not _ever_ share your secret phrase _or_ keypair.
5. Get your wallet address from previous command's output, or by typing: `solana address`

Obtain XNT, X1's native coin. Install the [X1 Wallet](https://chromewebstore.google.com/detail/x1-wallet/kcfmcpdmlchhbikbogddmgopmjbflnae). USDC can be bridged from Solana using the [X1 bridge](https://app.bridge.x1.xyz/). Then swapped to XNT on [XDEX](https://app.xdex.xyz/swap). If you have zero funds for gas, you can join the [X1 Blockchain Telegram](https://t.me/+qPGGU8WFFtczNDEz) and request a tiny amount of XNT for initial gas fees.

You should now have the Solana CLI configured for X1 development, and your wallet should have enough funds to mint tokens on X1.

If you want to launch tokens with no custom behavior, then you can more easily launch them on [XDEX](https://app.xdex.xyz/swap) in the "Mint token" section, although launching such tokens via CLI is possible as an exercise. Regardless of how you launched your token, you can add liquidity in the "Liquidity" section of XDEX. Adding liquidity gives you LP tokens. If you want to "burn" some or all of your LP tokens to increase trust in your token, then send the LP tokens to the incinerator addess: `1nc1nerator11111111111111111111111111111111`

_Disclaimer: Burning tokens is irreversible._ Please carefully check LP tokens before sending them to the incinerator, and keep in mind that liquidity (including your funds deposited in the pool) cannot be withdrawn once the associated LP tokens are burned.

If you want to launch tokens with moderately sophisticated behavior then _stay tuned_.

There is a very simple airdrop / snapshot scripts folder. Future simple guides could feature tokens on X1 with various Token-2022 Extensions. These extensions are very powerful, and they allow beginner devs to very quickly create tokens with nontrivial features such as interest rates, transfer fees, soulbound (non-transferable) properties, and so on!
