class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const counts = {}; // number: index
        for (let i = 0; i < nums.length; i++) {
            let potentialAnswer = target - nums[i];
            if (potentialAnswer in counts) return [counts[potentialAnswer], i];
            else counts[nums[i]] = i;
        }
    }
}
