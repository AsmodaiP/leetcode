# https://leetcode.com/problems/binary-search/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binary_search(nums, target, left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(nums, target, mid + 1, right)
            else:
                return binary_search(nums, target, left, mid - 1)

        return binary_search(nums, target, 0, len(nums) - 1)
