
# coding: utf-8

# In[58]:

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


# In[63]:

def depth_search(graph, start):
    stack_imp = [start]
    visited_list = [];
    while stack_imp:
        vertex = stack_imp.pop()
        if vertex not in visited_list:
            visited_list.append(vertex)
            stack_imp.extend(graph[vertex] - set(visited_list))
    return visited_list

depth_search(graph, 'A')


# In[ ]:



