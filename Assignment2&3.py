#!/usr/bin/env python
# coding: utf-8

# In[185]:


import numpy as np
import time


# In[186]:


# Task 1: Creating Arrays


# In[187]:


# 1.
# Write a Python program to:

# A. Create a 1D NumPy array of 10 integers ranging from 1 to 10.

# B. Create a 2D NumPy array of shape (3, 3) with integers from 1 to 9.

# C. Create a 3D NumPy array with random floating-point numbers of shape (3, 5, 3).


# In[188]:


n1=np.arange(1,11)
n1


# In[189]:


n2=np.arange(1,10).reshape(3,3)
n2


# In[190]:


n3=np.random.rand(3,5,3)
n3


# In[191]:


# 2.
# Display the shape, size, and datatype of each array.


# In[192]:


#First Array


# In[193]:


shape=n1.shape
datatype=n1.dtype
size=n1.size
print("Shape = ",shape)
print("Size = ",size)
print("Datatype = ",datatype)


# In[194]:


#Second Array


# In[195]:


shape=n2.shape
datatype=n2.dtype
size=n2.size
print("Shape = ",shape)
print("Size = ",size)
print("Datatype = ",datatype)


# In[196]:


#Third Array


# In[197]:


shape=n3.shape
datatype=n3.dtype
size=n3.size
print("Shape = ",shape)
print("Size = ",size)
print("Datatype = ",datatype)


# In[198]:


# Task 2: Array Indexing and Slicing


# In[199]:


# 1.
# Create a NumPy array from the following list:
# data = [10, 20, 30, 40, 50, 60, 70, 80, 90]


# In[200]:


data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
n1=np.array(data)
n1


# In[201]:


# 2.
# Write a Python program to:

# A. Retrieve the first three elements of the array.

# B. Retrieve every alternate element of the array.

# C. Reverse the array.


# In[202]:


arr1=n1[0:3] #first 3 elements
arr2=n1[0::2]#alternate elements
arr3=n1[::-1]#reverse the array


# In[203]:


# 3.
# Display the results.


# In[204]:


print("First 3 elements are:")
for i in arr1:
    print(i,end=" ")
print("\n")
print("Alternative elements are:")
for i in arr2:
    print(i,end=" ")
print("\n")
print("Reversed array is:")
for i in arr3:
    print(i,end=" ")
print()


# In[205]:


# Task 3: Mathematical Operations


# In[206]:


# 1.
# Create two NumPy arrays, A and B, each with 5 random integers between 1 and 20.


# In[207]:


a=np.random.randint(1,21,size=(5,))
b=np.random.randint(1,21,size=(5,))
print("Array A: ")
print(a, "\n")

print("Array B: ")
print(b)


# In[208]:


# 2.
# Write a Python program to:

# A. Add, subtract, multiply, and divide the two arrays element-wise.

# B. Compute the dot product of the arrays.

# C. Find the mean, median, standard deviation, and variance of array A.

# D. Identify the maximum and minimum values in array B and their indices.


# In[209]:


add,sub,div,mult=a+b,a-b,a/b,a*b
dot_prod=np.dot(a,b)
maxv=np.max(b)
maxin=np.argmax(b)
minv=np.min(b)
minin=np.argmax(b)
mean,median,variance=np.mean(a),np.median(a),np.var(a)
print(" A. Arithmetic Operations: ")
print("Addititon: ",add)
print("Subtraction: ",sub)
print("Division: ",div)
print("Multiplication: ",mult)
print()

print("B. Dot product: ", dot_prod)
print()

print("C. Aggregate Results: ")
print("Mean: ",mean)
print("Median: ",median)
print("Variance: ",variance)
print()

print("D. Min and Max Values: ")
print("Maximum value is: ",maxv," at index: ",maxin)
print("Minimum value is: ",minv," at index: ",minin)


# In[210]:


# Task 4: Reshaping and Transposing


# In[211]:


# 1.
# Create a 1D NumPy array of 12 integers ranging from 1 to 12.


# In[212]:


arr=np.arange(1,13)
print(arr)


# In[213]:


# 2.
# Write a Python program to:

# A. Reshape the array into a 2D array of shape (4, 3).

# B. Reshape the array into a 3D array of shape (2, 2, 3).

# C. Transpose the reshaped 2D array and display its shape.


# In[214]:


arr2=arr.reshape(4,3)
print("A. Reshaped Array (size=(4,3)")
print(arr2, "\n")

arr3=arr.reshape(2,2,3)
print("B. Reshaped Array (size=(2,2,3)")
print(arr3, "\n")

arr4=arr2.T #transpose the array
print("C. Transposed Array:")
print(arr4, "\n")

print("Shape of transposed 2D array is:",arr4.shape)


# In[215]:


# Task 5: Boolean Masking and Filtering


# In[216]:


# 1.
# Create a NumPy array with 15 random integers between 10 and 50.


# In[217]:


arr=np.random.randint(10,51,size=(15,))
print(arr)


# In[218]:


# 2.
# Write a Python program to:

# A. Find all elements greater than 25.

# B. Replace all elements less than 30 with 0.

# C. CouNt the number of elements divisible by 5.


# In[219]:


arr1=arr[arr>25]
print("A. Elements greater than 25 are: ")
for i in arr1:
    print(i,end=" ")
print("\n")
print("B. Array after replacing elements less than 30 with 0: ")
arr[arr<30]=0
print(arr,"\n")


divisible5=arr[arr%5==0].size
print("C. No. of elements divisible by 5 are:",divisible5)


# In[220]:


# Task 6: Working with Built-in Functions


# In[221]:


# 1.
# Use NumPy's built-in functions to:

# A. Create an array of 10 equally spaced values between 0 and 1.

# B. Create an identity matrix of size 4x4.

# C. Generate a 1D array of 20 random integers between 1 and 100, sort it, and find the 5 largest elements.


# In[222]:


print("A.")
arr=np.random.rand(10)
arr


# In[223]:


print("B.")
identity4=np.eye(4)
identity4


# In[224]:


print("C")
arr=np.random.randint(1,101,size=(20,))
print("Array: ")
print(arr)
      
arr.sort()
print("Sorted Array:")
print(arr)
print("5th Largest Element is:",arr[4])


# In[225]:


# Task 7: Generic


# In[226]:


# Create a Python program that:

# A.Generates two large random arrays of size (100, 100).

# B. Performs matrix multiplication on the two arrays.

# C. Finds the determinant and inverse of the resulting matrix (if possible).

# D. Measures the time taken to complete these operations.


# In[227]:


start=time.time()
print("A.")
arr1=np.random.rand(100,100)
arr2=np.random.rand(100,100)
print("Array 1: ")
print(arr1)
print("Array2:")
print(arr2,"\n")

print("B. Matrix multiplication of the two matrices:")
prod=np.dot(arr1,arr2)
print(prod,"\n")

print("C. Determinant and Inverse:")
det=np.linalg.det(prod)
print("Determinant: ")
print(det,"\n")
if(det!=0):
    print("Inverse: ")
    inv=np.linalg.inv(prod)
    print(inv,"\n")
else: print("Inverse does not exist \n")
end=time.time()
total=end-start
print(f'D. Time taken: {total:.3f}')


# In[ ]:





# In[ ]:




