class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        #t.c -O(n*n)
        fm = defaultdict(int)
        pairs = 0
        for row in grid:
            fm[tuple(row)] += 1
        for col in zip(*grid):
            pairs += fm[col]
        return pairs