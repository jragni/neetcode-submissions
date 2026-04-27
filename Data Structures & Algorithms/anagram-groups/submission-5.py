class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # have an object called seen
        # for each string
            # take a copy of the string and sort it
            # add the sorted string to the object as the key
            # add the unsorted to the array as the value
        # return thearray

        seen = {}

        for s in strs:
            s_copy = [char for char in s]
            s_copy.sort()
            s_copy = ''.join(s_copy)
            
            if s_copy in seen:
                seen[s_copy].append(s)
            else:
                seen[s_copy] = [s]
        
        return [val for val in seen.values()]