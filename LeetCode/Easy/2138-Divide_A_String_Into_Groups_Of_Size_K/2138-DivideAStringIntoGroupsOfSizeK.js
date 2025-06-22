/**
 * @param {string} s
 * @param {number} k
 * @param {character} fill
 * @return {string[]}
 */
var divideString = function (s, k, fill) {
    let n = s.length;

    if (n % k != 0) {
        s = s + fill.repeat(k - (n % k));
    }

    let ans = [];

    for (let i = 0; i < s.length; i += k) {
        ans.push(s.substring(i, i + k));
    }

    return ans
};