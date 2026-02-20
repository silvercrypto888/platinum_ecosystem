import pandas as pd
from calculate_allocations import calculate_airdrop
from get_holders import get_holders

## Config options

num_communities=2

mint_addresses=[
    "ACor5a1JMRsnbMKcibnNZfbY5nfiBg3TwRvWSNUE2DVb",
    "y1KEaaWVoEfX2gH7X1Vougmc9yD1Bi2c9VHeD7bDnNC"
              ]

data_folder = "multi_allocation/"
holders_filenames = ["top20_plat.csv","top20_xen.csv"]
allocations_filenames = ["plat_allocations.csv", "xen_allocations.csv"]
combined_allocations_filename = "COMBINED_allocations.csv"

base_allocation_per_community = 16_000_000_000
community_multipliers = [1,1]

within_community_allocation = "equal"
combine_allocations_method="max"

rounding_decimals = 3

excluded_addresses = [
    "9Dpjw2pB5kXJr6ZTHiqzEMfJPic3om9jgNacnwpLCoaU",
    "1nc1nerator11111111111111111111111111111111",
    ]




##  calculates allocations by community
allocations_by_community = [base_allocation_per_community * weight for weight in community_multipliers]

## edits filenames to store the files in the data subfolder
holders_filenames = [data_folder + file for file in holders_filenames]
allocations_filenames = [data_folder + file for file in allocations_filenames]
combined_allocations_filename = data_folder + combined_allocations_filename


for i in range(num_communities):
    get_holders(mint_addresses[i],holders_filenames[i])
    calculate_airdrop(holders_filenames[i],allocations_filenames[i],allocations_by_community[i],within_community_allocation,excluded_addresses)

# Read them all into a list of DataFrames
df_list = [pd.read_csv(f) for f in allocations_filenames]

# Stack them vertically (one on top of the other)
all_allocations = pd.concat(df_list, axis=0, ignore_index=True)

if(combine_allocations_method=="max"):
    # Finds the single highest allocation for each address
    combined_allocations = all_allocations.groupby('address')['amount'].max().reset_index()

elif(combine_allocations_method=="sum"):
    # Finds the sum of allocations for each address
    combined_allocations = all_allocations.groupby('address')['amount'].sum().reset_index()
    
else:
    raise Exception("Error: combine_allocations_method must be either 'max' or 'sum'.")
    
combined_allocations['amount'] = combined_allocations['amount'].round(rounding_decimals)
combined_allocations.to_csv(combined_allocations_filename, index=False)

print("Success! the combined airdrops were saved in " + combined_allocations_filename)
