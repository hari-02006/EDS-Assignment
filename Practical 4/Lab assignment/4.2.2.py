
import pandas as pd

# Prompt the user for the file name (Remove extra prompt text)
file_name = input().strip()

# Load the data
df = pd.read_csv(file_name)

# Find the product with the highest total quantity sold
product_sales = df.groupby("Product")["Quantity"].sum()
best_product = product_sales.idxmax()
highest_quantity = product_sales.max()

# Display the result with the correct formatting
print(f"Best selling product: {best_product}")
print(f"Total quantity sold: {highest_quantity}")