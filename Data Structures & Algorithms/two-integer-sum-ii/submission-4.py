class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            complimentary = numbers[left] + numbers[right]
            if target == complimentary:
                return [left + 1, right + 1]
            
            if target > complimentary:
                left += 1
            else:
                right -=1
        return []
            