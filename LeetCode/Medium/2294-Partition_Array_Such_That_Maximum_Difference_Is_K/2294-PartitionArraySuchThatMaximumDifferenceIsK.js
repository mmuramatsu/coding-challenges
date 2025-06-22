/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var partitionArray = function (nums, k) {
    nums.sort((a, b) => a - b);

    let ans = 1;
    let max_value = nums[0] + k;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > max_value) {
            ans++;
            max_value = nums[i] + k;
        }
    }

    return ans;
};