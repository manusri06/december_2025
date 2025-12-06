class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        for i in range(n):
            t = nums[i]
            res[i] = nums[t]
        return res