class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        temp = " "
        i = 0
        al = len(a)
        bl = len(b)
        limit = (bl//al)+1
        while b not in temp:
            if i<=limit:
                i += 1
                temp = a*i
            else:
                return -1
        return i