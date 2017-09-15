
# coding: utf-8

# In[8]:

def kadane(arr):
    
    curr = glob = arr[0]
    
    for index in range(1,len(arr)):
        curr = max(arr[index],arr[index]+curr)
        if curr > glob:
            glob = curr 
    
    return glob


# In[ ]:



