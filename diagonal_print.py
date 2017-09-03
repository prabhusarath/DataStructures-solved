
# coding: utf-8

# In[385]:

def diagonal_print(arr):
    
    row_size = len(arr)
    col_size = len(arr[0])
    
    lists =[]
    
    for rr in range(row_size):
        for cc in range(col_size):
            while rr >= 0 and cc < col_size:
                lists.append(arr[rr][cc]) 
                rr = rr - 1
                cc = cc + 1  
      
    for y in range(1,col_size):
        xx,yy = row_size-1,y
        while xx >= 0 and yy < col_size:
            lists.append(arr[xx][yy])
            xx = xx - 1
            yy = yy + 1
            
    return lists

