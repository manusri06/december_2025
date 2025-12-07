class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_first = {}
        lower_last = {}
        upper_first = {}
        upper_last = {}

        for i, ch in enumerate(word):
            if ch.islower():
                if ch not in lower_first:
                    lower_first[ch] = i
                lower_last[ch] = i
            else:
                c = ch.lower()
                if c not in upper_first:
                    upper_first[c] = i
                upper_last[c] = i

        count = 0
        for ch in lower_first:
            if ch in upper_first:
                if lower_last[ch] < upper_first[ch]:
                    count += 1

        return count

            

            