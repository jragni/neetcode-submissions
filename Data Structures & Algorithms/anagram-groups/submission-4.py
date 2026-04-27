class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        # for each string
        for s in strs:
            # get a sorted copy of the string
            s_copy = [char for char in s]
            s_copy.sort()
            s_copy = ''.join(s_copy)

            # check if that sorted copy is in anagrams dict
            if s_copy in anagram_dict:
                # if so, add it to the array of anagrams
                anagram_dict[s_copy].append(s)
            else: 
                # create a new key - value pair with an array including the word
                anagram_dict[s_copy] = [s]
            
        # return the list
        return [v for v in anagram_dict.values()]