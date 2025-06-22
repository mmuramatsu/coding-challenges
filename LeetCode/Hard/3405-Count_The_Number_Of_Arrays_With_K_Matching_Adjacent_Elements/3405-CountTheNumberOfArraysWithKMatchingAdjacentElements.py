from math import comb

MOD = (10**9) + 7
MAX_N = 10**5

factorial = [1] * (MAX_N + 1)
inv_factorial = [1] * (MAX_N + 1)

for i in range(1, MAX_N + 1):
    factorial[i] = (factorial[i - 1] * i) % MOD

inv_factorial[MAX_N] = pow(factorial[MAX_N], MOD - 2, MOD)

for i in range(MAX_N - 1, -1, -1):
    inv_factorial[i] = (inv_factorial[i + 1] * (i + 1)) % MOD


def nCr(n, r):
    if r < 0 or r > n:
        return 0

    return (factorial[n] * inv_factorial[r] * inv_factorial[n - r]) % MOD


class Solution:
    # Combinatronics + Modular Multiplicative Inverse solution. Beats 100%!
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        """
        Given `n`, `m` and `k`, our task is to find the number of good arrays we
        can form. A good array is an array of length `n`, with numbers in the
        range [1,m], where exists `k` pairs `array[i-1] == array[i]`.

        We can view this problem as a Stars and Bars problem. An array of `n`
        positions has `n-1` gaps where we can place a bar (imagine that between
        two positions of an array we can place a bar to separate this two
        elements.). So, if we need to find `k` pairs that has the same value, we
        can say that from n-1 gaps we need that k of these to has equal values.

        Let's ilustrate this with an example, a good array can be represented
        as:

            arr = [a,a,a|b,b|c,c,c]

        where, "," represent equal valeu gaps and "|" different value gaps. So,
        the idea is that we have `n-1` gaps and we need to find `n-1-k` gaps
        that are different or we can say `n-1-k` ways place our bars, which can
        be represented as the number of combinations of `n-1` elements picked
        `n-1-k` by `n-1-k` (C(n-1, n-1-k)).

        Now we need define which number will be in each streak of the array. We
        have `m` different possibilities for the first streak. The second, the
        third and so on, have `m-1` possibilities, since we cannot repeat the
        previous one.

        So, the final answer will b:

            ans = C(n-1, n-1-k) * m * (m-1)^(n-1-k)

        All right, now we need to find a way to calculate this in a fast way
        instead of use `math.comb`, because `math.comb(n-1, n-1-k)` can be
        really slow for a large `n`. Let's build a fast `comb` function.

        The problem lies when we want to calculate C(n, r) % MOD for a large `n`
        we cannot directly divide by r! or (n-r)! in modular arithmetic, so we
        going to use modular multiplicative inverses.

        The modular multiplicative inverse of a number A modulo M is a number
        A^(-1) such that:

            (A . A^(-1)) (mod M) = 1

        It's the same to the normal multiplication "X/A = X * A^(-1)". In
        modular arithmetic, if we want to "divide by A", we actually multiply by
        its modular inverse. To find "A^(-1) (mod M)", we use Fermat's Little
        Theorem, that states that if M is a prime number, then for any A not
        divisible by M we have:

            A^(M-1) (mod M) = 1

        multiplying both side by A^(-1):

            A^(M-2) (mod M) = A^(-1) (1)

        Based on that, we can rewrite the combination problem as:

            C(n, r) (mod MOD) = (n! . (r!)^(-1) . ((n-r)!)^(-1)) (mod MOD) (2)

        where (X!)^(-1) is the modular multiplicative inverse of X! modulo MOD.
        To make this really fast, we're going to precomputate the factorials and
        inverse factorials for all possible `n` value ([1, 10^5]).

        The factorials is easy, we just define a array with "10^5 + 1" positions,
        where each position will receive `(fact[i] = fact[i-1] * i) % MOD`. To
        calculate the inverse factorial, as we show in (1), we need to calculate

            (i!)^(-1) = i^(MOD - 2) (mod MOD)

        but this is also too slow, so let's use some math to make it easier.
        Let's represent factorial in that way:

            i! = (i+1)!
                -------
                 (i+1)

        So,

            (i!)^(-1) =   (i+1)!
                        ----------
                        (i+1)^(-1)
            (i!)^(-1) = (i+1)!^(-1) . (i+1)

        To precompute the inverse factorial we gonna first calculate the inverse
        factorial for `n=10^5` by doing `pow(fact[10^5], MOD - 2, MOD)`. Then we
        iterate from (10^5)-1 to down to 0 doing `(inv_fact[i+1] * (i+1)) % MOD`

        So, to calculate the C(n-1, n-k-1), we define a function `nCr`, that
        receive two parameters `n` and `r` and calculate (2), by doing
        `(fact[n] * inv_fact[r] * inv_fact[n - r]) % MOD`. If `r<0` or `r>n`, we
        return 0, because it's impossible to form combinations in this
        situations.

        OBS: The precomputations are made out of the Solution class to avoid
        redoing the precomputations. LeetCode typically instantiates our
        Solution class once per submission, and then calls our main solving
        method for each test case. In our case, the function `nCr` runs in O(1)
        time and the precomputations are done once, giving us a pretty fast
        solution!
        """
        # More equal gaps than the number of gaps available is impossible.
        if k > n - 1:
            return 0

        # If m==1, then the number of equal gaps need to be equal to the number
        # of gaps available, otherwise, it's impossible.
        if m == 1:
            return 1 if k == n - 1 else 0

        return (nCr(n - 1, n - k - 1) * m * pow(m - 1, n - 1 - k, MOD)) % MOD

    # Combinatronics solution. Beats 14.06%.
    def countGoodArrays1(self, n: int, m: int, k: int) -> int:
        """
        Given `n`, `m` and `k`, our task is to find the number of good arrays we
        can form. A good array is an array of length `n`, with numbers in the
        range [1,m], where exists `k` pairs `array[i-1] == array[i]`.

        We can view this problem as a Stars and Bars problem. An array of `n`
        positions has `n-1` gaps where we can place a bar (imagine that between
        two positions of an array we can place a bar to separate this two
        elements.). So, if we need to find `k` pairs that has the same value, we
        can say that from n-1 gaps we need that k of these to has equal values.

        Let's ilustrate this with an example, a good array can be represented
        as:

            arr = [a,a,a|b,b|c,c,c]

        where, "," represent equal valeu gaps and "|" different value gaps. So,
        the idea is that we have `n-1` gaps and we need to find k gaps that
        equal, which can be represented as the number of combinations of `n-1`
        elements picked k by k (C(n-1, k)).

        Now we need define which number will be in each streak of the array. We
        have `m` different possibilities for the first sequence. The second, the
        third and so on, have `m-1` possibilities, since we cannot repeat the
        previous one.

        So, the final answer will b:

            ans = C(n-1, k) * m * (m-1)^(n-1-k)
        """
        if k > n - 1:
            return 0

        MOD = (10**9) + 7

        return (comb(n - 1, k) * m * ((m - 1) ** (n - k - 1))) % MOD


a = Solution()
print(a.countGoodArrays(n=3, m=2, k=1))
print(a.countGoodArrays(n=4, m=2, k=2))
print(a.countGoodArrays(n=5, m=2, k=0))
print(a.countGoodArrays(n=1, m=1, k=0))
print(a.countGoodArrays(n=2, m=1, k=0))
