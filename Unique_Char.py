
# coding: utf-8

# In[3]:

def Unique_Char(str1):
    return len(str1) == len(set(str1))


# In[8]:

def uniques(str1):
    
    dicts = {};
    
    for ch in str1:
        
        if ch in dicts:
            
            return False
        
        else:
            
            dicts[ch] = 1
            
    return True


# In[ ]:



