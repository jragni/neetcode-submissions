class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs) {
        if (!strs.length) return "";
        // find smallest string
        let smallest = strs[0];
        for (let i = 0; i < strs.length; i++) {
            if (smallest.length > strs[i].length) smallest = strs[i];
        }

        // loop through smallest i = 0 -> length of smallest
        for (let i = 0; i < smallest.length; i++) {
            // if it doesnt equal return slice of smallest 0 -> i
            for (let str of strs) {
                if (str[i] !== smallest[i]) {
                   return str.slice(0, i) ;
                }
            }
        }
        // return  smallest
        return smallest;
    }
}
