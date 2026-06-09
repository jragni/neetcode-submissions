class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxf = 0
        left, right = 0, 0
        res = 0

        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxf = max(freq.get(s[right]), maxf)

            while right - left - maxf >= k:
                freq[s[left]] -= 1
                left += 1

            
            res = max(res, right - left + 1)

            right += 1
        
        return res
