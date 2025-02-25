from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        frequencies = [0] * 26
        for c in s1:
            frequencies[ord(c) - ord('a')] += 1

        left = 0
        right = 0
        currentFrequencies = [0] * 26

        while right < len(s2):
            index = ord(s2[right]) - ord('a')
            currentFrequencies[index] += 1

            while currentFrequencies[index] > frequencies[index]:
                currentFrequencies[ord(s2[left]) - ord('a')] -= 1
                left += 1

            right += 1
            if right - left == len(s1):
                return True
            
        return False