class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sorted_word = [char for char in word]
            sorted_word.sort()
            sorted_str = "".join(sorted_word)
            if sorted_str in groups:
                groups[sorted_str].append(word)
            else:
                groups[sorted_str] = [word]
        
        return [v for v in groups.values()]


    def _get_counts(self, s):
        counts = {}
        for char in s:
            counts[char] = counts[char] + 1 if char in s else 1
        return counts