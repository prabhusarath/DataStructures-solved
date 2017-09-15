
# coding: utf-8

# In[76]:

def negMatrix(arr):
    
    count = 0
    
    for lists in arr:
        for index in range(len(lists),0,-1):
            if lists[index-1]<0:
                count += index
                break

    return count

