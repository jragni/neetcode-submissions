class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        count, longest = 0, 0
        left, right = 0, 0
        
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            right += 1
            count = right - left
            longest = max(count, longest)
            
        return longest
