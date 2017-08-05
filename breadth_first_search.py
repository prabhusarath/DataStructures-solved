
# coding: utf-8

# In[ ]:

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


# In[ ]:

def breadth_search(graph, start):
    queue_imp = [start]
    visited_list = []
    while queue_imp:
        vertex = queue_imp.pop(0)
        if vertex not in visited_list:
            visited_list.append(vertex)
            queue_imp.extend(graph[vertex] - set(visited_list))
    return visited_list

breadth_search(graph, 'A')

