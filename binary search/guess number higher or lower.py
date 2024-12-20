#tc and sc - O(log n) and O(1)
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = (l + r) // 2
            res = guess(m)
            
            if res == 0:
                return m
            elif res < 0:
                r = m - 1
            else:  # res > 0
                l = m + 1
