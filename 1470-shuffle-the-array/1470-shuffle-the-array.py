class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(2*n):
            if i%2 == 0:
                res.append(nums[i//2])
            else:
                res.append(nums[n+i//2])
        return res
""" l = len(nums)
res = [0]*l
e , j = 0 , 1
for i in range(l):
    if i<n:
        res[e] = nums[i]
        e += 2
    else:
        res[j] = nums[i]
        j +=2
return res """