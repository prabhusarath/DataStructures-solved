
# coding: utf-8

# In[33]:

def leader(arr):
    
    # An element is leader if it is greater than all the elements to its right side.
    
    larg = arr[len(arr)-1]
    li = [larg]
    
    for x in range(len(arr)-2,-1,-1):
        print(x)
        if arr[x] > larg:
            li.append(arr[x])
            larg = arr[x]
    
    return li

