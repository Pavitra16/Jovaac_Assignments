#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import csv


# In[24]:


# Task1: Make a custom exception


# In[25]:


class ValidateAge(Exception):
    def __init__(self, age):
        self.age=age
        super().__init__(f"Invalid Age")

def voting_right(age):
    if age<0:
        raise ValidateAge(age)
    elif age<18: return "Not allowed to Vote"
    else: return "Allowed to Vote"

num=int(input("Enter age:"))
try:
    print(voting_right(num))
except ValidateAge as e:
    print("Error:", e)


# In[26]:


# Task2: Make a 2-d array and read and write it in a csv format


# In[27]:


#Create Array


# In[28]:


arr1=np.random.randint(1,100,size=(3,3))
arr1


# In[29]:


#Write Array to the CSV file


# In[30]:


with open("Array.csv","w",newline="") as file:
    write=csv.writer(file)
    for row in arr1:
        write.writerow(row)
        


# In[31]:


#Read the CSV file


# In[32]:


with open("Array.csv") as file:
    read=csv.reader(file)
    for row in read:
        print(row)


# In[ ]:




