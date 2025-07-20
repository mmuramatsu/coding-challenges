/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumLength = function (nums, k) {
    let dp = Array.from({ length: k }, () => Array(k).fill(0));
    let longest = 0;

    for (let num of nums) {
        let curr = num % k;

        for (let prev = 0; prev < k; prev++) {
            dp[curr][prev] = dp[prev][curr] + 1;
            longest = Math.max(longest, dp[curr][prev]);
        }
    }

    return longest;
};