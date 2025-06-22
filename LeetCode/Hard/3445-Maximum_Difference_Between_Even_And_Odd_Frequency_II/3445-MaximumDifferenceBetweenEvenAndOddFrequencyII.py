class Solution:
    # Enumeration + Prefix-sum + Sliding windo solution. Beats 81.64%.
    def maxDifference(self, s: str, k: int) -> int:
        """
        Given a string `s` and a integer `k`, our task is to find, in a
        substring `subs` of length at least `k`, the maximum difference between
        two characters `freq[a] - freq[b]`, where character `a` has an odd
        frequency in `subs` and character `b` has an even frequency in `subs`
        (freq_b > 0).

        If we look at the constraints of this problem, we see that the only
        possible characters are ["0", "1", "2", "3", "4"], five in total, which
        will lead us to 20 different pairs to check. The length of `s` can go up
        to 3*10^4, in our case will be 20*3*10^4 << 10^8 (1 sec standart). So, a
        O(N) algorithm can deal with this problem.

        So we going to have two nested loops that will pick two character `a`
        and `b`, from ["0", "1", "2", "3", "4"] for us to process. If `a == b`,
        then we just skip.

        First, we need to calculate the prefix-sum for the characters `a` and
        `b`. With that approach we can fast calculate the frequency of a
        character in a specific window [left, right], we just need subtract
        ps[right] from the ps[left-1].

        The idea is to use a slinding window to find the maximum difference
        `freq[a] - freq[b]` in the string `s`. As we're using prefix-sum, the
        idea will be for each `right` boundary find the best placement for a
        `left` boundary that follow the rules.

        Let's define this rules:
            1. the length of our substring needs to be greater or equal to `k`;
            2. `a` needs to have a odd frequency in `subs`;
            3. `b` needs to have a even frequency in `subs`.

        We can fulfill the first rule just by run our right boundary in the
        range [k, n], where `n` is the length of the string `s`. The second and
        third rule we can fulfill by finding a left boundary in which
        `ps_a[right] - ps_a[left] == odd` and `ps_b[right] - ps_b[left] == even`.
        For this, we can use a mathematical rule for parity of numbers. Let `e`
        be an even number and `o` an odd number, we have:

            e - e = e
            e - o = o
            o - e = o
            o - o = e

        So, if `ps_a[right]` is odd, we need `ps_a[left]` to be even to get an
        odd number or if `ps_a[right]` is even, we need `ps_a[left]` to be odd
        to get an odd number. Similarly, for `ps_b[right]`, if it's even, we
        need ` ps_b[left]` to be even and if it's odd we need ` ps_b[left]` to
        be odd.

        If we rewrite or goal, we have:

            diff = (ps_a[right] - ps_b[right]) - (ps_a[left] - ps_b[left])

        So, in order to maximize `diff`, we need to find a valid left boundary
        (according with the parity subtraction rule) that is minimum. But how
        can we find this left in O(1) time? Otherwise we going to need O(N^2).

        First, let see the parity of `ps_a[right]` and `ps_b[right]` as a two
        bit number. Let an even number to be 0 and an odd number to be 1. Also,
        the most significant digit of this number as the parity of `a` and the
        less significant digit as the parity of `b`. So, we have:

            a b  |  target  |  target (int)
            0 0  |    10    |      2
            0 1  |    11    |      3
            1 0  |    00    |      0
            1 1  |    01    |      1

        So, we can create two arrays of four positions, `min_val` and `min_idx`,
        that will store the minimum `ps_a[left] - ps_b[left]` for each target
        parity and their index in the prefix-sum array. So, in O(1), if we need
        to know what is the best choice of a left boundary for a parity of `00`,
        we just need to look at the position 2 of `min_val` to find our answer.
        We initialize `min_val` with infinity and we going to update as we move
        through the array. The only thing we need to do is `min_val[0] = 0`,
        that's the base case where we don't exclude anything.

        Let's define our sliding window idea. For each `right` in range [k,n],
        we do:
            (1) Calculate the parity of `ps_a[right]` and `ps_b[right]` and the
            target parity for this;
            (2) Check if we have seen a valid place for the left boundary in
            `min_val[parity_target]`. If we do, we going to update our answer by
            `max_diff = max(max_diff,
            (prefix_sum_a[right] - prefix_sum_b[right]) - min_val[parity_target])`
            (3) Update the `min_val` array. In this step we calculate the parity
            of the upcoming left boundary and add to our `min_val` array.

        At the end of this `max_diff` has the answer of this problem, so we
        return.
        """
        n = len(s)
        max_diff = float("-inf")

        for a in ["0", "1", "2", "3", "4"]:
            for b in ["0", "1", "2", "3", "4"]:

                # Skip
                if a == b:
                    continue

                # Initialize prefix sum arrays of size n+1 (for 0-based indexing up to n)
                prefix_sum_a = [0] * (n + 1)
                prefix_sum_b = [0] * (n + 1)

                for i, c in enumerate(s):
                    prefix_sum_a[i + 1] = prefix_sum_a[i] + (c == a)
                    prefix_sum_b[i + 1] = prefix_sum_b[i] + (c == b)

                min_val = [float("inf")] * 4  # Initialized to positive infinity
                min_idx = [-1] * 4  # Initialized to -1
                min_val[0] = min_idx[0] = 0

                for right in range(k, n + 1):
                    # (1) Calculate the parity
                    parity_A = prefix_sum_a[right] & 1
                    parity_B = prefix_sum_b[right] & 1
                    parity_target = ((parity_A ^ 1) << 1) + parity_B

                    # (2) Update the max_diff
                    if min_val[parity_target] != float("inf"):
                        if prefix_sum_b[min_idx[parity_target]] != prefix_sum_b[right]:
                            max_diff = max(
                                max_diff,
                                (prefix_sum_a[right] - prefix_sum_b[right])
                                - min_val[parity_target],
                            )

                    # (3) Update `min_val` with upcoming left boundary
                    left = right - k + 1
                    parity_A = prefix_sum_a[left] & 1
                    parity_B = prefix_sum_b[left] & 1
                    parity = (parity_A << 1) + parity_B
                    left_diff = prefix_sum_a[left] - prefix_sum_b[left]

                    if left_diff < min_val[parity]:
                        min_val[parity] = left_diff
                        min_idx[parity] = left

        return max_diff


a = Solution()
print(a.maxDifference(s="12233", k=4))
print(a.maxDifference(s="1122211", k=3))
print(a.maxDifference(s="110", k=3))
