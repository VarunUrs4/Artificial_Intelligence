graph = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '3': [],
    '4': ['7', '8'],
    '5': ['9', '10'],
    '6': [],
    '7': ['11', '12'],
    '8': [],
    '9': [],
    '10': [],
    '11': [],
    '12': []
}

def dfs(curr,dest,graph,depth):
    print("Expanding :",curr)
    if curr == dest:
        return True
    if depth <= 0:
        return False

    for children in graph[curr]:
        if dfs(children,dest,graph,depth-1):
            return True
    return False

def ids(curr,dest,graph,maxDepth):
    for limit in range(maxDepth):
        print()
        if dfs(curr,dest,graph,limit):
            return True
    return False

if not ids('1','9',graph,4):
    print("\nPath does not exists")
else:
    print("Path does exist")
