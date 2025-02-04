class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                stack.pop()
            elif c == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                stack.pop()
            elif c == '}':
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        return False
