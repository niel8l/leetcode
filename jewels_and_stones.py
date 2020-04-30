class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        r = 0
        for s in S:
            if s in jewels:
                r += 1
        return r
