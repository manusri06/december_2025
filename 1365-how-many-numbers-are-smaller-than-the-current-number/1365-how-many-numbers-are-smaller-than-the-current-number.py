class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        freq = {}
        for i,j in enumerate(s):
            if j not in freq:
                freq[j] = i

        return [freq[n] for n in nums]
            
            