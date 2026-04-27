class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        # loop through each word
        for word in strs:
            # get a sorted veresion of the word
            sorted_word = "".join(sorted(word))
            # if it is in the groups
            if sorted_word in groups:
                # append
                groups[sorted_word].append(word)
            # otherwise, create a new key and append
            else:
                groups[sorted_word] = [word]
        
        # return values of the groups
        return [v for v in groups.values()]