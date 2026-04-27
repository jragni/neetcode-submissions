class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        copy = [*nums]
        copy.sort()
        res = []
        for i in range(len(copy) - 2):
            if i > 0 and copy[i] == copy[i-1]:
                continue
            left, right = i + 1, len(copy) - 1
            while left < right:
                triplet = copy[i] + copy[left] + copy[right] 

                if triplet > 0:
                    right -= 1
                elif triplet < 0:
                    left += 1
                else:
                    res.append([copy[i], copy[left], copy[right]])
                    left += 1
                    right -= 1
                    while copy[left] == copy[left-1] and left < right:
                        left +=1
        return res