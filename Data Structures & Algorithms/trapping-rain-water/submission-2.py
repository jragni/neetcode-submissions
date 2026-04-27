class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        area = 0

        while left <= right:
            curr_left = height[left]
            curr_right = height[right]
            # bigger gets handled
            if max_left < max_right:
                area += max(max_left - curr_left, 0)
                max_left = max(curr_left, max_left)
                left += 1
            else:
                area += max(max_right - curr_right, 0)
                max_right = max(curr_right, max_right)
                right -= 1

        return area

       