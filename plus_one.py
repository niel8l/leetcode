class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t = 1
        for i, n in enumerate(digits):
            t += n * (10 ** i)
        ret = []
        while True:
            n = t % 10
            ret.append(n)
            t = t // 10
            if not t:
                break
        return ret[::-1]
