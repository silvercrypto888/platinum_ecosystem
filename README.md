# Platinum Ecosystem on X1 Blockchain, and Newbie Dev Guide
This repo has two purposes:

1. To document open-source code for the Platinum Ecosystem on the X1 Blockchain
2. To serve as a Newbie Dev Guide for aspiring new X1 devs

The guide will be very simple and assume minimal prior skills, with plenty of handholding. :\) The topics covered may go through Token-2022 Extensions such as interest rates, and airdrops/snapshots for top 20 holders. However, this guide will likely go no further than that. This guide can allow aspiring X1 Builders to easily launch token ecosystems with extensions that they desire, like interest rates.

This guide also shares some game theory on practices that can help builders to distinguish themselves from _extractors_ (shortsighted devs). This guide will tell you how to perform highly generous and competitive industry practices (airdrops and burned liquidity) to help attract a following in the X1 community!

Basic exposure (but not much knowledge and familiarity) is expected with:
1. Basic exposure to Windows and Command Prompt. This tutorial is primarily intended for Windows users.
2. Basic exposure to blockchains, crypto wallets, sending funds, etc.

(Basic exposure to programming principles is highly useful for the tutorial, which includes Python scripts, but it is not strictly necessary. Linux or Windows Subsystem for Linux is very useful for making advanced dApps, but is not necessary for this tutorial)

## Dipping Your Toe Into Building on X1

X1 is an SVM (Solana Virtual Machine) compatible blockchain, which means that devs can use the Solana CLI to build on X1. To get started with the CLI:

1. [Install the Solana CLI](https://docs.solanalabs.com/cli/install) using instructions for your OS.
2. Verify installation: Start Command Prompt (or Linux bash) and type `solana --version`.
3. Set RPC for X1: `solana config set --url https://rpc.mainnet.x1.xyz`
4. Generate a keypair: `solana-keygen new`. You can record the secret phrase. Do not _ever_ share your secret phrase _or_ keypair with others.

You can see your wallet address for reference from previous command's output, or by typing: `solana address`

Obtain XNT, X1's native coin, to perform operations. Install the [X1 Wallet](https://chromewebstore.google.com/detail/x1-wallet/kcfmcpdmlchhbikbogddmgopmjbflnae). USDC can be bridged from Solana using the [X1 bridge](https://app.bridge.x1.xyz/). Then swapped to XNT on [XDEX](https://app.xdex.xyz/swap). If you have zero funds for gas, you can join the [X1 Blockchain Telegram](https://t.me/+qPGGU8WFFtczNDEz) and request a tiny amount of XNT for initial gas fees.

You should now have the Solana CLI configured for X1 development, and your wallet should have enough funds to mint tokens on X1. If you have Linux or WSL and want to go much further, deploying highly advanced programs using Anchor, there is [a great guide on x1.xyz](https://docs.x1.xyz/build-on-x1/create-programs-on-x1). But that is beyond the scope of this tutorial. Note: that X1.xyz guide still references the testnet, even though X1 is now in mainnet. E.g., The official testnet faucet is not necessarily still working. Xen_artist has a [community testnet faucet](https://faucet.x1.wiki/).

## Burnt Liquidity and Airdrops

If you want to launch tokens with no custom behavior, then you can more easily launch them on [XDEX](https://app.xdex.xyz/swap) in the "Mint token" section, although launching such tokens via CLI is possible as an exercise. Regardless of how you launched your token, you can add liquidity in the "Liquidity" section of XDEX. Adding liquidity gives you LP tokens. If you want to "burn" some or all of your LP tokens to increase users' trust in your token, then send the LP tokens to the incinerator address: `1nc1nerator11111111111111111111111111111111`

_Disclaimer: Burning tokens is irreversible._ Please carefully examine LP tokens before sending them to the incinerator, and keep in mind that liquidity (your funds deposited in the pool) cannot be withdrawn once the associated LP tokens are burned. If you want the option of withdrawing some liquidity later, don't burn all the LP tokens.

The game theory for why you would burn liquidity: it is a credible onchain signal that you can't withdraw all liquidity in a "rug pull". If an extractor withdraws all liquidity, then it can cause the token to become instantly worthless. This is why many users prefer burned liquidity.

There is a very simple airdrop script folder into this repo. It allows the top 20 holders of a token to be captured via a snapshot, and experimentally allows minting of the token using scripts, to execute an airdrop. It requires Python to be installed in order to use the scripts.

Future simple guides could feature various Token-2022 Extensions. These extensions are very powerful, and they allow beginner devs to very quickly create tokens with features such as interest rates, soulbound (non-transferable) properties, transfer fees, and so on!

If you are interested in learning to launch tokens with these moderately sophisticated behaviors, then _stay tuned_.

_Disclaimer: All scripts are under development and have not been thoroughly tested. Some are even experimental. Please use them with caution._

License: This code and guide is in the public domain. However, the Platinum Ecosystem's branding materials and name are not in the public domain. The software is provided "as-is", without any warranty or liability, to the maximum extent permitted by law.
