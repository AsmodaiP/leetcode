# Definition for singly-linked list.
# https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        currentNode1 = list1
        currentNode2 = list2
        start = result = ListNode()
        while currentNode1 and currentNode2:
            if currentNode1.val <= currentNode2.val:
                result.next = currentNode1
                currentNode1 = currentNode1.next
            else:
                result.next = currentNode2
                currentNode2 = currentNode2.next
            result = result.next

        result.next = currentNode1 or currentNode2
        return start.next
