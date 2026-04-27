class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for word in strs:
            word_copy = [c for c in word]
            word_copy.sort()
            word_copy = ''.join(word_copy)
            print(word_copy)
            if word_copy in grouped:
                grouped[word_copy].append(word)
            else:
                grouped[word_copy] = [word]
            
        return [v for v in grouped.values()]