/**
 * @param {number} eventTime
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @return {number}
 */
var maxFreeTime = function (eventTime, startTime, endTime) {
    startTime.push(eventTime);
    endTime.unshift(0);

    let gaps = [];
    const m = startTime.length;

    for (let i = 0; i < m; i++)
        gaps.push(startTime[i] - endTime[i]);

    let sorted_gaps = [...gaps];
    sorted_gaps.sort((a, b) => a - b);

    let meetings = [];

    for (let i = 1; i < m; i++)
        meetings.push(endTime[i] - startTime[i - 1]);

    const n = meetings.length;
    let j = 1;
    let max_free_time = 0;
    let curr_free_time = 0;

    for (let duration of meetings) {
        let founded = false;
        let equal_left = true;
        let equal_right = true;

        for (let i = m - 1; i >= 0 && i >= m - 4; i--) {
            if (sorted_gaps[i] >= duration) {
                if (equal_left && sorted_gaps[i] == gaps[j - 1]) {
                    equal_left = false;
                }
                else if (equal_right && sorted_gaps[i] == gaps[j]) {
                    equal_right = false;
                }
                else {
                    founded = true;
                    break;
                }
            }
        }

        if (founded)
            curr_free_time = gaps[j - 1] + duration + gaps[j];
        else
            curr_free_time = gaps[j - 1] + gaps[j];

        max_free_time = Math.max(max_free_time, curr_free_time);

        j += 1;
    }

    return max_free_time
};