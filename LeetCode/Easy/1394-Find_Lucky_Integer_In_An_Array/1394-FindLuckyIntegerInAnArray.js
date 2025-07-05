/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function (arr) {
    let freq = new Map();

    for (let num of arr)
        freq.set(num, (freq.get(num) || 0) + 1);

    let ans = -1;

    for (let [k, v] of freq) {
        if (k == v && k > ans)
            ans = k;
    }

    return ans;
};