class Solution:
    def climb_stairs(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb_stairs(i+1, n) + self.climb_stairs(i + 2, n)

    def climbStairs(self, n: int) -> int:
        return self.climb_stairs(0, n)


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)
        return self.climb_stairs(0, n, memo)

    def climb_stairs(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climb_stairs(i+1, n, memo) + self.climb_stairs(i+2, n, memo)
        return memo[i]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second


s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(5))
