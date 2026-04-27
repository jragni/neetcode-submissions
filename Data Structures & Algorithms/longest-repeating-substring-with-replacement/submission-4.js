class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let longest = 0;
        let left = 0;
        let maxf = 0;
        const freq = {};
        for (let right = 0; right < s.length; right++) {
            freq[s[right]] = s[right] in freq ? freq[s[right]] + 1 : 0;
            maxf = Math.max(maxf, freq[s[right]]);
            // window condition
            while (right - left - maxf > k) {
                freq[s[left]]--;
                left++;
            }
            longest = Math.max(right - left + 1, longest);
        }

        return longest;
    }
}
