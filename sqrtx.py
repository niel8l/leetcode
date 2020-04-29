class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while True:
            m = n ** 2
            if m == x:
                return n
            if m > x:
                return n - 1
            n += 1


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while True:
            mid = left + (right - left) // 2
            if mid ** 2 > x:
                right = mid - 1
            else:
                if (mid + 1) ** 2 > x:
                    return mid
                left = mid + 1


s = Solution()
print(s.mySqrt(0))
print(s.mySqrt(4))
print(s.mySqrt(8))
print(s.mySqrt(100))
