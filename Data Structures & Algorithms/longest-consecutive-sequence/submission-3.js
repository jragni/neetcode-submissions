class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let longest = 0;
        let seen = new Set();
        for (let i = 0; i < nums.length; i++) {
            let curr = nums[i];
            if (seen.has(curr)) continue;
            seen.add(curr);
            let count = 1;
            while (nums.includes(curr+1)) {
                curr = curr + 1
                seen.add(curr);
                count++;
            }
            longest = Math.max(count, longest);
        }
        return longest;
    }
}
