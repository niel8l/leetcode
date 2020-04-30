class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        length = len(word)
        n = 0
        if length == 0:
            return n
        data = {c: i for i, c in enumerate(keyboard)}
        n = data[word[0]]
        for i in range(1, length):
            n += abs(data[word[i]] - data[word[i-1]])
        return n
