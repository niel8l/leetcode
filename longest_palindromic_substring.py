# Longest Common Substring
class Solution:  # NOQA
    def longestPalindrome(self, s: str) -> str:
        pass


# Brute Force
class Solution:  # NOQA
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length <= 1:
            return s
        palindromic = ''
        for i in range(length):
            for j in range(i+1, length+1):
                if s[i:j] == ''.join(reversed(s[i:j])) and len(palindromic) <= j - i:  # NOQA
                    palindromic = s[i:j]
        return palindromic


# Dynamic Programming
class Solution:  # NOQA
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        length = len(s)
        last = {}
        start = 0
        end = 0
        for i in range(length):
            for j in range(i, -1, -1):
                equal = s[i] == s[j]
                if i == j:
                    last[(i, j)] = True
                elif i - j == 1:
                    last[(i, j)] = equal
                else:
                    last[(i, j)] = last[(i-1, j+1)] and equal
                if i - j > end - start and last[(i, j)]:
                    start = j
                    end = i
        return s[start:end+1]


s = Solution()
print(s.longestPalindrome('babad'))
print(s.longestPalindrome('cbbd'))
print(s.longestPalindrome(''))
print(s.longestPalindrome('a'))
print(s.longestPalindrome('bb'))
print(s.longestPalindrome('abacdfgdcaba'))
print(s.longestPalindrome('zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir'))  # NOQA
