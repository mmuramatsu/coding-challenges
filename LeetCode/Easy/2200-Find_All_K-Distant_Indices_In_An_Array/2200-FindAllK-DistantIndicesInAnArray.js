/**
 * @param {number[]} nums
 * @param {number} key
 * @param {number} k
 * @return {number[]}
 */
var findKDistantIndices = function (nums, key, k) {
    let ans = [];
    let n = nums.length;

    let right = 0;
    let left = 0;

    for (let i = 0; i < n; i++) {
        if (nums[i] == key) {
            left = Math.max(right, i - k);
            right = Math.min(n - 1, i + k) + 1;
            for (let idx = left; idx < right; idx++) {
                ans.push(idx);
            }
        }
    }

    return ans
};