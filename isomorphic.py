
# coding: utf-8

# In[31]:

def iso(word1,word2):
    
    if len(word1)!= len(word2):
        return False
    
    oneto2 = {}
    twoto1 = {}
    
    for i,j in zip(word1,word2):
        if i not in oneto2 and j not in twoto1:
                oneto2[i] = j
                twoto1[j] = i
        elif oneto2[i] != j:
            return False

    return True


# In[ ]:



