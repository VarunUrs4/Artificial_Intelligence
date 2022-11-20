graph = {
    'A': [('B', 5), ('D', 3)],
    'B': [('C', 1)],
    'C': [('E', 6), ('G', 8)],
    'D': [('E', 2), ('F', 2),],
    'E': [('B', 4)],
    'F': [('G', 3)],
    'G': [('E', 4)]}

def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost, path[-1][0]

def ucs(graph, start, goal):
    queue = [[(start, 0)]]
    visited = []

    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            print(path)
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append([node2, cost])
                queue.append(new_path)

print()
pathSequence = ucs(graph, 'A', 'G')
totalCost = 0

for index in pathSequence:
    totalCost += int(index[1:][0])

print("The minimum cost from 'A' to 'G' is {}".format(totalCost))


