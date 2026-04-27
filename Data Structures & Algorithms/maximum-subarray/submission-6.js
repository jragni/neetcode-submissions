class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        let largest = nums[0];
        let prefix = nums[0];
        for (let i = 1; i < nums.length; i++) {
           prefix = Math.max(0, prefix);
           prefix += nums[i];
           largest = Math.max(largest, prefix);
        }
        return largest
    }
}
