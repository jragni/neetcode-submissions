class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            s_copy = [char for char in s]
            s_copy.sort()
            s_copy = ''.join(s_copy)
            if s_copy in anagrams:
                anagrams[s_copy].append(s)
            else:
                anagrams[s_copy] = [s]
        return [val for val in anagrams.values()]