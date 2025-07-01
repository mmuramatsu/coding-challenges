/**
 * @param {number[]} nums
 * @return {number}
 */
var findLHS = function (nums) {
    let freq = new Map();

    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    let ans = 0;

    for (const [k, v] of freq) {
        if (freq.has(k + 1)) {
            ans = ans > v + freq.get(k + 1) ? ans : v + freq.get(k + 1);
        }
    }

    return ans;
};