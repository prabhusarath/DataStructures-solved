
# coding: utf-8

# In[41]:

def miss(arr):
    
    arr.sort();

    arr = [x for x in arr if x>0]
    
    returns = list(set(range(1,max(arr))) - set(arr))
    
    if len(returns) == 0:
        return max(arr)+1
    else:
        return min(returns)

