class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
      return [[1 if b==0 else 0 for b in t[::-1]] for t in image]
