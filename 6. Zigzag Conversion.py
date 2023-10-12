class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [[] for _ in range(numRows)]
        level = 0
        answer = ""
        forward = True
        for i in range(len(s)):
            ans[level].append(s[i])
            if forward:
                level += 1
            if not forward:
                level -= 1
            if level > numRows - 1:
                level -= 2
                forward = False
            if level < 0:
                level += 2
                forward = True
        for i in ans:
            for j in i:
                answer += j
        return answer
