class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (!s.length && !t.length) return true;
        if (s.length !== t.length) return false;

        const _getCounts = (str) => {
            const counts = {};
            for (const char of str) {
                if (char in counts) {
                    counts[char] += 1;
                } else {
                    counts[char] = 1;
                }
            }
            return counts;
        };

        const sCounts = _getCounts(s);
        const tCounts = _getCounts(t);
        for (let [char, count] of Object.entries(sCounts)) {
            if (count !== tCounts[char]) return false;
        }
        return true;
    }
}
