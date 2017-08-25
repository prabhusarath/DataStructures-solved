
# coding: utf-8

# In[157]:

def getcount(arr,row,col):
    
    if row<0 or col<0 or row >= len(arr) or col >= len(arr[row]):
        return 0
    
    if arr[row][col] == 0:
        return 0
    
    arr[row][col] = 0
#     size = 1
    
    for x in range(row-1,row+2):
        for y in range(col-1,col+2):
            getcount(arr,x,y)
#             size = size + getcount(arr,x,y)
                
    return 1;


# In[158]:

def islands(arr):
    
    maxsize = 0
    island = 0 
    
    for row in range(0,len(arr)):
        for col in range(0,len(arr[row])):
            if arr[row][col] == 1:
                count = getcount(arr,row,col)
                island += 1
                #maxsize = max(count,maxsize)
    
    return island

