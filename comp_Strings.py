
# coding: utf-8

# In[6]:

def comp_Strings(arr):
    
    if len(arr) == 0:
        return ""
    
    if len(arr) == 1:
        return arr+"1"
    
    lengths = len(arr)
    
    start = arr[0]
    returns= ""
    i=1
    count = 1
    
    while i < lengths:
        
        if arr[i] == arr[i-1]:
            
            count += 1
        
        else:
            
            returns = returns + arr[i-1] + str(count)
            count = 1
            
        i += 1
    
    return returns + arr[i-1] + str(count)


# In[8]:

comp_Strings('AABCCCDAAA')


# In[ ]:



