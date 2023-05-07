class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def delete_zero_sum_sublists(head: Node) -> Node:
    dummy = Node(0)
    dummy.next = head
    prefix_sum = 0
    sum_map = {0: dummy}
    while head:
        prefix_sum += head.val
        if prefix_sum in sum_map:
            prev = sum_map[prefix_sum]
            # Delete nodes between prev and head
            curr = prev.next
            curr_sum = prefix_sum
            while curr != head:
                curr_sum += curr.val
                del sum_map[curr_sum]
                curr = curr.next
            # Update prev.next to skip over deleted nodes
            prev.next = head.next
        else:
            sum_map[prefix_sum] = head
        head = head.next
    return dummy.next
