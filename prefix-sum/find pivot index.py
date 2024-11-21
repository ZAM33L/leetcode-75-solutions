class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #also a two pointer
        lSum , rSum = 0 , sum(nums)
        for idx , num in enumerate(nums):
            rSum -= num
            if lSum == rSum:
                return idx
            lSum += num
        return -1