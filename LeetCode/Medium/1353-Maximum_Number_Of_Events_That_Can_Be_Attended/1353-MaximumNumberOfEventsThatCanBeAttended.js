/**
 * @param {number[][]} events
 * @return {number}
 */
var maxEvents = function (events) {
    let n = events.length;
    let count = 0;
    let day = 0;
    let j = 0;
    let available = new MinPriorityQueue();

    events.sort((a, b) => a[0] - b[0]);

    while (j < n || !available.isEmpty()) {
        if (available.isEmpty() && j < n)
            day = Math.max(day, events[j][0]);

        while (j < n && events[j][0] == day) {
            available.enqueue(events[j][1]);
            j++;
        }

        while (!available.isEmpty() && available.front() < day)
            available.dequeue();

        if (!available.isEmpty()) {
            available.dequeue();
            count++;
            day++;
        }
    }

    return count;
};