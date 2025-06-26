/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubsequence = function (s, k) {
    let length = 0;
    let power = 0n;
    let num = 0n;

    for (let i = s.length - 1; i >= 0; i--) {
        if (s[i] == '1') {
            if (power < 32n && (num + (1n << power)) <= BigInt(k)) {
                length++;
                num = num + (1n << power);
            }

        } else {
            length++;
        }

        power++;
    }

    return length
};