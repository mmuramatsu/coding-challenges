/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 */
var FindSumPairs = function (nums1, nums2) {
    this.nums2 = nums2;

    this.freq1 = new Map();
    for (const num of nums1) {
        this.freq1.set(num, (this.freq1.get(num) || 0) + 1);
    }

    this.freq2 = new Map();
    for (const num of nums2) {
        this.freq2.set(num, (this.freq2.get(num) || 0) + 1);
    }

    this.keys = Array.from(this.freq1.keys());
    this.keys.sort(function (a, b) { return a - b; });
};

/**
 * @param {number} index
 * @param {number} val
 * @return {void}
 */
FindSumPairs.prototype.add = function (index, val) {
    const oldVal = this.nums2[index];
    this.freq2.set(oldVal, this.freq2.get(oldVal) - 1);

    this.nums2[index] += val;
    const newVal = this.nums2[index];
    this.freq2.set(newVal, (this.freq2.get(newVal) || 0) + 1);
};

/**
 * @param {number} tot
 * @return {number}
 */
FindSumPairs.prototype.count = function (tot) {
    let count = 0;

    for (let k of this.keys) {
        if (k >= tot)
            break;

        if (this.freq2.has(tot - k)) {
            count += this.freq1.get(k) * this.freq2.get(tot - k);
        }
    }

    return count;
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * var obj = new FindSumPairs(nums1, nums2)
 * obj.add(index,val)
 * var param_2 = obj.count(tot)
 */