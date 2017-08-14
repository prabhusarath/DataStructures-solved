
# coding: utf-8

# In[28]:

class qstack():
    
    def __init__(self):
        self.stack1 = [];
        self.stack2 = [];
    
    def enque(self,ele):
        self.stack1.append(ele)
        
    def dequ(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())     
        return self.stack2.pop()

