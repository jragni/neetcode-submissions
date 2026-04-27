class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = [];
        const compliment = {
            '{':'}',
            '(':')',
            '[':']',
        };
        
        if (s.length <= 1 || !(s[0] in compliment)) return false;
        stack.push(compliment[s[0]]);
        console.log('---first, ',stack);
        for (let i = 1; i < s.length; i++) {
            console.log('current', s[i], stack);
            if (s[i] in compliment)  stack.push(compliment[s[i]]);
            else if (s[i] !== stack.pop())  return false;
        }
        return !stack.length

    }
}
