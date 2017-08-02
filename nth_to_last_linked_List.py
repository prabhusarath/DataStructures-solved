
# coding: utf-8

# In[ ]:

def nth_to_last(n,link):
    
    run1 = link
    run2 = link
    
    for i in range(n):
        run2 = run2.nextNode
        
    while run2.nextNode != None:
        run1 = run1.nextNode
        run2 = run2.nextNode
    
    return run1.value

