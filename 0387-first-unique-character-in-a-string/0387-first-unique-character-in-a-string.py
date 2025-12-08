class Solution:
    def firstUniqChar(self, s: str) -> int:
        f={}
        for i in s:
            if i not in f:
                f[i] = 0
            f[i]+=1

        for i,j in enumerate(s):
            if f[j] == 1:
                return i
        return -1
        