def reverseList(head):
    if not head:
        return
    curr = head
    next_node = curr.next
    prev = None
    while curr:
        curr.next = prev
        prev = curr
        curr = next_node
        if next_node:
            next_node = curr.next
    return prev
