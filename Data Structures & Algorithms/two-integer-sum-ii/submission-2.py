class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            diff = numbers[left] + numbers[right]
            print(diff, left, right)
            if (diff == target):
                return [left+1,right+1]
            elif diff < target:
                left += 1
            else:
                right -= 1
                
        return []
