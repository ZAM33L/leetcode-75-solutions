from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies=max(candies)

        return[(curNum + extraCandies >= maxCandies) for curNum in candies]


# time and space complexity - O(N) and O(1)