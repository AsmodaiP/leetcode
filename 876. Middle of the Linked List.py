# https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        start = head
        while head.next:
            count += 1
            head = head.next
        mid = count // 2
        if count % 2 != 0:
            mid += 1

        for _ in range(mid):
            start = start.next
        middleNode = start
        return middleNode
