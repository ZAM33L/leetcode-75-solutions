class Solution:
  def singleNumber(self, nums: list[int]) -> int:
    return functools.reduce(operator.xor, nums, 0)
#tc and sc - O(n) and O(1)