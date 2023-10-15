class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        comman=""
        # returning "" , if  List is not present 
        if len(strs)==0:
            return comman

        # 0 to first_string length
        for i in range(len(strs[0])):

            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return comman
            comman+=strs[0][i]
        return comman
