#!/usr/bin/env python
# coding: utf-8

# # Hashmap
# 
# Hash maps are indexed data structures. A hash map makes use of a hash function to compute an index 
# 
# with a key into an array of buckets or slots. Its value is mapped to the bucket with the corresponding index.
# 
# The key is unique and immutable

# In[2]:


#Creating a hashmap

d={}
d[1]='chiku'
d[2]='23'
print(d)


# In[6]:


#Accessing key
d={}
d[1]='chiku'
d[2]='23'
print(d[1])


# In[12]:


#delete key

d={}
d[1]='chiku'
d[2]='23'
d['singh']=22
print(d)
d.pop(2)          #delete by using pop(key)
print(d)

del d['singh']         #delet using del[key]
print(d)


# In[16]:


a='sudhanshu'
d={}
for i in a:
    if i not in d:
        d[i]=a.count(i)
print(d)


# In[5]:


d={'a':2,'b':3,'c':1}
for i in d:
    if i.values<2:
        print("false")


# In[ ]:




