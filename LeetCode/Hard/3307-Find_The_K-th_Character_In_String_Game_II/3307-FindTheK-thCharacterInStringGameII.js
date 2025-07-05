/**
 * @param {number} k
 * @param {number[]} operations
 * @return {character}
 */
var kthCharacter = function (k, operations) {
    let t = 0;
    let current_len = 1;
    k--;

    while (current_len <= k) {
        current_len *= 2
        t++;
    }

    let final_char = 97;

    while (current_len > 1) {
        current_len /= 2;
        t--;

        if (k >= current_len) {
            k -= current_len;

            if (operations[t] == 1)
                final_char++;

            if (final_char > 122)
                final_char = 97;
        }
    }

    return String.fromCharCode(final_char)
};