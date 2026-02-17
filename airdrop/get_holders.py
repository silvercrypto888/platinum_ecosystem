import requests
import pandas as pd
#import time

mint_address = "ACor5a1JMRsnbMKcibnNZfbY5nfiBg3TwRvWSNUE2DVb"

# Define the endpoint and the payload
url = "https://rpc.mainnet.x1.xyz"
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getTokenLargestAccounts",
    "params": [mint_address]
}

# Make the POST request
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract the relevant data from the RPC response
    # Usually, RPC results are nested inside 'result' -> 'value'
    if 'result' in data and 'value' in data['result']:
        df = pd.DataFrame(data['result']['value'])
        
        print("Data successfully loaded into DataFrame:")
        print(df.head())
    else:
        print("Unexpected JSON structure:", data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


## Getting Waletts from ATAs

url = "https://rpc.mainnet.x1.xyz"

# Assuming 'df' is your DataFrame from the previous step containing the 'address' column (ATAs)
# We will create a list to store our new enriched records
enriched_data = []

print(f"Processing {len(df)} accounts...")

for index, row in df.iterrows():
    ata_address = row['address']
    
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getAccountInfo",
        "params": [
            ata_address,
            {"encoding": "jsonParsed", "commitment": "confirmed"}
        ]
    }
    
    try:
        response = requests.post(url, json=payload)
        res_json = response.json()
        
        # Navigate the nested JSON to find the owner (the actual wallet address)
        # Path: result -> value -> data -> parsed -> info -> owner
        account_data = res_json.get('result', {}).get('value', {}).get('data', {})
        
        if account_data and 'parsed' in account_data:
            wallet_address = account_data['parsed']['info']['owner']
        else:
            wallet_address = "Unknown/Non-Parsed"
            
        # Combine original ATA info with the new Wallet Address
        enriched_data.append({
            "address": wallet_address,
            "ata_address": ata_address,
            "amount": row.get('amount'),
            "uiAmount": row.get('uiAmount'),
            "decimals": row.get('decimals')
        })
        
        # Optional: Small sleep to avoid hitting rate limits on the RPC node
        # time.sleep(0.1) 

    except Exception as e:
        print(f"Error processing {ata_address}: {e}")

# Create the final enriched DataFrame
final_df = pd.DataFrame(enriched_data)

print("\nFinal Dataframe (Wallet Mapping):")
print(final_df.head())

final_df.to_csv('top20wallets.csv', index=False)

print("Exported top20wallets.csv")
