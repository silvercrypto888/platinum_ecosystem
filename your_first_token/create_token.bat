@echo off
SETLOCAL EnableDelayedExpansion
SET logfile=token_creation_log.txt
SET mintfile=mint_address.txt

spl-token create-token --program-id TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb --decimals 9 --enable-metadata  > %logfile% 2>&1

FOR /F "tokens=2" %%i IN ('findstr "Address:" %logfile%') DO (
    SET MINT_ADDRESS=%%i
)

IF DEFINED MINT_ADDRESS (
    echo.
    echo New Token-2022 Mint Address: !MINT_ADDRESS!
    echo !MINT_ADDRESS! > !mintfile!
    echo Mint address saved to !mintfile!
) ELSE (
    echo.
    echo Failed to create token or find the address. Check !logfile! for details.
)
ENDLOCAL
pause