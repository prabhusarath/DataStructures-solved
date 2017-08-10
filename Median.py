
# coding: utf-8

# In[43]:

def get_median(lists):
    
    sorted_list = sorted(lists)
    
    if len(sorted_list) % 2 == 0:
        
        return (sorted_list[len(sorted_list) // 2] + sorted_list[(len(sorted_list)-1) // 2]) /2
        
    else:
        
        return sorted_list[len(sorted_list) // 2]
    pass


# In[46]:

get_median([3,3,1,6,8,9,7])


# In[47]:

get_median([8,1,2,4,3,6,9,5])


# In[ ]:



