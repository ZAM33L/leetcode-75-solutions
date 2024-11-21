class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        current_sum = 0

        for i in range(k):
            current_sum += nums[i]

        max_avg = current_sum /k

        for i in range (k,n):
            current_sum += nums[i]
            current_sum -= nums[i-k]

            avg = current_sum / k
            max_avg = max(max_avg , avg)

        return max_avg