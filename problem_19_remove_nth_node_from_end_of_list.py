from typing import Optional
from constants import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 0
        headPointer = head
        node_before_removal = head
        while headPointer:
            if index >= n and headPointer.next is not None:
                node_before_removal = node_before_removal.next

            headPointer = headPointer.next
            index += 1

        if n == 1 and index == 1:
            head = None

        elif n == 1:
            node_before_removal.next = None

        elif index == n:
            head = head.next

        else:
            node_before_removal.next = node_before_removal.next.next

        return head
