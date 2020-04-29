import sys
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.sortNums(nums)
        n = len(nums)
        res = []
        for i in range(n):
            x = nums[i]
            if x > 0:
                break
            if i > 0 and x == nums[i-1]:
                continue
            for y, z in self.twoSum(nums, i+1, n-1, -x, i):
                res.append([x, y, z])
        return res

    def twoSum(self, nums, lo, hi, target, i):
        while lo < hi:
            sum = nums[lo] + nums[hi]
            if sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):  # NOQA
                hi -= 1
                continue
            if sum < target or (lo > i + 1 and nums[lo] == nums[lo - 1]):
                lo += 1
                continue
            if sum == target:
                yield nums[lo], nums[hi]
                lo += 1
                hi -= 1

    def sortNums(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)
        # return nums

    def mergeSort(self, nums, p, r):
        if p < r:
            q = (p + r) // 2
            self.mergeSort(nums, p, q)
            self.mergeSort(nums, q + 1, r)
            self.merge(nums, p, q, r)

    def merge(self, nums, p, q, r):
        left = nums[p:q+1]
        right = nums[q+1:r+1]
        left.append(sys.maxsize)
        right.append(sys.maxsize)
        i = j = 0
        for k in range(p, r+1):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([-2, 0, 0, 2, 2]))
print(s.threeSum([-2, 0, 3, -1, 4, 0, 3, 4, 1, 1, 1, -3, -5, 4, 0]))
