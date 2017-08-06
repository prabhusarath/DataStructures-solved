
# coding: utf-8

# In[49]:

def find(arr1,arr2):
    
    
    arr1 = sorted(arr1);
    arr2 = sorted(arr2);
    
    for i,j in zip(arr1,arr2):
        
        if i!=j:
            return i
        
    
    return -1
    pass


# In[53]:

find([3,8,7,5,6],[7,5,8,3])


# In[51]:

import collections

def finds(arr1,arr2):
    
    
    arr1 = sorted(arr1);
    arr2 = sorted(arr2);
    
    keysdict = {}  
        
    for i in arr1:
        if i in keysdict:
            keysdict[i] += 1
        else:
            keysdict[i] = 1 
    
    for j in arr2:
        if j in keysdict:
            keysdict[j] -= 1
            

    for k in keysdict:
        if keysdict[k] != 0:
            print(k)
        
    pass


# In[54]:

finds([3,8,7,5,6],[6,5,8,7])


# In[ ]:



