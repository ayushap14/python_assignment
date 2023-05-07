class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def merge_alternate(head1: Node, head2: Node) -> Node:
    dummy = Node(0)
    curr = dummy
    while head1 and head2:
        curr.next = head1
        head1 = head1.next
        curr = curr.next
        curr.next = head2
        head2 = head2.next
        curr = curr.next
    if head1:
        curr.next = head1
    if head2:
        curr.next = head2
    return dummy.next
