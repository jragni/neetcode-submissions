class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        if (!nums.length) return 0;
        let maxSum = nums[0];
        let curr = 0;
        for (let num of nums) {
            if (curr < 0) curr = 0;
            curr += num;
            maxSum = Math.max(maxSum, curr);
        }
        return maxSum
    }
}
