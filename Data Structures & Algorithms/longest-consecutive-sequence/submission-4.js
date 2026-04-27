class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let longest = 0;
        for (const num of nums) {
            let count = 1;
            let curr = num;
            while (nums.includes(curr+1)) {
                curr = curr + 1
                count++;
            }
            longest = Math.max(count, longest);
        }
        return longest;
    }
}
