# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        start = ListNode(next=head)
        prev = start
        while head:
            if head.next and head.val == head.next.val:
                head = head.next
                prev.next = head
            else:
                prev = head
                head = head.next
        return start.next