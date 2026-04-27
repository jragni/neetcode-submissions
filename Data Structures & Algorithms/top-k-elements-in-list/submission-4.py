class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        # get sorted dict 
        sorted_counts = [pair for pair in counts.items()]
        sorted_counts.sort(key=lambda x: x[1], reverse=True)

        return [key for key, val in sorted_counts][0:k]