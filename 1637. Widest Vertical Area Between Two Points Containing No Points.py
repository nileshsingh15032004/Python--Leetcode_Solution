class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return max(starmap(sub, pairwise(sorted(next(zip(*points)))[::-1])))
