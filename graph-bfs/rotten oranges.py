class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns of the grid.
        rows, cols = len(grid), len(grid[0])

        # Initialize a queue for BFS and a counter for fresh oranges.
        queue = deque()
        fresh_count = 0
      
        # Go through each cell in the grid.
        for i in range(rows):
            for j in range(cols):
                # If we find a rotten orange, add its position to the queue.
                if grid[i][j] == 2:
                    queue.append((i, j))
                # If it's a fresh orange, increment the fresh_count.
                elif grid[i][j] == 1:
                    fresh_count += 1
      
        # Track the number of minutes passed.
        minutes_passed = 0
      
        # Perform BFS until the queue is empty or there are no fresh oranges left.
        while queue and fresh_count > 0:
            # Increment minutes each time we start a new round of BFS.
            minutes_passed += 1
          
            # Loop over all the rotten oranges at the current minute.
            for _ in range(len(queue)):
                i, j = queue.popleft()
              
                # Check the adjacent cells in all four directions.
                for delta_row, delta_col in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    x, y = i + delta_row, j + delta_col
                  
                    # If the adjacent cell has a fresh orange, rot it.
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        fresh_count -= 1
                        grid[x][y] = 2
                        queue.append((x, y))
      
        # If there are no fresh oranges left, return the minutes passed.
        # Otherwise, return -1 because some oranges will never rot.
        return minutes_passed if fresh_count == 0 else -1