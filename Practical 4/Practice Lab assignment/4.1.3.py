import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])
print("First five rows:")
print(data.head())
avg=round(data['Age'].mean(),2)
print("Average age:",avg)
print("Students with a grade up to B")
print(data[data['Grade'].str.strip().str.upper()<='B'])
1