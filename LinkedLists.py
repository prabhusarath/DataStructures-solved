
# coding: utf-8

# In[32]:

class linked_node(object):
    
    def __init__(self,val):
        self.value = val
        self.nextNode = None


# In[33]:

a = linked_node(1)
b = linked_node(2)
c = linked_node(3)


# In[ ]:

a.nextNode = b;
b.nextNode = c;


# In[26]:

class Double_linked_node(object):
    
    def __init__(self,val):
        self.value = val
        self.nextNode = None
        self.prevNode = None


# In[27]:

p = Double_linked_node(10)
q = Double_linked_node(20)
r = Double_linked_node(30)


# In[28]:

p.nextNode = q;
q.prevNode = p;
q.nextNode = r;
r.prevNode = q;


# In[ ]:



