def mergeTwoLists(list1, list2):
    merged = ListNode(0)
    merge_head = merged
    while list1 or list2:
        if not list1:
            merge_head.next = list2
            break
        elif not list2:
            merge_head.next = list1
            break
        else:
            if list1.val < list2.val:
                merge_head.next = list1
                list1 = list1.next
            else:
                merge_head.next = list2
                list2 = list2.next
        merge_head = merge_head.next
    return merged.next
