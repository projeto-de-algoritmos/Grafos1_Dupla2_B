import collections

def main(graph, root): 
    visited, queue = set(), collections.deque([root])
    while queue: 
        print(queue)
        vertex = queue.popleft()
        
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 
