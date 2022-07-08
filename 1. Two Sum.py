# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remain_dict = {}
        for num_index in range(len(nums)):
            num = nums[num_index]
            remain = target - num
            remain_dict[remain] = remain_dict.get(remain, []) + [num_index]

        for key in remain_dict:
            if target-key in remain_dict:
                if target-key == key:
                    if len(remain_dict[key]) > 1:
                        return remain_dict[key]
                else:
                    return [remain_dict[key][0], remain_dict[target-key][0]]
