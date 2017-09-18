
# coding: utf-8

# In[20]:

def swapAdd(num1,num2):
    
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    
    return num1,num2
    pass


# In[21]:

def swapMul(num1,num2):
    
    num1 = num1 * num2
    num2 = num1 // num2
    num1 = num1 // num2
    
    return num1,num2
    pass


# In[22]:

def swapXor(num1,num2):
    
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2
    
    return num1,num2
    pass

