class Solution:
    def removeStars(self, s: str) -> str:
        #time complexity -O(n)

        stack = []

        for c in s:

            if c == "*":
                stack and stack.pop()
            else:
                stack.append(c)

        return "".join(stack)