
# coding: utf-8

# In[11]:

class Queue():
    
    def __init__(self):
        self.lists =[]; 
    
    def push(self,element):
        self.lists.append(element)
        
    def pop(self):
        delete = self.lists.pop(0);
        print("poped elements is",delete);
        
    def printf(self):
        print(self.lists);
        
    def isEmpty(self):
        return len(self.lists)==0;


# In[ ]:



