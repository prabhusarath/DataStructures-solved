
# coding: utf-8

# In[7]:

def Str_Reverse(strs):
    
    if len(strs)<=1:
        return strs
    
    return Str_Reverse(strs[1:])+ strs[0]


# In[25]:

def String_Reverse(strs):
    return ''.join(reversed(strs))

