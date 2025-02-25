from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        
        longest = 1
        left = 0
        right = 1
        previous = 0

        currentLetter = s[0]
        currentCount = defaultdict(int)
        currentCount[currentLetter] += 1

        while right < len(s):
            currentCount[s[right]] += 1

            if s[right] != currentLetter:
                k -= 1
                previous = min(previous, k)

            if k < 0:
                previous = 0
                while s[left] == currentLetter:
                    currentCount[s[left]] -= 1
                    left += 1
                    previous += 1

                k += currentCount[s[left]] - currentCount[currentLetter]
                previous = min(previous, k)
                currentLetter = s[left]

            right += 1
            longest = max(longest, max(right - left, right - left + previous))

        return longest
