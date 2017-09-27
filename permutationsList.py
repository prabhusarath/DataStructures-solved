
# coding: utf-8

# In[55]:

def results(head, tail=[]):
    if len(head) == 0: print(tail)
    else:
        for i in range(len(head)):
            results(head[0:i] + head[i+1:], tail+[head[i]])

