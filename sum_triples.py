
# coding: utf-8

# In[71]:

def sum_triples(arr,value):
    
    arr.sort()
    
    for i in range(len(arr)-2):
            
            j = i + 1
            k = len(arr)-1
        
            while j < k:
                
                if arr[i]+arr[j]+arr[k] == value:
                    return arr[i],arr[j],arr[k]
                elif arr[i]+arr[j]+arr[k] < value:
                    j += 1
                else:
                    k -= 1

