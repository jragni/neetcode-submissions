class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0;

        if len(heights) <= 1:
            return max_area
        
        while left < right:
            dx = right - left
            dy = min(heights[left], heights[right])
            area = dx * dy
            max_area = max(area, max_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_area 
