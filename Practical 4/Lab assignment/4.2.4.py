
import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# Group products by date
grouped = df.groupby('Date')['Product'].apply(list)

# Initialize counter for product pairs
pair_counter = Counter()

# Count each pair in the product list for a given date
for products in grouped:
    # Only count if there are 2 or more products
    for pair in combinations(sorted(set(products)), 2):
        pair_counter[pair] += 1

# Find the highest frequency
if pair_counter:
    max_count = max(pair_counter.values())

    # Find all pairs with the highest frequency
    most_frequent_pairs = [pair for pair, count in pair_counter.items() if count == max_count]

    # Output results
    for pair in most_frequent_pairs:
        print(f"{pair[0]} and {pair[1]}: {max_count} times")
else:
    print("No product pairs found.")

