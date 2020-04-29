class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return f'{int(a, 2) + int(b, 2):b}'


s = Solution()
print(s.addBinary('11', '1'))
print(s.addBinary('1010', '1011'))
