from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        
        for word in strs:
            result += str(len(word)) + "."
            result += word

        return result

    def decode(self, s: str) -> List[str]:
        words = []

        current = 0
        size = len(s)

        while current < size:
            wordSize = 0

            while s[current] != ".":
                wordSize *= 10
                wordSize += int(s[current])
                current += 1
            current += 1

            word = ""
            while wordSize > 0:
                word += s[current]
                current += 1
                wordSize -= 1

            words.append(word)

        return words
