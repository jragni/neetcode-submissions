class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let longest = 0;
        for (let i = 0; i < nums.length; i++) {
            let curr = nums[i];
            let count = 1;
            while (nums.includes(curr+1)) {
                curr = curr + 1
                count++;
            }
            longest = Math.max(count, longest);
        }
        return longest;
    }
}
