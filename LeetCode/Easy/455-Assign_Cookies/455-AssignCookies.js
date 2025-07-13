/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function (g, s) {
    let n = g.length;
    let m = s.length;

    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);

    let j = 0;
    let count = 0;

    for (let i = 0; i < n; i++) {
        while (j < m && g[i] > s[j])
            j++;

        if (j < m) {
            count++;
            j++;
        } else
            break;
    }

    return count;
};