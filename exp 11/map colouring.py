
def map_coloring(graph, colors, result):
    if len(result) == len(graph):
        return True

    region = next(r for r in graph if r not in result)

    for color in colors:
        if all(result.get(neighbor) != color
               for neighbor in graph[region]):
            result[region] = color

            if map_coloring(graph, colors, result):
                return True

            del result[region]

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
result = {}

if map_coloring(graph, colors, result):
    print("Map Coloring Solution:")
    for region, color in result.items():
        print(region, ":", color)
else:
    print("No solution exists")
