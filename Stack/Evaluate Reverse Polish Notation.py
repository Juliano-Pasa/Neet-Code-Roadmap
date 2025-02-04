from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))
            print(stack)

        return stack[-1]

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
solution = Solution()
print(solution.evalRPN(tokens))