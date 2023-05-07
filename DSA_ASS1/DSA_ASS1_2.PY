class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def reverse_sublist(head: Node, size: int) -> Node:
    prev, curr = None, head
    for _ in range(size):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    head.next = curr
    return prev

def reverse_in_groups(head: Node, k: int) -> Node:
    # Count the length of the list
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    # Reverse each group
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    for i in range(length // k):
        curr_head = prev.next
        prev.next = reverse_sublist(curr_head, k)
        prev = curr_head
    return dummy.next
