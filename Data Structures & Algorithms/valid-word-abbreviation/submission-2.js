class Solution {
    /**
     * @param {string} word
     * @param {string} abbr
     * @return {boolean}
     */
    validWordAbbreviation(word, abbr) {
        if (!word.length) return false;
        // Loop through the string
        let i = 0;
        let count = 0;
        while (i < abbr.length) {
            // check if the current letter is a number or a stringof a number
            let current = abbr[i];
            if (typeof Number(current) === 'number' && !Number.isNaN(Number(current))) {
                if (current == 0) return false;
                let j = i;
                while (typeof Number(abbr[j]) === 'number' && !Number.isNaN(Number(abbr[j]))) {
                    j++;
                }
                let addNumber = Number(abbr.slice(i, j));
                count += addNumber;
                i = j;
                if (word[count] !== abbr[i]) return false;
            } else {
                count++;
                i++;
            }
        }
        return word.length === count;
    }
}
