
import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']

# 1. Create a new column ‘IsAlone' (1 if alone, 0 otherwise)
def familysize(size):
	if size == 0:
		return 1
	else:
		return 0
data['IsAlone'] = data['FamilySize'].apply(familysize)


# 2. Convert ‘Sex' to numeric (male: 0, female: 1)
def gender(sex):
	if sex == 'male':
		return 0
	else:
		return 1
data['Sex'] = data['Sex'].apply(gender)


# 3. One-hot encode the ‘Embarked' column


# 4. Get the mean age of passengers
mean_val = data['Age'].mean()
print(mean_val)


# 5. Get the median fare of passengers
median_val = data['Fare'].median()
print(median_val)


# 6. Get the number of passengers by class
print(data['Pclass'].value_counts())

# 7. Get the number of passengers by gender
print(data['Sex'].value_counts())

# 8. Get the number of passengers by survival status
print(data['Survived'].value_counts())

# 9. Calculate the survival rate
total = data['Survived'].value_counts().sum()
survived = data['Survived'].sum()
rate = (survived/total)
print(rate)

# 10. Calculate the survival rate by gender
grouped = data.groupby('Sex')['Survived'].mean()
print(grouped)



