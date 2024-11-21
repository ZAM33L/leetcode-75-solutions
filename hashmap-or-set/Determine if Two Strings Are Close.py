class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        fm1 = Counter(word1)
        fm2 = Counter(word2)

        if sorted(fm1.keys()) == sorted(fm2.keys()):
            if sorted(fm1.values()) == sorted(fm2.values()):
                return True
        return False