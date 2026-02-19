# Your First Token

This guide will show how to launch a very simple Token-2022 token with no custom behavior, using batch files to operate the Solana CLI.

**Prerequisites:** You must have already installed and set up the Solana CLI, setting your RPC, keypair, and config options appropriately. You must also have some XNT in your address (the one associated with your Solana CLI keypair) to cover gas fees.

# Minting the token

You can mint the token by running create_token.bat. It will create the token on X1 and then generate mint_address.txt, which contains your token's _mint address_. By default, it will use a precision of 9 decimal places (which is very common).

The batch file has a lot of error handling and logging code, but the key command is just this one:

`spl-token create-token --program-id TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb --decimals 9 --enable-metadata`

# Setting up Metadata

This part is more tedious, but it is very highly recommended since it's needed for your token to have a name, ticker, and image. First, if you want it to have an image, you should upload the image to IPFS using a service such as [Lighthouse](https://www.lighthouse.storage/) or [Filebase](https://filebase.com/). Get the image uri on IPFS. Then create a json file that contains your token metadata, including the IPFS uri for your image inside it. Then upload and pin the json file to IPFS. An example json file, test_token.json, is given. You can use it as a template and populate it with your own token's properties. After that, copy the IPFS uri for your json file for reference for the next step.

After you minted the token using create_token.bat, run create_metadata.bat. It will read mint_address.txt and then ask you for the name, ticker, and metadata URI. You provide these by typing (or copy-pasting) them and then pressing "Enter" for each prompt. You should enter the metadata URI for the json file you pinned to IPFS earlier, when prompted. The batch file's key role is to run the command:

`spl-token initialize-metadata %MINT_ADDRESS% "%T_NAME%" "%T_TICKER%" "%T_URI%"`

Where the placeholder variables surrounded by `%` symbols will be filled in with the values you provided.

# What if the metadata initialization got screwed up, or if I wanted to change something later?

Don't worry. Metadata is mutable by default. This means you can always just change it later (assuming you don't go out of your way to revoke that permission). If you later want to update the metadata (after first initialization) using the metadata.bat script, you will first need to edit it as follows:

1. Find the line `spl-token initialize-metadata %MINT_ADDRESS% "%T_NAME%" "%T_TICKER%" "%T_URI%"`
2. Replace with `spl-token update-metadata %MINT_ADDRESS% "%T_NAME%" "%T_TICKER%" "%T_URI%"`
3. Save metadata.bat, then run it again and enter the metadata fields again, with updated values.

# What next?

You only created the token, but it currently has a supply of 0, because none of it was issued yet. You may be asking how to issue a larger supply to get this token into the hands of more holders. That is a _very_ good question.

One way to do that is to explore the [snapshot and airdrop tool](../airdrop) in this repo to achieve a wide initial distribution by airdropping the token to the top 20 holders of another existing token whose community you really like, without having to create your own community and then distribute the tokens manually from scratch.
