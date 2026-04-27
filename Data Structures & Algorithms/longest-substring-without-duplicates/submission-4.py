class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = left = longest = 0
        
        seen = set()

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, len(seen))
            right += 1
        
        return longest