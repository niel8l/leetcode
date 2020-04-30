class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = 0
        while x or y:
            x, xm = divmod(x, 2)
            y, ym = divmod(y, 2)
            if xm != ym:
                n += 1
        return n


s = Solution()
print(s.hammingDistance(1, 4))
