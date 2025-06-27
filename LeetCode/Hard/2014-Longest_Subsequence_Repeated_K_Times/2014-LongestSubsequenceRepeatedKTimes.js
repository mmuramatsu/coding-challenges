var is_subsequence = function (s, subseq, k) {
    let i = 0;
    let j = 0;

    while (i < s.length) {
        if (s[i] == subseq[j]) {
            j++;

            if (j == subseq.length) {
                j = 0;
                k--;

                if (k == 0)
                    return true;
            }
        }
        i++;
    }

    return false;
}


/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var longestSubsequenceRepeatedK = function (s, k) {
    const freq = new Map();

    for (const char of s) {
        freq.set(char, (freq.get(char) || 0) + 1);
    }

    const possible_chars = [];

    for (const [key, value] of freq) {
        if (value >= k)
            possible_chars.push(key)
    }

    possible_chars.sort();

    let queue = [""];
    let ans;

    while (queue.length != 0) {
        let curr_subseq = queue.shift();
        ans = curr_subseq;

        for (let c of possible_chars) {
            let candidate = curr_subseq + c;
            if (is_subsequence(s, candidate, k))
                queue.push(candidate);
        }
    }

    return ans
};