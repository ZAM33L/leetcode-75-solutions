class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        operations_count = 0
        
        while left < right:
            sum_of_pair = nums[left] + nums[right]
            
            if sum_of_pair == k:
                operations_count += 1
                left += 1
                right -= 1
            elif sum_of_pair > k:
                right -= 1
            else:
                left += 1
      
        return operations_count
        
        #time complexity - O(n log n)