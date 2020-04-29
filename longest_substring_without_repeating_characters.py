class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        chars = set()
        r = i = j = 0
        while i < n and j < n:
            if s[j] not in chars:
                chars.add(s[j])
                j += 1
                r = max(r, j - i)
            else:
                chars.remove(s[i])
                i += 1
        return r


s = Solution()
print(s.lengthOfLongestSubstring('tmmzuxt'))
print(s.lengthOfLongestSubstring(''))
print(s.lengthOfLongestSubstring('abcabcbb'))
print(s.lengthOfLongestSubstring('bbbbb'))
print(s.lengthOfLongestSubstring('pwwk'))
print(s.lengthOfLongestSubstring('pwwkew'))
print(s.lengthOfLongestSubstring('dvdf'))
print(s.lengthOfLongestSubstring('ckilbkd'))
