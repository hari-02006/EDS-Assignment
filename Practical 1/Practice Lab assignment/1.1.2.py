import math
num = int(input())
if 1 <= num <= 9: 
    print(num ** 2)
elif 10 <= num <= 99: 
    print(f"{math.sqrt(num):.2f}")
elif 100 <= num <= 999: 
    print(f"{math.cbrt(num):.2f}")
else:
    print("Invalid")

