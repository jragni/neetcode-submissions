class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     */
    containsNearbyDuplicate(nums, k) {
        if (nums.length <= 1) return false;
        let seen = new Set();
        let left = 0;
        for (let right = 0; right < nums.length; right++) {
            if (seen.has(nums[right])) return true;
            seen.add(nums[right]);
            if (right - left + 1> k) {
                seen.delete(nums[left]);
                left++;
            }

        }
        return false;
    }
}
