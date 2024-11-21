class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        if not root : return 0

        q = [root]
        max_level = 1
        level = 1
        max_sum = float('-inf')

        while q:

            level_sum = 0
            next_level = []

            for node in q:

                level_sum += node.val

                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)

            if level_sum > max_sum :
                max_sum = level_sum
                max_level = level
            
            q = next_level
            level += 1

        return max_level
    
    
    
    # this prog returns only hte max sum .this is based on the prev progs concept
"""class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = float('-inf')  # Initialize max sum to negative infinity
        q = collections.deque([root])  # Queue for level order traversal

        while q:
            level_sum = 0  # Initialize sum for the current level
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level_sum += node.val  # Add the current node's value to the level sum
                    if node.left:
                        q.append(node.left)  # Add left child to the queue if it exists
                    if node.right:
                        q.append(node.right)  # Add right child to the queue if it exists
            
            max_sum = max(max_sum, level_sum)  # Update max_sum if the current level_sum is greater
        
        return max_sum
"""

