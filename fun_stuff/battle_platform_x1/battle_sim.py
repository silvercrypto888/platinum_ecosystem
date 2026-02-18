def battle_simulator(num_fighters, quality, boss_score=1_000_000_000_000_000):
    """
    Simulates a battle based on Lanchester's Square Law / Metcalfe's Law.
    Power = (Quantity^2) * Quality
    """
    
    # Calculate fighter power: (N^2) * Q
    fighter_power = (num_fighters ** 2) * quality
    
    # Determine win/loss
    is_victory = fighter_power > boss_score

    message = f"The size of the X1 Network community is {num_fighters:,}.\nEach person's quality is {quality:,}.\n"
    message += f"The X1 community is fighting against HYPERINFLATION!\nHe has a score of {boss_score:,}!\n"
    message += f"The Warriors (Validators) are burning XNT.\nThe Rogues (Xenians) are burning Xen.\nThe Mages (Alchemists) are burning Platinum.\n"
    message += f"The community's quadratic Metcalfe-Lanchester power level:\n{fighter_power:,}.\n"
    # Generate the status message
    if is_victory:
        message += f"Victory! The fighters amassed {fighter_power:,} power.\nThey slammed HYPERINFLATION.\nX1 has saved the entire world, with help from the Alchemists."
    else:
        message += f"Defeat! The HYPERINFLATION remains standing.\nFighters only reached {fighter_power:,} power.\nBillions of people are living in a daily clown show."
        
    return is_victory, message

# Example usage:
# Let's try 30 million fighters with a quality of 8.88888888
win, result_text = battle_simulator(15_000_000, 8.88888888)
print(result_text)
