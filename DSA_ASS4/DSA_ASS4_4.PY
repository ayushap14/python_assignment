# Tree representation using adjacency list
adj_list = {
    1: [2, 3],
    2: [4],
    3: [5, 6],
    4: [],
    5: [],
    6: [7],
    7: []
}

def count_trees(adj_list):
    visited = set()
    count = 0

    for node in adj_list:
        if node not in visited:
            count += 1
            dfs(node, visited, adj_list)

    return count

def dfs(node, visited, adj_list):
    visited.add(node)

    for neighbor in adj_list[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, adj_list)
