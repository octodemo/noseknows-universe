import pandas as pd
import random

# Load the perfume data
perfume_df = pd.read_csv('data/final_perfume_data.csv', encoding='unicode_escape')

# Randomly select 20 perfume names
sampled_perfumes = perfume_df['Name'].sample(n=20, random_state=1)

# Save the sampled perfume names to a new CSV file
sampled_perfumes.to_csv('data/sample_perfumes.csv', index=False, header=['Name'])

print("Sampled perfumes saved to data/sample_perfumes.csv")