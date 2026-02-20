# Your First Token

This guide will launch a very simple Token-2022 token with no custom logic, using the Solana CLI via batch files.

**Prerequisites:** You must have already installed the Solana CLI, with the RPC and keypair configured appropriately. You must also have some XNT in your address (the one associated with your Solana CLI keypair) to cover gas fees.

# Creating the token

You can create the token by running create_token.bat. It will create the token on X1 and create mint_address.txt, which has your token's _mint address_. By default, it will use a precision of 9 decimal places (which is very common).

The batch file has lots of logging code, but the key command is just this:

`spl-token create-token --program-id TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb --decimals 9 --enable-metadata`

# Setting up Metadata

Metadata will give your token a name, ticker, and image.

## Preliminaries

This part is tedious, but it's very highly recommended. That's because it's needed if you want the token to have an image:

1. Upload the image to IPFS using a service such as [Lighthouse](https://www.lighthouse.storage/) or [Filebase](https://filebase.com/).
2. Find the image uri on IPFS. Keep it for the next step.
3. Create a json file that contains your token metadata, including the IPFS uri for your image inside it.
(An example json file, test_token.json, is given. You can use it as a template.)
4. Upload and pin the json file to IPFS.
5. Copy the IPFS uri for your json file for reference, for the next section.

## Initializing the Metadata

1. Run create_metadata.bat. It will read mint_address.txt (if generated earlier). Then it will ask you for the name, ticker, and metadata URI.
2. You provide these fields by typing (or copy-pasting) them and then pressing "Enter" for each prompt. When prompted, you should enter the metadata URI for the json file that you had earlier pinned to IPFS.

The batch file's key role is to run the command:

`spl-token initialize-metadata %MINT_ADDRESS% "%T_NAME%" "%T_TICKER%" "%T_URI%"`

Where the placeholder variables with `%` symbols will be automatically filled in with the appropriate values.

# What if the metadata initialization got screwed up, or if I wanted to change something later?

Don't worry. Metadata is mutable by default. This means you can always just change it later (assuming you don't go out of your way to revoke your authority).

If you later want to update the metadata (after first initialization) using the create_metadata.bat script, you will first need to edit it as follows:

1. Find the line `spl-token initialize-metadata %MINT_ADDRESS% "%T_NAME%" "%T_TICKER%" "%T_URI%"`
2. Replace with `spl-token update-metadata %MINT_ADDRESS% "%T_NAME%" "%T_TICKER%" "%T_URI%"`
3. Save create_metadata.bat, then run it again and enter the metadata fields again, with updated values.

# What next?

You only created the token, but it currently has a supply of 0, because none of it was issued yet. You may be asking how to issue a larger supply to get this token into the hands of more holders. That is a _very_ good question.

One way to do that is to explore the [snapshot and airdrop tool](../airdrop) in this repo to achieve a wide initial distribution by airdropping the token to the top 20 holders of another existing token whose community you really like. This way, you won't have to create your own community and then distribute the tokens manually from scratch.
