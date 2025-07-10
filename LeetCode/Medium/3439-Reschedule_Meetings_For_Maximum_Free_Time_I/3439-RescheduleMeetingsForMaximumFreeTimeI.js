/**
 * @param {number} eventTime
 * @param {number} k
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @return {number}
 */
var maxFreeTime = function (eventTime, k, startTime, endTime) {
    startTime.push(eventTime);
    endTime.unshift(0);

    let gaps = [];
    const n = startTime.length;

    for (let i = 0; i < n; i++)
        gaps.push(startTime[i] - endTime[i]);

    let left = 0;
    let max_free_time = 0;
    let curr_free_time = 0;

    for (let i = 0; i < k; i++)
        curr_free_time += gaps[i];

    for (let right = k; right < n; right++) {
        curr_free_time += gaps[right];
        max_free_time = Math.max(max_free_time, curr_free_time);
        curr_free_time -= gaps[left];
        left++;
    }

    return max_free_time;
};