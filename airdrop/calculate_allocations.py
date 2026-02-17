import pandas as pd
import argparse

def calculate_airdrop(
    input_csv: str, 
    output_csv: str, 
    total_supply: float, 
    distribution_type: str, 
    exclude_addresses: list
):
    """
    Calculate airdrop allocations.
    
    :param input_csv: Path to the input CSV file containing holders.
    :param output_csv: Path to save the resulting allocations CSV.
    :param total_supply: Total amount of tokens to distribute.
    :param distribution_type: 'proportional' or 'equal'.
    :param exclude_addresses: List of addresses to exclude from the airdrop.
    """
    print(f"Loading data from {input_csv}...")
    try:
        df = pd.read_csv(input_csv)
    except FileNotFoundError:
        print(f"Error: The file {input_csv} was not found.")
        return

    # Check if 'address' column exists
    if 'address' not in df.columns:
        print("Error: Input CSV must contain an 'address' column.")
        return

    initial_count = len(df)
    
    # Exclude addresses
    if exclude_addresses:
        df = df[~df['address'].isin(exclude_addresses)].copy()
        print(f"Excluded {initial_count - len(df)} addresses.")
        
    if len(df) == 0:
        print("Error: No addresses left after applying exclusions.")
        return

    print(f"Calculating {distribution_type} allocation for {len(df)} addresses...")

    if distribution_type == 'equal':
        # Calculate equal distribution
        allocation_per_address = total_supply / len(df)
        df['amount'] = allocation_per_address

    elif distribution_type == 'proportional':
        # We assume 'uiAmount' or 'amount' is used for proportional math
        # It defaults to 'uiAmount' if available (which is standard for Solana exports), 
        # otherwise falls back to 'amount'
        balance_col = 'uiAmount' if 'uiAmount' in df.columns else 'amount'
        
        if balance_col not in df.columns:
            print("Error: Input CSV must contain 'uiAmount' or 'amount' column for proportional calculation.")
            return
            
        total_holdings = df[balance_col].sum()
        
        if total_holdings == 0:
            print("Error: Total holdings sum to 0. Cannot perform proportional calculation.")
            return
            
        df['amount'] = (df[balance_col] / total_holdings) * total_supply

    else:
        print("Error: distribution_type must be either 'proportional' or 'equal'.")
        return

    # Keep only the required columns: 'address' and 'amount'
    output_df = df[['address', 'amount']]

    # Export to CSV
    output_df.to_csv(output_csv, index=False)
    print(f"Success! Exported {len(output_df)} allocations to {output_csv}.")


if __name__ == "__main__":
    # =========================================================================
    # CONFIGURATION
    # You can edit these variables directly or pass them via command line later
    # =========================================================================
    INPUT_FILE = "top20_holders.csv"
    OUTPUT_FILE = "allocations.csv"
    
    # Total tokens to give away in this airdrop
    TOTAL_AIRDROP_SUPPLY = 1_000_000_000
    
    # Set to 'proportional' or 'equal'
    DISTRIBUTION_TYPE = "proportional"  
    
    # Add any addresses you want to exclude to this list (e.g., team wallets, LPs)
    EXCLUDED_ADDRESSES = [
        # "3bQvcXYPiD7AUFHsidJzmKJo2U4RX81mrTveuXBunhQ9",
        # "2SP5VzXU86JMr3oZXxwakzBHP5ZDf9T3LNaAZbctjiG9"
    ]
    # =========================================================================

    calculate_airdrop(
        input_csv=INPUT_FILE,
        output_csv=OUTPUT_FILE,
        total_supply=TOTAL_AIRDROP_SUPPLY,
        distribution_type=DISTRIBUTION_TYPE,
        exclude_addresses=EXCLUDED_ADDRESSES
    )
