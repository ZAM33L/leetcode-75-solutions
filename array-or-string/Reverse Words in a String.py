class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = reversed(words)
        reversed_sentence = ' '.join(reversed_words)
        return reversed_sentence
#time and space complexity