from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left_max = [0] * length
        x = 0
        for i in range(length):
            if x <= height[i]:
                x = height[i]
            left_max[i] = x
        right_max = [0] * length
        y = 0
        for i in range(length - 1, -1, -1):
            if y <= height[i]:
                y = height[i]
            right_max[i] = y
        ans = 0
        for i in range(length):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
