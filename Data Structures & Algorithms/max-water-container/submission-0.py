class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1 
        area = 0
        while left < right:
            dx = right - left
            dy = min(heights[left], heights[right])
            area = max(area, dx * dy)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return area
            
