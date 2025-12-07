from math import factorial
class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10**9+7
        ans = 1
        for i in s.split(" "):
            n = len(i)
            freq = {}

            for j in i:
                freq[j] = freq.get(j,0)+1
            num = factorial(n)%MOD
            denomi = 1
            for j in freq.values():
                denomi *= factorial(j)%MOD
            
            ans = (ans * num * pow(denomi, MOD-2, MOD)) % MOD
        return ans