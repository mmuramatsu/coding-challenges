var split = function (nums) {
    let pos = [];
    let neg = [];

    for (let num of nums) {
        if (num < 0)
            neg.push(-num);
        else
            pos.push(num);
    }

    neg.reverse();
    return [pos, neg];
}

var count_products = function (A, B, m) {
    let count = 0n;
    let j = BigInt(B.length) - 1n;

    for (let num of A) {
        while (j >= 0n && BigInt(num) * BigInt(B[j]) > m) {
            j--;
        }

        count += j + 1n;
    }

    return count;
}

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var kthSmallestProduct = function (nums1, nums2, k) {
    let A1, A2, B1, B2;

    pair = split(nums1);
    A1 = pair[0];
    A2 = pair[1];

    pair = split(nums2);
    B1 = pair[0];
    B2 = pair[1];

    let count_negative = A1.length * B2.length + A2.length * B1.length;
    let sign = 1;

    if (k > count_negative) {
        k -= count_negative;
    } else {
        k = count_negative - k + 1;
        sign = -1;
        [B1, B2] = [B2, B1];
    }

    let left = 0n;
    let right = 10000000000n;

    while (left < right) {
        let mid = (left + right) / 2n;

        if (count_products(A1, B1, mid) + count_products(A2, B2, mid) >= BigInt(k)) {
            right = mid;
        } else {
            left = mid + 1n;
        }
    }

    return sign * Number(left);
};