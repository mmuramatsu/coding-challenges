/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumLength = function (nums) {
    let odd = 0;
    let even = 0;
    let alternate_even = 0;
    let alternate_odd = 0;
    let next_even = true;
    let next_odd = true;

    for (let num of nums) {
        if (num & 1) {
            // Odd
            odd += 1;
            if (next_odd) {
                alternate_odd += 1;
                next_odd = false;
            }

            if (!next_even) {
                alternate_even += 1;
                next_even = true;
            }
        } else {
            // Even
            even += 1;

            if (next_even) {
                alternate_even += 1;
                next_even = false;
            }

            if (!next_odd) {
                alternate_odd += 1;
                next_odd = true;
            }
        }
    }

    return Math.max(...[even, odd, alternate_even, alternate_odd]);
};