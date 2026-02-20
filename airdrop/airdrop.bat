@echo off
SETLOCAL EnableDelayedExpansion
set RPC_URL="https://rpc.mainnet.x1.xyz"
set MINT_ADDRESS="<insert mint address here>"
set PAYER_KEYPAIR=" <insert keypair file path here>"
SET "INPUT_FILE= <Insert csv file path here>"

solana config set %PAYER_KEYPAIR%

echo Starting token minting...

FOR /F "usebackq tokens=1,2 delims=," %%A IN (!INPUT_FILE!) DO (
    SET WALLET_ADDRESS=%%A
    SET AMOUNT=%%B
    
    REM Check if the line is a header and skip
    IF "%%A" == "address" (
        echo Skipping header row...
    ) ELSE (
        echo Try to mint !AMOUNT! tokens to !WALLET_ADDRESS!...
        
        REM Command to create Associated Token Account (ATA) if it doesn't exist
        REM This command handles creation or just gets the address if it exists
        FOR /F "tokens=3 delims= " %%C IN ('spl-token create-account --owner %%A !MINT_ADDRESS! --fee-payer !PAYER_KEYPAIR!') DO SET ATA_ADDRESS=%%C

        echo ATA address is !ATA_ADDRESS!

        REM Command to mint tokens to the Associated Token Account
        spl-token mint !MINT_ADDRESS! !AMOUNT! !ATA_ADDRESS!
        
        echo Ended mint to !WALLET_ADDRESS!.
    )
)

echo Token minting complete.
ENDLOCAL
pause