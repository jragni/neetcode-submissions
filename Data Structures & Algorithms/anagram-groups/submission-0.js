class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        // create an array of sorted strings
        const sorted = strs.map(str =>  str.split('').sort());
        const dict = {};
        for (let i = 0; i < sorted.length; i++) {
           if (sorted[i] in dict) dict[sorted[i]].push(strs[i]);
           else dict[sorted[i]] = [strs[i]];
        }
        return Object.values(dict).sort((a,b) => a[0].length - b[0].length);
    }
}
