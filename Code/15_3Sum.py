# 2019-06-08  Runtime: 1064 ms

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if (i == 0 or (i > 0 and nums[i] != nums[i - 1])):
                l = i + 1
                r = len(nums) - 1
                sumTwo = 0 - nums[i]
                while l < r:
                    if (nums[r] + nums[l] == sumTwo):
                        tri = [nums[i], nums[l],  nums[r]]
                        res.append(tri)
                        while (l < r and nums[l] == nums[l + 1]):
                            l += 1
                        while (l < r and nums[r] == nums[r - 1]):
                            r -= 1
                        l += 1
                        r -= 1
                    elif (nums[r] + nums[l] < sumTwo):
                        l += 1
                    else:
                        r -= 1
        return res
