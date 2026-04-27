class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        if (height.length <= 2) return 0;
        let maxArea = 0;
        let left = 0;
        let right = height.length - 1;
        let leftMax = height[left];
        let rightMax = height[right];

        while (left <= right) {
            if (leftMax < rightMax) {
                leftMax = Math.max(leftMax, height[left]);
                maxArea += leftMax - height[left];
                left++;
                console.log('left', leftMax, 'max', maxArea);
            } else {
                rightMax = Math.max(rightMax, height[right]);
                maxArea += rightMax - height[right];
                right--;
                console.log('right', rightMax, 'max', maxArea);
            }
        }
        return maxArea;
    }
}
