
# coding: utf-8

# In[56]:

class Stackedlist():
    
    def __init__(self):
        self.lists =[]; 
    
    def push(self,element):
        self.lists.append(element);
        
    def pop(self):
        delete = self.lists.pop();
        print("poped elements is",delete);
        
    def printf(self):
        print(self.lists);
        
    def isEmpty(self):
        return len(self.lists)==0;
    
    def peeks(self):
        return self.lists[len(self.lists)-1];


# In[ ]:



