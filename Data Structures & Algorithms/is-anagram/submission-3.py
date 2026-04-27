class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_counts = self.getCounts(s)
        t_counts = self.getCounts(t)

        for key, val in s_counts.items():
            if not key in t_counts or t_counts[key] != val:
                return False
        return True

    def getCounts(self, string):
        counts = {}
        for char in string:
            counts[char] = counts[char] + 1 if char in counts else 1
        return counts