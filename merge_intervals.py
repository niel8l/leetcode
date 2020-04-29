import sys
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n < 2:
            return intervals
        self.sort(intervals)
        r = []
        current = intervals[0]
        for i in range(1, n):
            if current[1] >= intervals[i][0]:
                current = [current[0], max(intervals[i][1], current[1])]
            else:
                r.append(current)
                current = intervals[i]
            if i == n - 1:
                r.append(current)
        return r

    def sort(self, intervals):
        self.mergeSort(intervals, 0, len(intervals) - 1)

    def mergeSort(self, intervals, p, r):
        if p < r:
            q = (p + r) // 2
            self.mergeSort(intervals, p, q)
            self.mergeSort(intervals, q + 1, r)
            self._merge(intervals, p, q, r)

    def _merge(self, intervals, p, q, r):
        left = intervals[p:q+1]
        right = intervals[q+1:r+1]
        left.append([sys.maxsize, sys.maxsize])
        right.append([sys.maxsize, sys.maxsize])
        i = j = 0
        for k in range(p, r+1):
            if left[i][0] <= right[j][0]:
                intervals[k] = left[i]
                i += 1
            else:
                intervals[k] = right[j]
                j += 1


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge([[1, 4], [1, 5]]))
print(s.merge([[1, 4], [2, 3]]))
