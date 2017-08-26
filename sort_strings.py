
# coding: utf-8

# In[41]:

def sort_strings(arr):
    
    returns = ''
    
    for element in arr:
        if element.isalpha():
            returns += ''.join(sorted(element))
                
                
    return ''.join(sorted(returns))      


# In[42]:

sort_strings(['bca','df2e','g','ijh'])

