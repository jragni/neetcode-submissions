class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        // calculate postfix product
        let pre = Array(nums.length).fill(1);
        let preProd = 1;

        for (let i = 0; i < pre.length; i++) {
            pre[i] = preProd; 
            preProd *= nums[i];
        }

        let postProd = 1;
        for (let j = pre.length - 1; j >= 0; j--) {
            pre[j] *= postProd;
            postProd *= nums[j];
        }

        return pre;
    }
}
