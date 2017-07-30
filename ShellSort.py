
# coding: utf-8

# In[31]:

def Shell(arr):
    mid = len(arr)//2
    
    while mid > 0:
        for s in range(mid):
            ins(arr,s,mid)
        mid = mid //2


# In[32]:

def ins(arr,start,space):
    
    for i in range(start+space,len(arr),space):
        curr = arr[i];
        pos = i
        while arr[pos - space] > curr and pos >= space:
            arr[pos] = arr[pos - space]
            pos = pos - space
        
        arr[pos] = curr

