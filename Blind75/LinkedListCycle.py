def hasCycle(head):
    rabbit = tortoise = head
    while rabbit and rabbit.next:
        tortoise = tortoise.next
        rabbit = rabbit.next.next
        if rabbit == tortoise:
            return True
    return False
