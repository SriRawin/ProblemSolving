def removeNthFromEnd(head, n):
    curr = rabbit = head
    for _ in range(n):
        rabbit = rabbit.next
    if rabbit == None:
        return head.next
    while rabbit.next:
        rabbit = rabbit.next
        curr = curr.next
    curr.next = curr.next.next
    return head
