class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])  # Dimensions of the maze
        i, j = entrance  # Starting position (entrance of the maze)
        q = deque([(i, j)])  # Initialize the queue with the entrance
        maze[i][j] = '+'  # Mark the entrance as visited by replacing it with '+'
        ans = 0  # Steps counter
        while q:
            ans += 1  # Increment the step counter at the beginning of each level
            for _ in range(len(q)):  # Loop over every node in the current level
                i, j = q.popleft()  # Dequeue the front element from the queue
                for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:  # The 4 possible directions
                    x, y = i + a, j + b  # Calculate the next cell's coordinates
                    if 0 <= x < m and 0 <= y < n and maze[x][y] == '.':  # Check if it's within bounds and not visited
                        if x == 0 or x == m - 1 or y == 0 or y == n - 1:  # Check if it's an exit
                            return ans  # Return the current step count as the answer
                        q.append((x, y))  # Enqueue the cell for future exploration
                        maze[x][y] = '+'  # Mark the cell as visited
        return -1 