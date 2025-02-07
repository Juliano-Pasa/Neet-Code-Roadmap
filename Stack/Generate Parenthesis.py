from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        currentStack = ['(']
        branchingStack = [0]
        count = 1
        remaining = n - 1

        
        while True:
            if len(currentStack) == 2*n:
                result.append("".join([c for c in currentStack]))

                while not count or len(currentStack) == 2*n:
                    while currentStack[-1] != '(':
                        currentStack.pop()
                        count += 1
                    currentStack.pop()
                        
                    count -= 1
                    remaining += 1

                    if not len(currentStack):
                        return result

                currentStack.append(')')
                count -= 1

            if remaining:
                currentStack.append('(')
                branchingStack.append(len(currentStack) - 1)

                count += 1
                remaining -= 1
            else:
                count -= 1
                currentStack.append(')')

        