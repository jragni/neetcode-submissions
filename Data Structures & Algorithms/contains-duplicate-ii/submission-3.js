class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     */
    containsNearbyDuplicate(nums, k) {
        // initialize a seen variable
        const seen = new Set();
        // get the initial window
        // for 0 -> k (inclusive) 
            // if the current value is in seen
                // return true
            // add current element to seen
        for (let i = 0; i <= k; i++) {
            if (seen.has(nums[i])) {
                return true;
            }
            seen.add(nums[i]);
        }
        
        // set left to 0;
        // set right to k+1
        let left = 0;
        let right = k;
        
        // loop through values from right to end
            // if right in seen 
                // return true
            // add current to seen
            // remove left
            // increment left and right
        while (right < nums.length) {
            seen.delete(nums[left]);
            right++;
            if (seen.has(nums[right])) return true;
            seen.add(nums[right]);
            left++;
        }
        return false;
    }
}
