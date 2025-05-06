
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract the month in YYYY-MM format
df['Month'] = df['Date'].dt.to_period('M').astype(str)

# Calculate total sales per row (Quantity * Price)
df['Sales'] = df['Quantity'] * df['Price']

# Group by month and calculate total sales
monthly_sales = df.groupby('Month')['Sales'].sum()

# Find the month with the highest total sales
best_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()

# Print the results
print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")

