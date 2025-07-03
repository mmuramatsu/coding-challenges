const MOD = 1_000_000_007;

/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var possibleStringCount = function (word, k) {
    let groups = [];
    let count = 1;

    for (let i = 1; i < word.length; i++) {
        if (word[i - 1] == word[i]) {
            count++;
        } else {
            groups.push(count);
            count = 1;
        }
    }

    groups.push(count);

    let total = 1;

    for (let size of groups) {
        total = (total * size) % MOD;
    }

    if (groups.length >= k)
        return total;

    let prefix_sum = new Array(k).fill(1);
    let dp;

    for (let size of groups) {
        dp = new Array(k).fill(0);

        for (let len = 1; len < k; len++) {
            dp[len] = prefix_sum[len - 1];

            if (len - size - 1 >= 0)
                dp[len] = (dp[len] - prefix_sum[len - size - 1] + MOD) % MOD;
        }

        prefix_sum = new Array(k).fill(0);

        for (let i = 1; i < k; i++) {
            prefix_sum[i] = (prefix_sum[i - 1] + dp[i]) % MOD;
        }
    }

    return (total - prefix_sum[k - 1] + MOD) % MOD;
};