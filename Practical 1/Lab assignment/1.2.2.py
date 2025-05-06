# Recursive function to calculate Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Main function to take input and display Fibonacci series
def main():
    # Input for number of terms
    terms = int(input("Enter terms for Fibonacci series: "))
    
    # Generating Fibonacci series
    for i in range(terms):
        print(fibonacci(i), end=" ")

# Run the program
if __name__ == "__main__":
    main()


    
    
    
    
    
    
    
    
    

'''n=int(input("Enter terms for Fibonacci series: "))
for i in range (n):
      print(fib(i),end=" ")'''