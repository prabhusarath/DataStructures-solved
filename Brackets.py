
# coding: utf-8

# In[2]:

def duplicate(arr):
    
    stack = [];
    
    open_brackets = ['(','{','['];
    
    matches = [ ( '(', ')'), ('[',']'), ('{','}')]
    
    for x in arr:
        
        if x in open_brackets:
            stack.append(x)
            
        else:
            
            if len(stack) == 0:
                return False
            
            poped = stack.pop();
            
            if (poped,x) not in matches:
                
                return False
    
    
    return True


# In[ ]:



