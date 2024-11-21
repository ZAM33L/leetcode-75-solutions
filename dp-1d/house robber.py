from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
       
        prev_not_rob, prev_robbed = 0, 0
        
        for current_house_value in nums:
           
            temp = max(prev_not_rob, prev_robbed)
            #temp stores the maximum amount if we don't rob the current house.
            prev_robbed = prev_not_rob + current_house_value
            prev_not_rob = temp

        
        return max(prev_not_rob, prev_robbed)