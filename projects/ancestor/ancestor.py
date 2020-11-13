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
   - create a hash table that stores the lengths of the path from the starting node
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
    
    
    stack = []
    visited = set()
    path_lengths = {starting_node: 0}
    
    stack.append(starting_node)
    
    while len(stack) > 0:
        current_node = stack.pop()
        
        if current_node not in visited:
            visited.add(current_node)
            
            for n in graph[current_node]:
                stack.append(n)
                path_lengths[n] = 1 + path_lengths[current_node]
      
    longest_path = max(path_lengths.values())
    
    solution = min([k for k,v in path_lengths.items() if v == longest_path])
        
    if solution == starting_node:
        solution = -1
    
    return solution
            
    