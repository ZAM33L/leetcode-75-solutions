class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #start at city 0
        #recursively check its neighbors
        #count outgoing edges

        edges = { (a,b) for a, b in connections}
        neighbors = { city:[] for city in range (n)}
        visit = set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges , neighbors , visit , changes

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                #check if neighbor can reach city 0
                if (neighbor , city) not in edges:
                    changes +=1
                visit.add(neighbor)
                dfs(neighbor)
        visit.add(0)
        dfs(0)
        return changes


"""
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(a: int, fa: int) -> int:
            return sum(c + dfs(b, a) for b, c in g[a] if b != fa)

        g = [[] for _ in range(n)]
        for a, b in connections:
            g[a].append((b, 1))
            g[b].append((a, 0))
        return dfs(0, -1)

"""
