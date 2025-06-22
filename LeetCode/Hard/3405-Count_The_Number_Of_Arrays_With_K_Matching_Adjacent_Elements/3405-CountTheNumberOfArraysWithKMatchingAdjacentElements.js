// BigInt literals are created by appending 'n' to an integer.
const MOD = 1_000_000_007n;
const MAX_N = 100_000n;

let factorial = new Array(Number(MAX_N) + 1);
let invFactorial = new Array(Number(MAX_N) + 1);

/**
 * @param {bigint} base
 * @param {bigint} exp
 * @param {bigint} mod
 * @returns {bigint}
 */
function modPow(base, exp, mod) {
    let res = 1n;
    base %= mod

    while (exp > 0n) {
        if (exp % 2n === 1n) {
            res = (res * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2n;
    }
    return res;
}

function precomputeFactorials() {
    factorial[0] = 1n;

    for (let i = 1; i <= Number(MAX_N); i++) {
        factorial[i] = (factorial[i - 1] * BigInt(i)) % MOD;
    }
}

function precomputeInvFactorials() {
    invFactorial[Number(MAX_N)] = modPow(factorial[Number(MAX_N)], MOD - 2n, MOD);

    for (let i = Number(MAX_N) - 1; i >= 0; i--) {
        invFactorial[i] = (invFactorial[i + 1] * BigInt(i + 1)) % MOD;
    }
}

precomputeFactorials();
precomputeInvFactorials();


/**
 * @param {number} n_num
 * @param {number} r_num
 * @returns {bigint}
 */
function nCr(n_num, r_num) {

    if (r_num < 0 || r_num > n_num) {
        return 0n;
    }

    let numerator_term = factorial[n_num];
    let inv_r_factorial_term = invFactorial[r_num];
    let inv_n_minus_r_factorial_term = invFactorial[n_num - r_num];

    let result = (numerator_term * inv_r_factorial_term) % MOD;
    result = (result * inv_n_minus_r_factorial_term) % MOD;

    return result;
}

/**
 * @param {number} n
 * @param {number} m
 * @param {number} k
 * @return {number}
*/
var countGoodArrays = function (n, m, k) {
    if (k > n - 1) return 0;

    if (m === 1) return (k === n - 1) ? 1 : 0;


    let combinations = nCr(n - 1, n - 1 - k);
    let powerVal = modPow(m - 1, n - 1 - k, MOD);

    let ans = (combinations * m) % MOD;
    ans = (ans * powerVal) % MOD;

    return Number(ans);
}