class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let prod = 1;
        const res = [];
        for (const n of nums) {
            res.push(prod);
            prod *= n;
        }

        prod = 1;
        const post = [];
        for (let i = nums.length - 1; i >= 0; i--) {
           post.unshift(prod);
           prod *= nums[i];
        }

        for (let j = 0; j < nums.length; j++) {
            res[j] = res[j]* post[j];
        }

        return res

    }
}
