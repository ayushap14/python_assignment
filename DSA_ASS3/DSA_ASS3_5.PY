from collections import deque

# Adjacency list representation of graph
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

# Breadth First Search (BFS) function
def bfs(graph, start):
    visited = set()  # set to keep track of visited nodes
    queue = deque([start])  # deque to store nodes to visit
    
    while queue:
        node = queue.popleft()  # remove the node at the front of the deque
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for neighbor in graph[node]:
                queue.append(neighbor)

# Depth First Search (DFS) function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Test the functions
print("BFS:", end=' ')
bfs(graph, 1)
print("\nDFS:", end=' ')
dfs(graph, 1)
