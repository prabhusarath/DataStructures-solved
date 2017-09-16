
# coding: utf-8

# In[65]:

def water(arr):
    
    left = []
    left.insert(0,-1)
    
    right = []
    values = []

    m = arr[0]
    for i in range(1,len(arr)):
        if m < arr[i]:
            m = arr[i]
        left.append(max(m,arr[i]))
    
    n = arr[len(arr)-1]
    for j in range(len(arr)-2,-1,-1):
        if n < arr[j+1]:
            n = arr[j+1]
        right.append(max(n,arr[j+1]))
    
    right.insert(len(arr)-1,-1)
    
    for k in range(len(arr)):
        if k == 0 or k == len(arr)-1:
            continue
        else:
            values.append(min(left[k],right[k]) - arr[k])
        
    return sum(values)

