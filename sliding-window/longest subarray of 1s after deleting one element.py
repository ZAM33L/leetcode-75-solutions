class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l , maxCount , zeros = 0,0,0
        for r in range (len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            maxCount = max(maxCount , r-l)
        return maxCount