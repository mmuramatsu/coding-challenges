class Solution:
    def maximumValueSum1(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        """
        Intuition:
        The operation allows us to XOR the values of two connected nodes (u, v) with k.
        Due to the tree structure and the nature of this operation, we can propagate the
        XOR effect. Applying the operation on (u, v) and then (v, w) effectively XORs u and w
        while reverting v. This means that through a sequence of these pairwise operations,
        we can achieve a state where any even number of nodes in the tree have their values
        XORed with k an odd number of times (which is equivalent to a single XOR in terms of the final value).

        How we solve:
        1. Calculate the 'gain' for each node if its value is XORed with k: (nums[i] ^ k) - nums[i].
        2. We want to select an even number of nodes to XOR such that the total gain is maximized.
        3. Sort these gains in descending order.
        4. Greedily consider pairs of gains from the sorted list. If the sum of a pair is non-negative,
           including these XORs contributes to a larger total sum while maintaining an even number
           of effectively XORed nodes.
        5. The maximum possible sum is the original sum of nums plus the maximum total gain we can
           achieve from selecting an even number of nodes to XOR.

        Important details:
        - The tree structure (specifically, its connectivity) is crucial as it allows us to effectively
          target any even-sized subset of nodes for the XOR operation through a series of edge operations.
        - We must choose an even number of nodes to XOR because each edge operation always affects two nodes.
          Therefore, the total number of nodes whose values are flipped an odd number of times must be even.
        - We prioritize larger gains to maximize the overall sum. The greedy pairwise approach on the sorted gains
          helps us achieve this efficiently.
        """
        n = len(nums)
        gain = [0] * n

        for i in range(n):
            gain[i] = (nums[i] ^ k) - nums[
                i
            ]  # Calculate the gain if nums[i] is XORed with k

        gain.sort(reverse=True)  # Sort the gains in descending order
        max_gain = 0

        # Iterate through the sorted gains by pairs
        for i in range(1, n, 2):
            # Check if there's a pair to consider
            if i < n:
                # If the sum of the current pair of gains is non-negative, add it to max_gain
                if max_gain + gain[i] + gain[i - 1] >= max_gain:
                    max_gain += gain[i] + gain[i - 1]
                else:
                    # If adding the pair decreases the gain, we can stop as the gains are sorted descending
                    break

        return sum(nums) + max_gain

    # Greedy solution that beat 100%
    def maximumValueSum2(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        """
        The code iterates through each number in nums and greedily chooses the larger value
        between the original number and its XOR with k, adding it to the total sum ans. It
        also keeps track of how many times the XORed value was chosen (xored_nodes).

        If the total number of times the XORed value was chosen (xored_nodes) is even,
        then we have a valid state according to the problem's constraints (even number
        of effective XORs), and ans is the maximum sum.

        If xored_nodes is odd, it means we've made an odd number of "flips" that
        increased the sum. To satisfy the "even number of effective XORs" rule, we
        need to undo one of these flips. To maximize the sum, we undo the flip that
        had the smallest positive impact (or caused the least increase).
        discarded_value tracks this minimum positive difference encountered when
        we chose the XORed value. By subtracting discarded_value from ans, we
        effectively revert the least beneficial XOR, resulting in a state with
        an even number of effective XORs and a maximized sum.
        """
        ans = 0
        xored_nodes = 0  # Count of nodes where XORing increased (or equaled) the value
        discarded_value = float(
            "inf"
        )  # Minimum difference between XORed and original value (for odd case)

        for n in nums:
            xor = n ^ k
            if n > xor:
                ans += n  # Original value is better
            else:
                ans += xor  # XORed value is better or equal
                xored_nodes += 1  # Increment the count of 'beneficial' XORs

            # Track the smallest absolute difference for a beneficial XOR
            discarded_value = (
                abs(xor - n) if abs(xor - n) < discarded_value else discarded_value
            )

        # If the number of beneficial XORs is odd, we need to undo one (the least beneficial)
        return ans if not xored_nodes & 1 else ans - discarded_value

    # DP version
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        dp = [0, -(10**18)]

        for n in nums:
            c0 = dp[0] + n
            c1 = dp[1] + n
            xor = n ^ k

            dp = [
                c0 if c0 > dp[1] + xor else dp[1] + xor,
                c1 if c1 > dp[0] + xor else dp[0] + xor,
            ]

        return dp[0]


a = Solution()
print(a.maximumValueSum(nums=[1, 2, 1], k=3, edges=[[0, 1], [0, 2]]))  # 6
print(a.maximumValueSum(nums=[2, 3], k=7, edges=[[0, 1]]))  # 9

print(
    a.maximumValueSum(
        nums=[7, 7, 7, 7, 7, 7], k=3, edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
    )
)  # 42

print(
    a.maximumValueSum(
        nums=[24, 78, 1, 97, 44], k=6, edges=[[0, 2], [1, 2], [4, 2], [3, 4]]
    )
)  # 260
