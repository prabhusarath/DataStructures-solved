
# coding: utf-8

# In[17]:

def anagram_check(str1,str2):
    
    
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()
                        
    if len(str1) != len(str2):
        return False
    
    dict1={}
    
    
    for i in str1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] =1
            
    for j in str2:
        if j in dict1:
            dict1[j] -= 1
        else:
            dict1[j] =1
            
            
    for k in dict1:
        if dict1[k] != 0:
            return False
        
        
    return True


# In[21]:

anagram_check('Wlliam Shakespeareyu','I amy a weaksh spelleru')


# In[ ]:



