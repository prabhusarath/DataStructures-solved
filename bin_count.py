
# coding: utf-8

# In[52]:

def bin_count(arr):
    count = 0
    
    while arr>0:
        count += arr & 1 
        arr = arr// 2
    
    return count

