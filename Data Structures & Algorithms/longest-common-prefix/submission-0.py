class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = self.getSmallestString(strs)

        res = ""
        for i in range(len(smallest)):
            for s in strs:
                if s[i] != smallest[i]:
                    return res
            res += s[i]
        return res

    
    def getSmallestString(self, strs: List[str]) -> str:
        smallest_length = len(strs[0])
        smallest_str = strs[0]
        for s in strs:
            if len(s) < smallest_length:
                smallest_length = len(s)
                smallest_str = s
        return smallest_str