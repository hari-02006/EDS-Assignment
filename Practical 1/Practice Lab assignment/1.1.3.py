
from datetime import datetime

def calculate_age(birthdate):
    # Convert the string date to a datetime object
    birth_date = datetime.strptime(birthdate, "%d-%m-%Y")
    # Get the current date
    today = datetime.today()
    # Calculate the age
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def convert_salary_to_dollars(salary_in_rupees):
    return salary_in_rupees * 0.012  # Conversion rate 1 INR = 0.012 USD

# Read input
birthdate = input().strip()
salary_in_rupees = float(input().strip())

# Compute age and salary in dollars
age = calculate_age(birthdate)
salary_in_dollars = convert_salary_to_dollars(salary_in_rupees)

# Display results
print(f"Age: {age}")
print(f"Salary in dollars: {salary_in_dollars:.2f}")
