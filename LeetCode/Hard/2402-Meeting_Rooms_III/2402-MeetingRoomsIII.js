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
}

/**
 * @param {number} n
 * @param {number[][]} meetings
 * @return {number}
 */
var mostBooked = function (n, meetings) {
    meetings.sort((a, b) => a[0] - b[0]);

    let free_rooms = new HeapQueue((a, b) => a - b);
    let occupied_rooms = new HeapQueue((a, b) => {
        if (a[0] !== b[0]) {
            return a[0] - b[0];
        }
        return a[1] - b[1];
    });
    let rooms_count = new Array(n).fill(0);

    for (let i = 0; i < n; i++)
        free_rooms.push(i);

    for (let i = 0; i < meetings.length; i++) {
        let start_time = meetings[i][0];
        let end_time = meetings[i][1];

        while (!occupied_rooms.isEmpty() && occupied_rooms.peek()[0] <= start_time) {
            let tuple = occupied_rooms.peek();
            occupied_rooms.pop();
            free_rooms.push(tuple[1]);
        }

        if (!free_rooms.isEmpty()) {
            let room = free_rooms.peek();
            occupied_rooms.push([end_time, room]);
            rooms_count[room]++;
            free_rooms.pop();
        } else {
            let tuple = occupied_rooms.peek();
            occupied_rooms.pop();
            occupied_rooms.push([end_time + (tuple[0] - start_time), tuple[1]]);
            rooms_count[tuple[1]]++;
        }
    }

    return rooms_count.reduce((best, val, i) => val > rooms_count[best] ? i : best, 0);
};