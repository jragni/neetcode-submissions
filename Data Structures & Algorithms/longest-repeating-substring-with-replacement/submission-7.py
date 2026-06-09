class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxf = 0
        res = 0
        left, right = 0, 0

        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxf = max(maxf, freq[s[right]]) 

            if right - left - maxf >= k:
                freq[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        
        return res