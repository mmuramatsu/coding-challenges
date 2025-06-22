const int MOD=1e9+7;
const int MAX_N=1e5;

std::vector<long long> factorial(MAX_N + 1);
std::vector<long long> inv_factorial(MAX_N + 1);

long long modPow(long long x, unsigned exp) {
    long long res = 1;
    x %= MOD;

    while (exp > 0) {
        if (exp & 1) res = (res * x) % MOD;
        x = (x * x) % MOD;
        exp /= 2 ;
    }

    return res;
}

void precompute_factorials() {
    factorial[0] = 1;

    for (int i = 1; i < MAX_N + 1; i++) {
        factorial[i] = (factorial[i-1] * i) % MOD;
    }
}

void precompute_inv_factorials() {
    inv_factorial[MAX_N] = modPow(factorial[MAX_N], MOD - 2);

    for (int i = MAX_N - 1; i >= 0 ; i--) {
        inv_factorial[i] = (inv_factorial[i+1] * (i+1)) % MOD;
    }
}

struct PrecomputationInitializer {
    PrecomputationInitializer() {
        precompute_factorials();
        precompute_inv_factorials();
    }
};

static PrecomputationInitializer initializer;

class Solution {
public:

    static long long nCr(int n, int r) {
        if (r < 0 or r > n) return 0;

        long long numerator = factorial[n];
        long long denominator = (inv_factorial[r] * inv_factorial[n - r]) % MOD;

        return (numerator * denominator) % MOD;
    }

    int countGoodArrays(int n, int m, int k) {
        if (k > n - 1) return 0;

        if (m == 1) return k == n-1 ? 1 : 0;

       // Calculate combinations C(n-1, n-k-1)
        long long comb = nCr(n - 1, n - k - 1);

        // Calculate (m - 1)^(n - 1 - k) modulo MOD
        long long power = modPow(m - 1, n - 1 - k);

        //  C(...) * m * (m-1)^(...) % MOD
        long long ans = (comb * m) % MOD;
        ans = (ans * power) % MOD;

        return static_cast<int>(ans); // Cast back to int if return type is int
    }
};