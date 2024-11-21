class Solution:
  def countBits(self, n: int) -> list[int]:
    # f(i) := i's number of 1s in bitmask
    # f(i) = f(i / 2) + i % 2 (main formula)
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
      ans[i] = ans[i // 2] + (i & 1)
      # f(i) = f(i / 2) + i % 2 (main formula)

    return ans