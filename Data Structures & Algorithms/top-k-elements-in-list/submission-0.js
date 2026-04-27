class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const _counter = (nums) => {
            const counts = {};
            for (const num of nums) {
                if (num in counts) counts[num]++;
                else counts[num] = 1;
            }
            return counts;
        }
        const countEntries = Object.entries(_counter(nums)).sort((a,b) => a[1] - b[1]);
        let solution = [];
        for (let i = 0; i < k; i++) {
            solution.push(countEntries[countEntries.length - 1][0]);
            countEntries.pop();
        }
        return solution;
    }
}
