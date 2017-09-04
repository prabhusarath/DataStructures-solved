
# coding: utf-8

# In[17]:

def stairs(arr,search):
    
    columns = len(arr[0])
    
    x,y = 0,columns-1
    
    while x < len(arr) and y >= 0:
        if(search == arr[x][y]):
            return True
        elif(search > arr[x][y]):
            x,y = x + 1,y 
        else:
            x,y = x,y - 1
            
    return False

