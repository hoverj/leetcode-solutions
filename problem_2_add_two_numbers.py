from typing import Optional
from constants import ListNode


class Solution:
    def print_linked_list(self, head: Optional[ListNode]) -> None:
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry_over = 0
        added_value = 0
        l1_value = 0
        l2_value = 0
        result = ListNode()
        result_pointer = result
        while l1 or l2:
            if l1:
                l1_value = l1.val
                l1 = l1.next
            if l2:
                l2_value = l2.val
                l2 = l2.next

            added_value = l1_value + l2_value + carry_over
            l1_value, l2_value = 0, 0

            carry_over = added_value // 10
            result_pointer.next = ListNode(added_value % 10)
            result_pointer = result_pointer.next

        if carry_over != 0:
            result_pointer.next = ListNode(carry_over)

        return result.next
