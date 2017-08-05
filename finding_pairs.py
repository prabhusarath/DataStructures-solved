
# coding: utf-8

# In[41]:

def pairs(arr,finds):
    
    seen = set()
    op = set()
    
    for ele in arr:
        target = finds - ele
        
        if target not in seen:
            seen.add(ele)
        else:
            op.add((target,ele))      
      
    return op


# In[42]:

pairs([1,3,2,2],4)


# In[ ]:




# In[ ]:



