class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()

        count = 0
        for ch in word:
            if ch.islower():
                lower.add(ch)
            else:
                upper.add(ch)
        for ch in lower:
            if ch.upper() in upper:
                count+=1
        return count