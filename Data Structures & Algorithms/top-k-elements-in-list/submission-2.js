class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
       const counts = {};
       for (let num of nums) {
            if (num in counts) {
                counts[num]++;
            } else {
                counts[num] = 1;
            }
       }
       let entries = Object.entries(counts).sort((a,b)=>a[1] - b[1]);
       console.log(entries);
       const solution = [];
       while (k > 0) {
        solution.push(entries.pop()[0]);
        k--;
       }
       return solution;
    }
}
