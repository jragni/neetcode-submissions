class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            # get counts
            s_counts = [f'{count}' for count in self.get_counts(s)]
            # turn counts to into a key where values are array
            key = ",".join(s_counts)
            print(key)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
            print(groups)

        # return values
        return [v for v in groups.values()]
    

    def get_counts(self, s):
        counts = [0]*26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        
        return counts