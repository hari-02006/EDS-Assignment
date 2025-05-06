# Function to perform linear search
def linear_search(arr, key):
    # Traverse the array
    for i in range(len(arr)):
        if arr[i] == key:
            return i  # Return the index if the element is found
    return -1  # Return -1 if the element is not found

# Input reading
arr = list(map(int, input().split()))  # Read the array of integers
key = int(input())  # Read the key to be searched

# Perform the linear search
index = linear_search(arr, key)

# Output the result
if index != -1:
    print(index)  # If found, print the index
else:
    print("Not found")  # If not found, print "Not found"

