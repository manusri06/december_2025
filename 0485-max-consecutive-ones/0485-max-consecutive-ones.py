class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = t = 0
        for i in nums:
            if i & 1 :
                t += 1
                maxi = max(maxi,t)
            else:
                t = 0
        return maxi