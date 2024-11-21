class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currAlt , maxAlt = 0,0
        for val in gain:
            currAlt += val
            maxAlt = max(maxAlt , currAlt)
        return maxAlt