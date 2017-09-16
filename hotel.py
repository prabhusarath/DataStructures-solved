
# coding: utf-8

# In[53]:

def hotel(arr):
    
    rooms = []
    
    for times in arr:
        for x in range(len(times)):
            if x%2 == 0:
                rooms.append((times[x],"s"))
            else:
                rooms.append((times[x],"c"))
        
    rooms.sort()
    
    count = 0
    maxs = []
    
    for ele in rooms:
        if ele[1] == "s":
            count += 1
        else:
            count -= 1
        maxs.append(count)
        
    return max(maxs)


# In[54]:

hotel([(2,5),(1,3),(4,7)])


# In[ ]:



