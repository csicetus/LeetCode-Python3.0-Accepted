# 2019-05-30  Runtime: 60 ms
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Mydict = {}
        for i, num in enumerate(nums):
            if target - nums[i] in Mydict:
                return [Mydict[target - nums[i]], i]
            if nums[i] not in Mydict:
                Mydict[nums[i]] = i
