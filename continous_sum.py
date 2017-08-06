
# coding: utf-8

# In[9]:

def continous_sum(arr):
    
    maxsum = arr[0]
    continous = arr[0]
    
    for i in arr[1:]:
        
        continous = max(i+continous,i)
        maxsum = max(maxsum,continous)
        
    return maxsum


# In[ ]:



