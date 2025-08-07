var remove = function (s, sub) {
    let stack = [];

    for (let c of s) {
        if (c == sub[1] && stack.length && stack.at(-1) == sub[0])
            stack.pop();
        else
            stack.push(c);
    }

    return stack;
};

/**
 * @param {string} s
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var maximumGain = function (s, x, y) {
    let ans = 0;
    let first;
    let second;
    if (y > x) {
        first = "ba";
        second = "ab";
    }
    else {
        first = "ab";
        second = "ba";
    }

    let new_s = remove(s, first);
    ans += ((s.length - new_s.length) / 2) * Math.max(x, y);
    ans += ((new_s.length - remove(new_s, second).length) / 2) * Math.min(x, y);

    return ans;
};