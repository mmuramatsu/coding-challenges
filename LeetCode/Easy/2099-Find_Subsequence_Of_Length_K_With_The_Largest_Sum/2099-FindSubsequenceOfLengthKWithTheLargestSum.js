/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSubsequence = function (nums, k) {
    const indexedNums = nums.map((num, i) => ({ num, originalIndex: i }));

    const greatest = indexedNums
        .sort((a, b) => b.num - a.num) // Sort descending by number
        .slice(0, k); // Take the top k elements

    const idxGreatest = greatest.sort((a, b) => a.originalIndex - b.originalIndex);

    const ans = idxGreatest.map(item => item.num);

    return ans;
};