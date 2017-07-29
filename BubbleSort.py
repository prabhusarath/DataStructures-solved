
# coding: utf-8

# In[38]:

def Bubble_sort(arr):
    
    for index in range(len(arr)-1,0,-1):
        
        for i in range(index):
            
            if arr[i]>arr[i+1]:
                
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
    
    return arr
    


# In[ ]:



