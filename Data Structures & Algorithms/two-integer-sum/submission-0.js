class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const dict = {};
        for (let i = 0; i < nums.length; i++) {
            const pot = target - nums[i];
            if (pot in dict) return [dict[pot], i];
            else {
                dict[nums[i]] = i;
            }
        }
    }
}
