from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[0] > target or letters[-1] <= target:
            return letters[0]

        i = 1
        while i < len(letters):
            if target >= letters[i-1] and target < letters[i]:
                return letters[i]
            i += 1

        return letters[0]
