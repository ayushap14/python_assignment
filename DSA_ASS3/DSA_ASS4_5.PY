# Graph representation using adjacency list
adj_list = {
    1: [2],
    2: [3, 4],
    3: [4, 5],
    4: [],
    5: [2]
}

def has_cycle(adj_list):
    visited = [False] * (max(adj_list.keys()) + 1)
    rec_stack = [False] * (max(adj_list.keys()) + 1)

    for node in adj_list:
        if not visited[node]:
            if dfs(node, visited, rec_stack, adj_list):
                return True

    return False

def dfs(node, visited, rec_stack, adj_list):
    visited[node] = True
    rec_stack[node] = True

    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            if dfs(neighbor, visited, rec_stack, adj_list):
                return True
        elif rec_stack[neighbor]:
            return True

    rec_stack[node] = False
    return False
has_cycle = has_cycle(adj_list)
print(has_cycle)  # Output: True
