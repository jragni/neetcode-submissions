class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        let left = 0;
        let right = matrix[0].length - 1;
        // check if it is in range
        let r = -1;


        for (let i = 0; i < matrix.length; i++) {
            if (
                target >= matrix[i][left]
                && target <= matrix[i][right]
            ) r = i
        }
        console.log(r)
        if (r === -1) return false

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            if (matrix[r][mid] === target) return true;
            if (matrix[r][mid] < target) left = mid + 1; 
            if (matrix[r][mid] > target) right = mid - 1; 
        }
        return false;
    }
}
