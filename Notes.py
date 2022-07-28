#!/usr/bin/env python
# coding: utf-8

# # An Array is a data structure consisting of a collection of elements each identified by at least one array  index

# # Properties

# Array cann store data of specific type  ex:- int,char double etc.
# 
# Elements of an array are located in a contigious ex:- |2|3|3|5| no gap b/w elemnts
# 
# Each elements of array has unique index ex:- a[0],a[1],...
# 
# Size of array is predefined not modified ex:- |_3_|_4_|_5_|_1_|  size= 4

# # Creating an array

# Array in Python can be Impliment using array module
# 
# Type/Unicode  :-    Signed char='b' 
#                          Float = 'f' 
#                                Integer = 'i'

# In[11]:


from array import *
array1=array('i',[3,5,1,6,9])
print(array1)


# # Inserting element in an Array

# In[14]:


from array import *
a1=array('i',[2,3,4,5,6])
print(a1)
a1.insert(0,1)             # At Beginning
print(a1)
a1.insert(6,7)             # At End
print(a1)
a1.insert(3,9)             # At Anywhere
print(a1)


# # Array Traversal

# In[17]:


from array import *
a1=array('i',[2,3,4,1,7])
def trans(a1):
    for i in a1:
        print(i)
trans(a1)


# In[18]:


from array import *
a1=array('i',[2,3,4,1,7])
for i in a1:
    print(i)


# # Acccess Element of an Array

# In[25]:


from array import *
a1=array('i',[3,4,5,6,7])
def accessElement(array,index):
    if index>=len(a1):
        print("The element is not exist")
    else:
        print(a1[index])
accessElement(a1,3)
accessElement(a1,8)


# In[27]:


from array import *
a1=array('i',[3,4,5,6,7])
index=int(input())
if index>=len(a1):
    print("The element is not exist")
else:
    print(a1[index])


# # Searching Element in an Array --Liner Search

# In[40]:


from array import *
a1=array('i',[4,5,2,8,1])
def search(array,target):
    for i in array:
        if i==target:
            return array.index(target)
    return "The Element is not present in Array"
print(search(a1,5))
print(search(a1,9))


# In[60]:


from array import *
a1=array('i',[4,5,2,8,1])
target=int(input())
for i in a1:
    if i!=target:
        pass
    else:
        print(a1.index(target))
        break


# # Deletion of Element from an array

# In[67]:


from array import *
a1=array('i',[4,5,2,8,1])
a1.remove(5)
print(a1)


# In[101]:


# from array import *

#create an array and transverse it

array1=array('i',[1,2,3,4,5])
for i in array1:
    print(i)
print()
    
#Access individual element through it index
print(array1[2])
print()

#Append an element to an array using append() method

array1.append(6)
print(array1)
print()

#Insert any value in an array using insert() method

array1.insert(7,7)
print(array1)
print()

#Extend an array using extend() method

array2=array('i',[8,9,10])
array1.extend(array2)
print(array1)
print()

#Add item from List into array using fromlist() method

list=[11,13,13,14]
array1.fromlist(list)
print(array1)
print()

#Remove an elemnt

array1.remove(11)
print(array1)
print()

#Remove last element in an array using POP() method

array1.pop()
print(array1)
print()

#Fetch the elemnt of an array using index

array1.index(3)
print()

#Reverse an array using reverse() method

array1.reverse()
print(array1)
print()

#Get array buffer info using butter_info() method . (Bufer info,no of elements)

print(array1.buffer_info())
print()

#Check the number of occurance of an element using count() method

print(array1.count(13))
print()

#Convert string to array vice versa

str=array1.tostring()
print(str)
array1=array('i')
array1.fromstring(str)
print(array1)
print()

#Convert array to list

print(array1.tolist())
print()

#Slice element from array

print(array1[0:4])
print(array1[:])


# # Two Dimensional Array 

# Creating Two Dimensional array

# In[5]:


import numpy as np
two=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(two)


# # Insert element in Two D array
# 
# Syntax: new_array_name=np.insert(old_array_name , index at which inser , value[ [ ] ] , axis=0/Row or axis=1/coloum)

# In[2]:


import numpy as np
two_d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Old array:\n",two_d)
newtwo_d=np.insert(two_d,3,[[10,11,12]],axis=0)
print("New array:\n",newtwo_d)
print()

#at the end ar array 
newtwo_d=np.append(two_d,[[13,14,15]],axis=0)
print(newtwo_d)


# 
# # Access element of an array

# In[20]:


import numpy as np
two=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(two)
def access(array,rindex,cindex):
    if rindex>=len(array) and cindex>=len(array):
        print("Elemet is not presend in array")
    else:
        print(array[rindex][cindex])
access(two,1,2)


# # Traversal of Two D array

# In[22]:


import numpy as np
two=np.array([[1,2,3],[4,5,6],[7,8,9]])
def traversal(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
traversal(two)


# # Searching Element in a 2D array:- Linear search

# In[32]:


import numpy as np
two=np.array([[1,2,3],[4,5,6],[7,8,9]])
def search(array,target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==target:
                return 'Element present at index :'+str(i)+","+str(j)
    return 'Element not found'
print(search(two,9))


# # Deletion in 2D array

# In[37]:


import numpy as np
two_d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Old array:\n",two_d)
newtwo_d=np.delete(two_d,0,axis=0)
print("New array:\n",newtwo_d)
print()


# In[ ]:


form array import *
a1=array('f',[1.2,2.3,4.5])
pri

