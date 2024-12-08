import numpy as np

# i) Create a NumPy array
array = np.array([10, 20, 30, 40, 50])
print("Created NumPy Array:", array)

# ii) Demonstrate Indexing in NumPy Array
# Accessing single elements
print("\nIndexing in NumPy Array:")
print("Element at index 0:", array[0])
print("Element at index 3:", array[3])

# Accessing a range (slicing)
print("Elements from index 1 to 3:", array[1:4])

# Accessing elements with step
print("Every second element:", array[::-1])

# iii) Perform Basic Operations on a Single Array
print("\nBasic Operations:")
print("Array + 5:", array + 5)           # Add 5 to each element
print("Array * 2:", array * 2)           # Multiply each element by 2
print("Array squared:", array ** 2)      # Square each element
print("Mean of Array:", np.mean(array))  # Calculate the mean
print("Sum of Array:", np.sum(array))    # Sum of all elements
print("Max of Array:", np.max(array))    # Maximum value
