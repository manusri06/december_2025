class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        l = u = 0
        for i in word:
            if i.islower():
                l+=1
            else:
                u+=1
        if l>0 and u==0:
            return True

        elif l>0 and (u == 1 and word[0].isupper()):
            return True
        elif u>0 and l == 0:
            return True
        else:
            return False