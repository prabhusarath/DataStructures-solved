class Deque(object):
    
    def __init__(self):
        self.deque = []
        
        
    def InsertFront(self,value):
        self.deque.insert(0,value)
        
        
    def InserBack(self,value):
        self.deque.append(value)
        
        
    def DelFront(self):
        delf = self.deque.pop(0);
        return delf
    
    def DelBack(self):
        delb = self.deque.pop();
        return delb
    
    def isEmpty(self):
        return self.deque == []
    
    
    def size(self):
        return len(self.deque)
    