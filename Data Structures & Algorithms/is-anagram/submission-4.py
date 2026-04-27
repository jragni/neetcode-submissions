class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = self._get_counts(s)
        t_counts = self._get_counts(t)

        return s_counts == t_counts
    
    def _get_counts(self, s: str) -> dict[str, int]:
        counts = {}
        for char in s:
            counts[char] = counts[char] + 1 if char in counts else 1  
        return counts