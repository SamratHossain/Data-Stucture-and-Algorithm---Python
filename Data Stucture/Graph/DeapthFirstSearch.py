def breadthFirstSearch(graph, startVertex):
    queue = [startVertex] 
    visited = [] 

    while queue:
        vertex = queue.pop(0) 
        if vertex not in visited:
            visited.append(vertex)

            for neighbar in graph[vertex]:
                    if neighbar not in visited:
                        queue.append(neighbar)

    print(visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

breadthFirstSearch(graph, 'A')

