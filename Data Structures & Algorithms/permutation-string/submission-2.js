class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        if (s1.length > s2.length) return false;

        let right = 0;
        let left = 0;
        let s1Counts = s1.split('').reduce((acc, curr) => {
            acc[curr] = curr in acc ? acc[curr] + 1 : 1;
            return acc;
        }, {});
        while (right < s2.length) {
            let s1Copy = {...s1Counts};
            while (s2[right] in s1Copy) {
                if (s1Copy[s2[right]] < 0) break;
                s1Copy[s2[right]]--;
                if (Object.values(s1Copy).every(val => val === 0)) return true;
                right++;
            }
            left++;
            right = left;

        }
        return false;
    }
}
