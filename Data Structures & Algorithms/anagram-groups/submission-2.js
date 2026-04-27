class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        if (!strs.length) return [];
        const dict = {};
        for (const str of strs) {
            let sorted = [...str.split('')].sort().join('')
            if (sorted in dict) {
                dict[sorted].push(str);
            } else {
                dict[sorted] = [str];
            }
        }
        return Object.values(dict);
    }
}
