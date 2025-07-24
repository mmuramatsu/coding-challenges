class HeapQueue {
    constructor(cmp) {
        this.data = [];
        this.cmp = cmp;
    }

    push(value) {
        this.data.push(value);
        let i = this.data.length - 1;

        while (i > 0) {
            const parent = (i - 1) >> 1;
            if (this.cmp(this.data[i], this.data[parent]) < 0) {
                [this.data[i], this.data[parent]] = [this.data[parent], this.data[i]];
                i = parent;
            } else
                break;
        }
    }

    pop() {
        if (this.isEmpty()) {
            return undefined;
        }
        if (this.data.length === 1) {
            return this.data.pop();
        }

        const top = this.data[0];
        this.data[0] = this.data.pop();
        this._heapifyDown(0);
        return top;
    }

    _heapifyDown(i) {
        const n = this.data.length;

        while (true) {
            let l = 2 * i + 1;
            let r = 2 * i + 2;
            let minI = i;

            if (l < n && this.cmp(this.data[l], this.data[minI]) < 0)
                minI = l;
            if (r < n && this.cmp(this.data[r], this.data[minI]) < 0)
                minI = r;
            if (minI !== i) {
                [this.data[i], this.data[minI]] = [this.data[minI], this.data[i]]
                i = minI;
            } else
                break;
        }
    }

    peek() {
        if (this.isEmpty())
            return undefined;
        return this.data[0];
    }

    isEmpty() {
        return this.data.length === 0;
    }

    size() {
        return this.data.length
    }
}

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDifference = function (nums) {
    const n3 = nums.length;
    const n = Math.floor(n3 / 3);

    const min_heap = new HeapQueue((a, b) => a - b);
    const suffix_sum = new Array(n3).fill(0);
    let curr_sum = 0;

    for (let i = n3 - 1; i >= n - 1; --i) {
        min_heap.push(nums[i]);
        curr_sum += nums[i];

        if (min_heap.size() > n) {
            curr_sum -= min_heap.pop();
        }

        if (min_heap.size() === n) {
            suffix_sum[i] = curr_sum;
        }
    }

    const max_heap = new HeapQueue((a, b) => b - a);
    curr_sum = 0
    let ans = Infinity;

    for (let i = 0; i < 2 * n; ++i) {
        max_heap.push(nums[i]);
        curr_sum += nums[i];

        if (max_heap.size() > n) {
            curr_sum -= max_heap.pop();
        }

        if (max_heap.size() === n) {
            ans = Math.min(ans, curr_sum - suffix_sum[i + 1]);
        }
    }

    return ans;
};