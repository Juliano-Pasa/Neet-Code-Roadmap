from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for str in strs:
            letters = [0] * 26
            for c in str:
                letters[ord(c) - ord('a')] += 1
            
            name = ""
            for i in range(len(letters)):
                name += chr(i + ord('a')) * letters[i]

            groups[name].append(str)

        result = []
        for group in groups:
            result.append(groups[group])

        return result