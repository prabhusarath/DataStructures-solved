
# coding: utf-8

# In[ ]:

def Cycledetect(start):
    
    run1 = start
    run2 = start
    
    while run2 != None and run2.nextnode != None:
        
        run1 = start.nextnode
        run2 = start.nextnode.nextnode
        
        if run1 == run2:
            return True
        
    return False
    

