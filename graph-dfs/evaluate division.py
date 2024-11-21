from typing import List
import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)  # Map a -> list of [b, a/b]

        # Build the graph
        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        # Function to perform BFS
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1.0
            q, visit = collections.deque([(src, 1.0)]), set()
            visit.add(src)

            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append((nei, w * weight))
                        visit.add(nei)

            return -1.0

        # Evaluate each query
        result = []
        for src, target in queries:
            result.append(bfs(src, target))
        return result








"""
from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
      
        # This function finds the root of the set to which 'x' belongs
        # It uses path compression to make subsequent lookups faster
        def find(x):
            if parent[x] != x:
                original_parent = parent[x]
                parent[x] = find(parent[x])  # Recursively find the root parent
                weight[x] *= weight[original_parent]  # Adjust the weight
            return parent[x]

        # Initialize default dictionary for weights and parents
        weight = defaultdict(lambda: 1.0)
        parent = defaultdict(str)
      
        # Set initial parent of each variable to itself
        for a, b in equations:
            parent[a], parent[b] = a, b
          
        # Process each equation and union the groups setting the parent relationship and weight
        for i, value in enumerate(values):
            a, b = equations[i]
            root_a, root_b = find(a), find(b)
          
            if root_a != root_b:  # If 'a' and 'b' have different roots, union them
                parent[root_a] = root_b
                weight[root_a] = weight[b] * value / weight[a]
              
        # Process each query
        results = []
        for c, d in queries:
            # If either variable is unknown, or they belong to different sets, the result is -1
            if c not in parent or d not in parent or find(c) != find(d):
                results.append(-1.0)
            else:
                # If they belong to the same set, calculate the result based on weights
                results.append(weight[c] / weight[d])
              
        return results
"""
