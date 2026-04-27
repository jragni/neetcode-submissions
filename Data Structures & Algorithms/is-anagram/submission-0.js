class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;
        let _counter = (str) => {
            const counts = {};
            for (const char of str) {
                if (char in counts) counts[char]++;
                else counts[char] = 1;
            }
            return counts;
        }
        let sCounts = _counter(s);
        let tCounts = _counter(t);
        for (const char of s) {
            if (sCounts[char] !== tCounts[char]) return false;
        }
        return true;
    }
}
