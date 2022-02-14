def mergeKLists(self, lists):
    if len(lists) == 0 or lists == None:
        return None
    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if (i+1) < len(lists) else None
            mergedLists.append(self.merge(l1, l2))
        lists = mergedLists
    return lists[0]


def merge(self, l1, l2):
    merged = ListNode(0)
    merge_head = merged
    while l1 and l2:
        if l1.val < l2.val:
            merge_head.next = l1
            l1 = l1.next
        else:
            merge_head.next = l2
            l2 = l2.next
        merge_head = merge_head.next
    if not l1:
        merge_head.next = l2
    else:
        merge_head.next = l1
    return merged.next
