import numpy as np
import numpy as np

# Read the dimensions of the array
rows, cols = map(int, input().split())

# Read the elements of the array
elements = []
for _ in range(rows):
    elements.extend(map(int, input().split()))

# Create the NumPy array and reshape it
array = np.array(elements).reshape(rows, cols)

# Display the array
print(array)

# Display ndim, shape, and size
print(array.ndim)
print(array.shape)
print(array.size)





