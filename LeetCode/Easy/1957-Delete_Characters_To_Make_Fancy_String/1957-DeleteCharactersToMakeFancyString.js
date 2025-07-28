/**
 * @param {string} s
 * @return {string}
 */
var makeFancyString = function (s) {
    if (s.length < 3)
        return s;

    let prev = s[0];
    let count = 1;
    let ans = s[0];

    for (let i = 1; i < s.length; i++) {
        if (prev == s[i])
            count++;
        else
            count = 1;

        if (count < 3)
            ans += s[i]

        prev = s[i];
    }

    return ans;
};