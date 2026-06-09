class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        if len(s1) > len(s2):
            return False

        def _get_counts(s):
            freq = {}
            for c in s:
                freq[c] = freq.get(c,0) + 1
            return freq
        
        # get counts of s1
        s1_counts = _get_counts(s1)

        for right in range(len(s2) - len(s1) + 1):
            curr_counts = _get_counts(s2[right:right+len(s1)])
            if curr_counts == s1_counts:
                return True
        
        return False