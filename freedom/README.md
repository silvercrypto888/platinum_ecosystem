# Soulbound tokens with interest rates

**Prerequisites:** You must have already installed the Solana CLI, with the RPC and keypair configured appropriately. You must also have some XNT in your address (the one associated with your Solana CLI keypair) to cover gas fees.

Running the batch file `create_soulbound_token.bat` will create a soulbound (non-transferable) token with a continuously compounded interest/inflation rate. It will prompt you for the interest rate in basis points. This creates a token like the Platinum Ecosystem's FREEDOM token, which is soulbound with a 17.76% interest rate.

The main command is this one: `spl-token create-token --program-id TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb --decimals %DECIMALS% --interest-rate %INT_RATE%`

After creating the token, you can initialize metadata using the batch files [here](/your_first_token).

## Why soulbound tokens that can't be transferred?


They can be used as "badges" for ecosystem participation, as well as marketing purposes. For example, airdropping them to the top holders of a token is a non-monetary way to recognize those holders and promote the community onchain. It is a clear signal to highlight a past achievement, one that can never be transferred or sold.
