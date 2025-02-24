class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        longest = 0
        letters = set([s[0]])

        left = 0
        right = 1

        while right < len(s):
            newCharacter = s[right]
            while newCharacter in letters:
                letters.remove(s[left])
                left += 1

            letters.add(newCharacter)
            longest = max(longest, right - left + 1)
            right += 1

        return longest

