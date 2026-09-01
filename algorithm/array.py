graph = [
    [1, 2],    # 0
    [3, 4],    # 1
    [5],       # 2
    [],        # 3
    [5],       # 4
    []         # 5
]

visited = [False] * 6

def dfs(node):
    print(node, end=" ")
    visited[node] = True

    for neighbor in graph[node]:
        if visited[neighbor] == False:
            dfs(neighbor)

dfs(0)