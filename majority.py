
# coding: utf-8

# In[83]:

from collections import defaultdict

def majority(arr):
    
    dicts = defaultdict(int)
    
    for x in arr:
        dicts[x] += 1
    
    for key,value in dicts.items():
        if value > len(arr)//2:
            return key
        
    return -1


# In[ ]:



