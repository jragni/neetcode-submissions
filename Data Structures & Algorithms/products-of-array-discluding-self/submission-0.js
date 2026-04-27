class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const ans = [];
        for (let i = 0; i < nums.length; i++) {
            let pre = i === 0 ? 1 : nums.slice(0,i)
                .reduce((acc, curr) => acc * curr, 1);
            let post = i === nums.lenght - 1 ? 1 : nums.slice(i+1)
                .reduce((acc, curr) => acc * curr, 1);

            ans.push(pre*post);
        }
        return ans;
    }
}
