@echo off
SETLOCAL EnableDelayedExpansion

:: Check if the mint_address.txt file exists
if not exist mint_address.txt (
    echo [ERROR] mint_address.txt not found!
    pause
    exit /b
)

:: Read the first line of the file as the Mint Address
set /p MINT_ADDRESS=<mint_address.txt
echo [INFO] Found Mint Address: %MINT_ADDRESS%

:: Prompt user for input
set /p T_NAME="Enter Token Name: "
set /p T_TICKER="Enter Token Ticker: "
set /p T_URI="Enter Metadata URI (JSON link): "

echo.
echo ------------------------------------------
echo Updating Metadata for: %MINT_ADDRESS%
echo Name: %T_NAME%
echo Ticker: %T_TICKER%
echo URI: %T_URI%
echo ------------------------------------------
echo.

:: Execute the SPL Token CLI command
:: Note: This uses 'initialize-metadata' for the first-time setup.
:: If metadata already exists, use 'update-metadata' instead.
spl-token initialize-metadata %MINT_ADDRESS% "%T_NAME%" "%T_TICKER%" "%T_URI%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo [SUCCESS] Metadata initialized successfully!
) else (
    echo.
    echo [ERROR] Failed to update metadata. Ensure you have SOL for rent and are the update authority.
)
ENDLOCAL
pause