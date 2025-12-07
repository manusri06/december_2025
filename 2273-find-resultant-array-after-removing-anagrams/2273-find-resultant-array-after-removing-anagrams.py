class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        res = [words[0]]
        prev = "".join(sorted(words[0]))

        for i in words[1:]:
            curr = "".join(sorted(i))
            if curr != prev:
                res.append(i)
                prev = curr
        return res



            