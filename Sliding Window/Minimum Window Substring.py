from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        frequencies = defaultdict(int)
        for c in t:
            frequencies[c] += 1

        smallest = len(s) + 1
        startSmallest = 0

        left = 0
        right = 0
        missingLetters = len(t)

        currentFrequencies = defaultdict(int)
        while right < len(s):
            currentFrequencies[s[right]] += 1

            if currentFrequencies[s[right]] <= frequencies[s[right]]:
                missingLetters -= 1

            while missingLetters == 0:
                if right - left < smallest:
                    smallest = right - left
                    startSmallest = left

                currentFrequencies[s[left]] -= 1
                if currentFrequencies[s[left]] < frequencies[s[left]]:
                    missingLetters += 1

                left += 1
            right += 1

        if smallest > len(s):
            return ""
        return s[startSmallest : startSmallest + smallest + 1]
