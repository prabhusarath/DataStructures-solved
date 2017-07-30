
# coding: utf-8

# In[39]:

def InsertSort(arr):
    
    for i in range(1,len(arr)):
        
        value = arr[i]
        pos = i
        
        while pos > 0 and arr[pos-1]>value:
            arr[pos] = arr[pos-1];
            pos = pos-1;
            
        arr[pos] = value
     

    return arr
    

