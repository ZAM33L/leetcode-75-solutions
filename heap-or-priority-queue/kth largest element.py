class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #tc - O(n)[as we r goin to look at one part of the list]
        #quick select - time limit exceeds here
        """
        k = len(nums) - k

        def quickSelect(l,r):
            pivot , p = nums[r] , l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p] , nums[i] = nums[i] ,nums[p]
                    p += 1
            nums[p] , nums[r] = nums[r] ,nums[p]

            if p > k :
                return quickSelect(l , p-1)
            elif p < k:
                return quickSelect(p+1 ,r)
            else:
                return nums[p]

        return quickSelect(0 , len(nums) -1)
        """
         #the easiest case possible
        nums.sort()
        return nums[len(nums) - k]
        