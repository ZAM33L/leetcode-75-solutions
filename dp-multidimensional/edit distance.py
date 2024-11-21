class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Get the lengths of both words
        len_word1, len_word2 = len(word1), len(word2)
      
        # Initialize a table to store the edit distances
        # The table size will be (len_word1+1) x (len_word2+1)
        dp_table = [[0] * (len_word2 + 1) for _ in range(len_word1 + 1)]
      
        # Set up the initial state where converting an empty string to word2
        # requires adding all letters of word2
        for j in range(1, len_word2 + 1):
            dp_table[0][j] = j
      
        # Set up the state where converting word1 to an empty string
        # requires removing all letters of word1
        for i in range(1, len_word1 + 1):
            dp_table[i][0] = i
          
            for j in range(1, len_word2 + 1):
                # If the current characters match, take the previous best without these characters
                if word1[i - 1] == word2[j - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1]
                else:
                    # If the characters don't match, consider all possible operations
                    # 1. Add a character (dp_table[i][j - 1])
                    # 2. Remove a character (dp_table[i - 1][j])
                    # 3. Replace a character (dp_table[i - 1][j - 1])
                    # Take the minimum of these possibilities and add 1 to represent the cost of the operation
                    dp_table[i][j] = min(
                        dp_table[i - 1][j],      # Deletion
                        dp_table[i][j - 1],      # Insertion
                        dp_table[i - 1][j - 1]   # Substitution
                    ) + 1
      
        # The answer is in the bottom-right cell of the table
        # It represents the minimum edit distance between the two full words
        return dp_table[len_word1][len_word2]