class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        p = q = 0
        r = ''
        for s in S:
            if s == '(':
                p += 1
                stack.append(s)
            else:
                q += 1
                stack.append(s)
            if p == q:
                if len(stack) > 2:
                    r += ''.join(stack[1:-1])
                stack = []
        return r


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        r = []
        p = 0
        for s in S:
            if s == '(' and p > 0:
                r.append(s)
            if s == ')' and p > 1:
                r.append(s)
            p += 1 if s == '(' else -1
        return ''.join(r)
