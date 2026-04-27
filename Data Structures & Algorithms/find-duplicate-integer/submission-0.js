class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findDuplicate(nums) {
        let set = new Set();
        for (const num of nums) {
            if (set.has(num)) {
                return num
            } else {
                set.add(num);
            }
        }
        return null;
    }
}
