import pandas as pd
import pickle

from calculate_allocations import calculate_airdrop
from get_holders import get_holders

### Config options and saving/loading config as file

data_folder = "multi_allocation/"
read_config_from_file=False
config_filename = "config.pkl"

if(read_config_from_file == False):
    
    num_communities=2
    mint_addresses=[
        "ACor5a1JMRsnbMKcibnNZfbY5nfiBg3TwRvWSNUE2DVb",
        "y1KEaaWVoEfX2gH7X1Vougmc9yD1Bi2c9VHeD7bDnNC"
                  ]
    token_names = ["plat", "xen"]
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
    rescale_final_allocations=False
    final_allocation_limit = 1_000_000_000
else:
    with open(data_folder+config_filename, 'rb') as f:
        loaded_data = pickle.load(f)
        globals().update(loaded_data)


## Backup config options to file for reference

# List of variable names you want to save
to_save = ['data_folder', 'read_config_from_file', 'config_filename','num_communities',
           'mint_addresses','token_names','combined_allocations_filename',
           'base_allocation_per_community','community_multipliers','within_community_allocation',
           'combine_allocations_method','rounding_decimals','excluded_addresses',
           'rescale_final_allocations', 'final_allocation_limit'] 

# Create a dictionary using their names as keys
data_to_serialize = {name: globals()[name] for name in to_save if name in globals()}

with open(data_folder+config_filename, 'wb') as f:
    pickle.dump(data_to_serialize, f)

print("Backed up config options in "+ data_folder+config_filename)


### Now do the actual snapshot

##  calculates allocations by community
allocations_by_community = [base_allocation_per_community * weight for weight in community_multipliers]

## edits filenames to store the files in the data subfolder
holders_filenames = [data_folder + "top20_"+ name + ".csv" for name in token_names]
allocations_filenames = [data_folder + "allocations_partial_"+ name + ".csv" for name in token_names]
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
    


#Rescale allocations to match a limit (if enabled)

if(rescale_final_allocations == True):
    combined_allocations['amount'] = combined_allocations['amount'] * (final_allocation_limit / combined_allocations['amount'].sum())

combined_allocations['amount'] = combined_allocations['amount'].round(rounding_decimals)
combined_allocations.to_csv(combined_allocations_filename, index=False)

print("Success! the final combined allocations were saved in " + combined_allocations_filename)


