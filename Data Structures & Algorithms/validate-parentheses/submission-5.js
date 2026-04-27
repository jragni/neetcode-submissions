class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        if (!s.length) return true;
        if (s.length === 1) return false;
        const openDict = {
            '{': '}',
            '(': ')',
            '[': ']',
        }; // [openBrace]: closeBrace
        const stack = [];

        for (const char of s) {
            if (char in openDict) {
                stack.push(openDict[char]);
            } else {
                if (char === stack.at(-1)) stack.pop();
                else return false
            }
        }
        return !stack.length;
    }
}
