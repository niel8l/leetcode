from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:  # NOQA
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        p = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1
        nums1[:j+1] = nums2[:j+1]


s = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
s.merge(nums1, 3, nums2, len(nums2))
print(nums1)
nums2 = [1, 2, 3]
nums1 = [2, 5, 6, 0, 0, 0]
s.merge(nums1, 3, nums2, len(nums2))
print(nums1)
