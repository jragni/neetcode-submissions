class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) or not s1:
            return False

        def _get_counts(s): 
            freq = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
            for c in s:
                freq[c] += 1
            return freq
        
        s1_counts = _get_counts(s1)
        s2_counts = _get_counts("")

        k = len(s1)
        #sliding window for 0 -> k
        for i in range(0, k):
            s2_counts[s2[i]] += 1
        
        if s1_counts == s2_counts:
            return True

        for j in range(1, len(s2) - k + 1):
            # decrement j - 1
            s2_counts[s2[j - 1]] -= 1
            # add j + k
            s2_counts[s2[j+k-1]] += 1

            # compare 
            if s2_counts == s1_counts:
                return True
        
        return False
