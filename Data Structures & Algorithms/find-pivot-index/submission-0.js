class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    pivotIndex(nums) {
        if (!nums.length) return -1;
        if (nums.length <= 1) return 0;

        // calculate prefix
        const pre = Array(nums.length).fill(0);
        let preSum = 0;

        for (let i = 0; i < nums.length; i++) {
            pre[i] = i > 0 ? preSum : 0;
            preSum += nums[i];
        }
        // calculate post fix
        const post = Array(nums.length).fill(0);
        let postSum = 0;
        for (let j = nums.length - 1; j >= 0; j--) {
            post[j] = j < nums.length - 2 ? postSum : 0;
            postSum += nums[j];
        }

        console.log(post, pre)
        // compare and walk 
        for (let k = 0; k < nums.length; k++) {
            if (post[k] === pre[k]) return k;
        }
        return -1;
    }
}
