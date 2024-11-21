class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0 # 'l' is the left pointer to track the position of non-zero elements.
        for r in range(len(nums)):
            if nums[r]: # If the current element 'nums[r]' is non-zero:
                nums[l] ,nums[r] = nums[r],nums [l]
                l+=1
        return nums