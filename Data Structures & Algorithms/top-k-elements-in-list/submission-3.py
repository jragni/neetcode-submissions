class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter[n] + 1 if n in counter else 1
        
        sorted_counter_list = [(key,value) for (key,value) in counter.items()]
        sorted_counter_list.sort(key=lambda x: x[1], reverse=True)

        sorted_values = [key for key,val in sorted_counter_list]
        print(sorted_values)

        return sorted_values[0:k]