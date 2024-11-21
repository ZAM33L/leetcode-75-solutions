# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        # Helper function to perform depth-first search
        def dfs(node, current_sum):
            if node is None:
                return 0
            # Increment the current path's sum with the current node's value
            current_sum += node.val
          
            # Number of times the (current_sum - target_sum) has occurred so far
            # which indicates a valid path when subtracted from the current_sum
            path_count = path_counts[current_sum - target_sum]
          
            # Store the current path's sum in the counter
            path_counts[current_sum] += 1
          
            # Recursively find paths in left and right subtrees
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)
          
            # Once the node is done, remove its sum from the counter
            # to not use it in the parallel subtree calls
            path_counts[current_sum] -= 1
          
            # Return the number of paths found
            return path_count

        # Initialize a counter to keep track of all path sums
        path_counts = Counter({0: 1})
      
        # Call the dfs function from the root of the tree
        return dfs(root, 0)
