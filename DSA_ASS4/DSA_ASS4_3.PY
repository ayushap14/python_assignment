from collections import deque

# Tree representation using nested lists
tree = [1, [2, [4, [], []], [5, [], []]], [3, [6, [], []], [7, [], []]]]

def count_nodes_at_level(tree, level):
    queue = deque([(tree, 0)])
    count = 0

    while queue:
        node, node_level = queue.popleft()

        if node_level == level:
            count += 1
        elif node_level > level:
            break

        for child in node[1:]:
            if child:
                queue.append((child, node_level + 1))

    return count

count = count_nodes_at_level(tree, 2)
print(count)  # Output: 4
