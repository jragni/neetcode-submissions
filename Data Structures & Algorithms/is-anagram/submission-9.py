class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counts = self.get_counts(s)
        t_counts = self.get_counts(t)

        return s_counts == t_counts


    def get_counts(self, s: str) -> List[int]:
        counts = [0]*26
        for char in s:
            char_idx = ord(char) - ord('a')
            counts[char_idx] += 1

        return counts
