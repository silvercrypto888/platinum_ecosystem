# Snapshot Tool for Multiple Tokens

The `multi_allocation.py` script can calculate a snapshot and allocation across holders of many tokens. As an applied example, it can allocate equal amounts of tokens to: anyone who is a top 20 holder of either Platinum or X1 Xen, or both. However, it does this without giving extra tokens to anyone who is a top 20 holder of both tokens.

This script does multiple things in sequence:

1. Gets the 20 holders for each token.
2. Calculates an intermediate allocation for top 20 holders in each individual community. Each intermediate allocation is for the top 20 holders of each community, based solely on their holdings in that particular community.
3. Calculates each holder's combined final allocation based on their intermediate allocations across many communities (with the methods: sum or max), to generate a final combined allocation for many holders across all those communities.
4. (optional) If enabled, it can rescale the final combined allocations to meet a strict limit for total amount.

The script will use a folder (like `multi_allocation` by default) as a workspace. Here, it will save the top 20 holders list and allocations list for each community, as well as the final combined allocation, using csv files.

## Config

Config options for `multi_allocation.py` (which is in the parent folder) are given by editing the following variables, where order in almost all lists should maintain a consistent ordering across tokens (e.g., Platinum is ordered 1st in all lists, Xen on X1 is ordered 2nd in all lists, etc.). The only exception is `excluded_addresses`, where order doesn't matter, and which doesn't need to be the same length as the number of communities. The config variables will be automatically backed up.

### Workspace config variables:

`data_folder`: name of workspace folder

`read_config_from_file`: True/False. By default (False), it will use config variables provided in ``multi_allocation.py``

`config_filename`: Filename for saving and loading config options from a file

### Calculation config variables:

`num_communities`: number of communities to take snapshots of

`mint_addresses`: list of mint addresses for tokens to take snapshots of

`token_names`: A list of token names. This can be informal (`['plat','xen']`) and is only used for internal reference

`combined_allocations_filename`: filename for final list of combined allocations output

`base_allocation_per_community`: Base amount of tokens to allocate to each community

`community_multipliers`: list of multipliers to apply to each community. The community's token allocation is the base allocation multiplied by its multiplier.

`within_community_allocation`: "equal" for allocating each community's tokens equally across its top 20 members, or "proportional" for allocating the community's tokens across its users in proportion to holdings

`combine_allocations_method`: Method for combining users' allocations based on their holding across communities. "max" gives each user _only the maximum allocation_ among their intermediate allocations in all their holdings across communities, or "sum" for _adding up_ all their allocations across all communities

`rounding_decimals`: Number of decimal places to round token amounts for the final combined allocations

`excluded_addresses`: List of addresses which will be excluded from all allocations. In this applied example, the incinerator and LP addresses are excluded

`rescale_final_allocations`: True/False. False by default. If True, it rescales the final allocations to meet a strict limit in `final_allocation_limit`

`final_allocation_limit`: The targeted limit for the rescaled total allocations (summed across all holders in all communities). Only applicable if `rescale_final_allocations = True`

The main output is the final combined allocations csv file, which is `COMBINED_allocations.csv` in this applied example. This can be used for the airdrop tool in the parent folder, with appropriate configuration.

There are also intermediate outputs of top 20 holder lists for each token, `top20_<token_name>.csv`, and intermediate allocations for each community, `allocations_partial_<token_name>.csv`.

## Possible Allocation Combination Methods

There are four different allocation combinations of the different options for `within_community_allocation` and `combine_allocations_method`:

1. `within_community_allocation = "equal"`, `combine_allocations_method = "max"`: This allocates tokens equally across top 20 holders in each community, and the allocations are combined for each user to only consider their maximum allocation across all communities. This effectively rewards people who are top 20 holders in one or more communities, but with no extra rewards for being a top 20 holder in multiple communities.

2. `within_community_allocation = "equal"`, `combine_allocations_method = "sum"`: This allocates tokens equally across top 20 holders in each community, and the allocations are combined for each user to sum their allocations for all communities. This effectively means that if a user is a top 20 holder in many communities, they could get additional allocations for their role in each of those communities.
  
3. `within_community_allocation = "proportional"`, `combine_allocations_method = "max"`: This allocates tokens proportionally across top 20 holders in each community, and the allocations are combined for each user to only consider their maximum allocation across all communities. This effectively means that if a user is a very high top-ranked holder in any one community, they could get an especially high allocation. But no extra allocations for their less impressive holdings in other communities (even if top 20).

4. `within_community_allocation = "proportional"`, `combine_allocations_method = "sum"`: This allocates tokens proportionally across top 20 holders in each community, and the allocations are combined for each user to sum their allocations for all communities. This effectively means that if a user is a very high-ranked holder in one community, or if they are high-ranked enough in many different communities (top 20 holder in each), they could get an especially high allocation.

### Notes on Allocation Methods

As an applied example, Combination 1 can allocate equal amounts of tokens to: anyone who is a top 20 holder of either Platinum or X1 Xen, or both. However, it does this without giving extra tokens to anyone who is a top 20 holder of both tokens.

Note that if `combine_allocations_method = "max"`, then the sum over final combined allocations will likely not be equal to the sum of allocations for the communities themselves. This is because individuals' lower qualifying allocations in other communities were effectively disregarded, removing those amounts from the total allocations as well.

Note that if rescaling is enabled (`rescale_final_allocations=True`), then the final combined allocation will be rescaled to meet that strict limit in `final_allocation_limit`. For example, if the previously calculated combined allocation added up to 2 billion, and the script is asked to rescale the total amount to 1 billion, then it will halve everyone's allocations to meet the limit and then use that as the final combined allocation.
