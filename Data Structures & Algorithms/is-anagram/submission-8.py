class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_counts = self._frequency_counter(s)
        t_counts = self._frequency_counter(t)

        return s_counts == t_counts
             
    def _frequency_counter(self, s):
        counts = {}
        for char in s:
            counts[char] = 1 if char not in counts else counts[char] + 1
        return counts