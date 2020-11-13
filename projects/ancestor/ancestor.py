'''
Plan
1. Translate into graph terminology
   - vertices: each individual in the dataset
   - edges: connect children to parents
   - weights: n/a
   - path: youngest to oldest, generation by generation
2. Build graph:
   - adjacency list with each individual as a key and the value is a set of the parents
3. Traverse graph:
   - farthest distance -> DFT
'''
def earliest_ancestor(ancestors, starting_node):
    graph = {}
    
    for pair in ancestors:
        parent, child = pair[0], pair[1]
        
        if parent not in graph:
            graph[parent] = set()
        
        if child not in graph:
            graph[child] = {parent}
        else:
            graph[child].add(parent)
    
    print(graph)

earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 10)
            
    