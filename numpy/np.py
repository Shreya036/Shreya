import numpy as np

# ##### Create a NumPy array

# arr1 = np.array([10, 20, 30, 40, 50])
# print("np.array():", arr1)

# #### array of zeros

# zeros = np.zeros((2, 3))
# print("\nnp.zeros():")
# print(zeros)


# #####3. Array of ones

# ones = np.ones((2, 3))
# print("\nnp.ones():")
# print(ones)

#  #### 4. Sequence using arange

# arr2 = np.arange(1, 11)
# print("\nnp.arange():", arr2)

# #####5. Evenly spaced values

# arr3 = np.linspace(0, 10, 5)
# print("\nnp.linspace():", arr3)

# ######6. Random integers

# random = np.random.randint(1, 100, size=5)
# print("\nnp.random.randint():", random)

# #########7. Random decimal values

# random_float = np.random.rand(5)
# print("\nnp.random.rand():", random_float)

# ########## ARRAY OPERATIONS #######

# arr = np.array([10, 20, 30, 40, 50, 60])

# print("\nShape:", arr.shape)
# print("Dimensions:", arr.ndim)
# print("Total Elements:", arr.size)
# print("Data Type:", arr.dtype)

#######Reshape########

# arr2d = arr.reshape(2, 3)
# print("\nReshaped Array:")
# print(arr2d)

# ###Flatten

# flat = arr2d.flatten()
# print("\nFlattened Array:")
# print(flat)

# ####Sort

# unsorted = np.array([50, 10, 40, 20, 30])
# sorted_arr = np.sort(unsorted)
# print("\nSorted Array:", sorted_arr)


    
# ###########MATHEMATICAL  OPERATIONS####

# data = np.array([10, 20, 30, 40, 50])

# print("\nData:", data)
# print("Sum:", np.sum(data))
# print("Mean:", np.mean(data))
# print("Median:", np.median(data))
# print("Minimum:", np.min(data))
# print("Maximum:", np.max(data))
# print("Standard Deviation:", np.std(data))
# print("Variance:", np.var(data))


# arr = np.array([10, 20, 30, 40, 50, 60])
# print("\nShape:", arr.shape)
# a = arr.reshape(2,3,1)
# print(a)
# print("Dimensions:", a.ndim)

# print(np.__version__)

#######identity matrix###########

e=np.eye(4)
print(e)

