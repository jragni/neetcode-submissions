class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counts = self.charCount(s)
        t_counts = self.charCount(t)

        for char in s:
            if not char in t_counts or s_counts[char] != t_counts[char]:
                return False
        return True
        
    def charCount(self, s:str) -> dict:
        counts = {};
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        return counts