class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const dict = {
            '(':')',
            '{':'}',
            '[':']',
        };
        const stack = [];
        for (const char of s) {
            if (char in dict) stack.push(dict[char]);
            else {
                if(stack.at(-1) !== char) return false;
                stack.pop();
            }
        }
        return stack.length === 0;
    }
}
