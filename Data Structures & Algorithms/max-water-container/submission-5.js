class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let largestArea = 0;
        let left = 0, right = heights.length - 1;
        while (left < right) {
            const deltaX = right - left;
            const deltaY = Math.min(heights[left], heights[right]);
            const area = deltaX * deltaY;
            largestArea = Math.max(largestArea, area);
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return largestArea;
    }
}
