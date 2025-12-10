class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        s = a
        i = 1

        while len(s) < len(b):
            s+=a
            i+=1

        if b in s:
            return i

        s = s+a
        i+=1
        if b in s:
            return i
            
        return -1

"""temp = " "
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
return i """