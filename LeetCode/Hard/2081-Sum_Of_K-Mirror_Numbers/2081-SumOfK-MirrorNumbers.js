var to_base_k = function (num, base) {
    if (num == 0) return "0";

    let base_k = [];

    while (num > 0) {
        base_k.push(String.fromCharCode((num % base) + '0'.charCodeAt(0)));
        num = Math.floor(num / base);
    }

    return base_k.reverse().join('');
}

var is_palindrome = function (s) {
    return s == s.split('').reverse().join('');
}

var create_palindrome = function (num, odd) {
    let x = num;
    // Discart the last digit
    if (odd) x = Math.floor(x / 10);

    while (x > 0) {
        num = num * 10 + x % 10;
        x = Math.floor(x / 10);
    }

    return num;
}

/**
 * @param {number} k
 * @param {number} n
 * @return {number}
 */
var kMirror = function (k, n) {
    let ans = 0;

    for (let range = 1; n > 0; range *= 10) {
        for (let i = range; n > 0 && i < range * 10; i++) {
            const palindrome = create_palindrome(i, true);
            const base_k = to_base_k(palindrome, k)

            if (is_palindrome(base_k)) {
                n--;
                ans += palindrome;
            }
        }

        for (let i = range; n > 0 && i < range * 10; i++) {
            const palindrome = create_palindrome(i, false);
            const base_k = to_base_k(palindrome, k)

            if (is_palindrome(base_k)) {
                n--;
                ans += palindrome;
            }
        }
    }

    return ans;
};