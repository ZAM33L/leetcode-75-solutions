class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        # Helper function to perform DFS (Depth-First Search) on the tree
        def dfs(node, left_length, right_length):
            # If the node is None, we've reached the end of a path
            if node is None:
                return
            # Update the global answer by taking the maximum value found so far
            nonlocal max_length
            max_length = max(max_length, left_length, right_length)
            # Recursively explore the left child, incrementing the "left_length" as we are
            # making a zig (left direction) from the right side of the current node
            dfs(node.left, right_length + 1, 0)
            # Recursively explore the right child, incrementing the "right_length" as we are
            # making a zag (right direction) from the left side of the current node
            dfs(node.right, 0, left_length + 1)
      
        # Initialize the maximum length to 0 before starting DFS
        max_length = 0
        # Start DFS with the root of the tree, initial lengths are 0 as starting point
        dfs(root, 0, 0)
        # Once DFS is complete, return the maximum zigzag length found
        return max_length