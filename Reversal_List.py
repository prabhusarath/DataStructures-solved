
# coding: utf-8

# In[ ]:

def reverse(links):
    
    if len(links) == 0:
        return
    
    if len(links)<2:
        return links
    
    curr = links
    prev = None
    Next = None
    
    while curr:
        Next = curr.nextNode;
        curr.nextNode = prev
        prev = curr
        curr = Next
        
    return prev


# In[ ]:

class linked_node(object):
    
    def __init__(self,val):
        self.value = val
        self.nextNode = None

