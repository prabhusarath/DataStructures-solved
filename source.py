
# coding: utf-8

# In[81]:

from collections import defaultdict

def source(arr):
    
    dicts = defaultdict(int)
    series=[]
    
    if len(arr) == 0:
        return -1
    
    if len(arr) == 1:
        return arr[0]
        
    for i,j in arr:
        dicts[j] += 1;
        dicts[i] += 1;
        
    print(dicts.items())
    
    for keys in dicts:
        if dicts[keys] == 1:
            series.append(keys)
            
    return series


# In[ ]:



