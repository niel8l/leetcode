from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        n = 0
        for x, y in zip(guess, answer):
            if x == y:
                n += 1
        return n
