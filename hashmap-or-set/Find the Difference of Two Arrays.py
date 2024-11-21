class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #time and space complexity - O(n+m)
        nS1 , nS2 = set(nums1) , set(nums2) #given set
        r1 , r2 = set() , set() #result sets

        for n in nums1:
            if n not in nS2:
                r1.add(n)
        for n in nums2:
            if n not in nS1:
                r2.add(n)
        
        return [list(r1),list(r2)] #final list