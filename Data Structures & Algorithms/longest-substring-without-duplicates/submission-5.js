class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let longest = 0;
        let seen = new Set();
        let right = 0;
        let left = 0;
        while (right < s.length) {
            while (seen.has(s[right])) {
                seen.delete(s[left]);
                left++; 
            }
            seen.add(s[right]);
            longest = Math.max(longest, right - left + 1);
            right++;
        }
        return longest;
    }
}
