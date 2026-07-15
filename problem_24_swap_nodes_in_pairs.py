from typing import Optional
from constants import ListNode, list_to_linked_list, print_linked_lists

case = list_to_linked_list([1, 2, 3, 4, 5])
result = list_to_linked_list([2, 1, 4, 3, 5])


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current and current.next:

            next_node = current.next
            current.next = next_node.next
            next_node.next = current
            prev.next = next_node
            prev = current
            current = current.next

        return dummy.next
