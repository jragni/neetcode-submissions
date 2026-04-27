class Solution {
    /**
     * @param {number[]} arr
     * @param {number} k
     * @param {number} threshold
     * @return {number}
     */
    numOfSubarrays(arr, k, threshold) {
        let sum = 0;    
        let left = 0;
        let count = 0;
        for (let i = 0; i < k; i++) {
            sum += arr[i];
        }
        if (sum / k >= threshold) count++;
        let right = k;
        while (right < arr.length) {
            sum += arr[right] - arr[left];
            if (sum / k >= threshold) count++;
            right++;
            left++;
        }
        return count;
    }
}
