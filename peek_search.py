
# coding: utf-8

# In[91]:

def peek(arr):
    
    for x in range(len(arr)):
        
        prevs = x - 1
        nexts = x + 1
        
        if arr[prevs]<arr[x] and arr[x]>arr[nexts]:
            print(arr[x])


# In[103]:

def peek_search(arr):
    
    if len(arr) == 0:
        return -1
    
    start = 0
    end = len(arr)-1
    
    mid = (start+end)//2
    
    if arr[mid-1]< arr[mid] and  arr[mid]>arr[mid+1]:
        print(arr[mid])
        return arr[mid]
    elif arr[mid-1] > arr[mid]:
        peek_search(arr[:mid])
    elif arr[mid+1] > arr[mid]:
        peek_search(arr[mid:])
    else:
        return 0

