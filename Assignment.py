#!/usr/bin/env python
# coding: utf-8

# In[12]:


nl=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5!=0):
        nl.append((x))
print (nl)


# In[13]:


fname = input("enter a string")
lname = input("enter a string")
print ("hello" + lname + " " + fname)


# In[17]:


v = (1.33) * (3.14) * (216)
print(v)

