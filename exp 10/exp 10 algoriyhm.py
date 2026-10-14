import heapq
def astar(graph, heuristic, start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()
    while queue:
        f, g, node, path = heapq.heappop(queue)
        if node == goal:
            print("Shortest Path:", path)
            print("Total Cost:", g)
            return
        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    new_g = g + cost
                    new_f = new_g + heuristic[neighbor]
                    heapq.heappush(queue, 
                                   (new_f, new_g, neighbor,
                                    path + [neighbor]))
    print("No path found")
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}
heuristic = {
    'A': 5, 'B': 4, 'C': 4,
    'D': 2, 'E': 1, 'F': 2, 'G': 0
}
astar(graph, heuristic, 'A', 'G')
