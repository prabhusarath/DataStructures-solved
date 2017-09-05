
# coding: utf-8

# In[62]:

def List_Intersection(arr1,arr2):
    
    if len(arr1) > len(arr2):
        diff = len(arr1) - len(arr2)
    else:
        arr1,arr2 = arr2,arr1
        diff = len(arr1) - len(arr2)
    
    if arr1[len(arr1)-1] == arr2[len(arr2)-1]:
        print("True")
    else:
        return -1
    
    x = diff    
    for y in range(len(arr2)):
        if arr1[x] == arr2[y]:
            return arr1[x]
        else:
            x = x + 1

    pass

