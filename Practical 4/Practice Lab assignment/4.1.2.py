
import pandas as pd

# Provided dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Adding a new row
name=input("New name: ")
age=int(input("New age: "))
Data={
	'Name':[name],
	'Age': [age]
}
D=pd.DataFrame(Data)
df=pd.concat([df,D],ignore_index=True)


# Display the DataFrame after adding a new row
print("After adding a row:\n",df)

# Modifying a row
a=int(input("Index of row to modify: "))
A=int(input("New age: "))
df.at[a,'Age']=A


# Display the DataFrame after modifying a row
print("After modifying a row:")
print(df)

# Deleting a row
n=int(input("Index of row to delete: "))
df=df.drop(index=n).reset_index(drop=True)


# Display the DataFrame after deleting a row
print("After deleting a row:")
print(df)

# Adding a new column
l=input("Enter genders separated by space: ").split()
D1={
	'Gender': l
}
df['Gender']=l


# Display the DataFrame after adding a new column
print("After adding a new column:")
print(df)

# Modifying a column
df['Name']=df['Name'].str.upper()


# Display the DataFrame after modifying a column
print("After modifying a column:")
print(df)

# Deleting a column
df=df.drop(['Age'],axis=1)


# Display the DataFrame after deleting a column
print("After deleting a column:")
print(df)

