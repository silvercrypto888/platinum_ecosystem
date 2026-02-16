import json
import csv
import sys

input_file = "top20_holders.json"
output_file = "top20_holders.csv"

def json_to_csv(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Extract the list of holders (handles Solana RPC 'result' nesting)
    holders = data.get('result', {}).get('value', data) if isinstance(data, dict) else data

    if not holders:
        print("No data found.")
        return

    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=holders[0].keys())
        writer.writeheader()
        writer.writerows(holders)
    print(f"Successfully converted to {output_file}")

json_to_csv(input_file, output_file)

##if __name__ == "__main__":
##    json_to_csv(sys.argv[1], sys.argv[2])
##
