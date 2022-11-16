graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [],
    4: [7, 8],
    5: [9, 10],
    6: [],
    7: [11, 12],
    8: [],
    9: [],
    10: [],
    11: [],
    12: []
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    print("\nBFS traversal : ")

    while queue:
        x = queue.pop(0)
        print(x , end=" ")

        for adjacent in graph[x]:
            if adjacent not in visited:
                visited.append(adjacent)
                queue.append(adjacent)

    print("")

bfs(visited, graph, 1)



