var bisect_right = function (arr, x, lo = 0, hi = arr.length) {
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);

        if (x < arr[mid])
            hi = mid;
        else
            lo = mid + 1
    }
    return lo
}

/**
 * @param {number[][]} events
 * @param {number} k
 * @return {number}
 */
var maxValue = function (events, k) {
    let n = events.length;
    events.sort((a, b) => a[0] - b[0])

    let memo = Array.from({ length: n }, () => Array.from({ length: k + 1 }).fill(-1));
    let start_days = events.map(e => e[0]);
    let next_event = Array(n).fill(0);

    for (let i = 0; i < n; i++)
        next_event[i] = bisect_right(start_days, events[i][1], i + 1);

    var solve = function (events, event_idx, k) {
        if (k == 0 || event_idx >= n)
            return 0;

        if (memo[event_idx][k] != -1)
            return memo[event_idx][k];

        let skip = solve(events, event_idx + 1, k);
        let attend = solve(events, next_event[event_idx], k - 1) + events[event_idx][2];

        memo[event_idx][k] = Math.max(skip, attend);

        return memo[event_idx][k];
    }

    return solve(events, 0, k);
};