const MOD = 1_000_000_007;
const MAX_N = 100_000;

let powers = new Array(MAX_N);

function precomputePowers() {
    powers[0] = 1;

    for (let i = 1; i <= MAX_N; i++) {
        powers[i] = (powers[i - 1] * 2) % MOD;
    }
}

precomputePowers();

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var numSubseq = function (nums, target) {
    let count = 0;

    nums.sort((a, b) => a - b);

    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        if (nums[left] + nums[right] <= target) {
            count += powers[right - left];
            left++;
        } else {
            right--;
        }
    }

    return count % MOD;
};