class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if not strs:
            return prefix

        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            curr_char = strs[0][i]

            for j in range(1, len(strs)):
                if i >= len(strs[j])  or curr_char != strs[j][i]:
                    return prefix
            
            prefix += curr_char
        
        return prefix