from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sortedHead = ListNode()
        sortedPointer = sortedHead
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        while list1 and list2:

            if list1 and list2:
                value1 = list1.val
                value2 = list2.val

                if value1 <= value2:
                    sortedPointer.next = list1
                    list1 = list1.next

                else:
                    sortedPointer.next = list2
                    list2 = list2.next

            sortedPointer = sortedPointer.next

        if list2:
            sortedPointer.next = list2

        if list1:
            sortedPointer.next = list1

        return sortedHead.next
