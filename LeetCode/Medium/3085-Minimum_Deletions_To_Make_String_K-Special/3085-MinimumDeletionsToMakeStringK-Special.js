/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var minimumDeletions = function (word, k) {
    const freq = {};

    for (const char of word) {
        freq[char] = (freq[char] || 0) + 1;
    }

    let ans = Number.MAX_SAFE_INTEGER;

    for (const [_, x] of Object.entries(freq)) {
        let deletions = 0;
        for (const [_, y] of Object.entries(freq)) {
            if (x > y) {
                deletions += y;
            } else if (y > x + k) {
                deletions += y - (x + k);
            }
        }

        ans = Math.min(ans, deletions);
    }

    return ans
};