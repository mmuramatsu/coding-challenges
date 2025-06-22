/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxDistance = function (s, k) {
    let ans = 0;
    let north = 0,
        south = 0,
        east = 0,
        west = 0;

    for (let i = 0; i < s.length; i++) {
        switch (s[i]) {
            case "N":
                north++;
                break;
            case "S":
                south++;
                break;
            case "E":
                east++;
                break;
            case "W":
                west++;
                break;
        }

        let conflicts = Math.min(north, south) + Math.min(east, west);

        let max_distance = i + 1;

        if (k < conflicts) max_distance = max_distance - (conflicts * 2) + (k * 2);

        ans = Math.max(ans, max_distance);
    }

    return ans
};