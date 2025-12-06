class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = len(nums)
        res = [0]*l
        e , j = 0 , 1
        for i in range(l):
            if i<n:
                res[e] = nums[i]
                e += 2
            else:
                res[j] = nums[i]
                j +=2
        return res