class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initialize the pointers
        left, right = 0, len(heights) - 1
        max_area = 0
        # while they dont overlap: 
        while left < right:
            # calculate width
            width = right - left
            # calculate height, which is the min of the two selected heights
            height = min(heights[left], heights[right])
            # calculate the area
            area = width * height
            # compare it with the max area, replace if larger
            max_area = max(area, max_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        # return max_area
        return max_area

