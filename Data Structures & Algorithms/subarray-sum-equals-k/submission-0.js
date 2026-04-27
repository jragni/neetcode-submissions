class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    subarraySum(nums, k) {
        let count = 0;
        if (nums.length === 0) return count;
        if (nums.length === 1 && nums[0] !== k) return count;

        for (let i = 0; i < nums.length; i++) {
            let curr = nums[i];
            if (curr === k) count++;
            if (i === nums.length - 1) break;
            
            for (let j = i + 1; j < nums.length; j++) {
                curr += nums[j];
                if (curr === k) count++;
            }
        }
        return count;
    }
}
