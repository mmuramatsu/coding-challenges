import heapq


class Solution:
    # Split nums in negative and non-negative + Binary search solution. Beats 97%.
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        Given two interger arrays and an integer `k`, our task is to find the
        kth smallest product of `nums1[i] * nums2[j]` where
        `0 <= i < nums1.length` and `0 <= j < nums2.length`.

        We can have two cases. If `nums1[i]` is negative, then to minimize the
        product we need to multiply by the largest number in `nums2`. If
        `nums1[i]` is positive, then to minimize the product we need to multiply
        by the shortest number in `nums2`. Based on that, to simplify our
        solution, we can split `num` into two arrays, non-negative and negative.
        Also, we can remove the negative sign of the negative part to make the
        products even easier, as we don't need to keep tracking is the number is
        negative or positive.

        Another key point that we need to understand is, let `A1` and `B1` be
        the non-negative part of `nums1` and `nums2`, respectively. Also, let
        `A2` and `B2` be the negative part of `nums1` and `nums2`, respectively.
        If we calculate `len(A1) * len(B2) + len(A2) * len(B1)`, this will give
        us how many negative products we have that are negative, similarly,
        `len(A1) * len(B1) + len(A2) * len(B2)`, will give us how many products
        are non-negative.

        Let's call `negative_count` the number of products negative, if
        `k > negative_count`, means that the `k`th number that we are looking
        for is after the negative products. Also, if `k <= negative_count`,
        means that the `k`th number that we are looking for is in the negative
        products. Based on this analysis, we can reduce the search space by
        looking only in the negative or non-negative products. In the first
        case, our the `k` that we are looking will be `k -= negative_count`,
        meaning that the number is after the non-negative. Similarly, in the
        second case, as we remove the sign of the numbers `k` will become
        `k = negative_count - k + 1`.

        Let's represent this with an example, let say that the products are
        "prod = [-16, -8, -8, -4, 0, 0, 6, 12]". The `negative_count = 4`. Let's
        say that `k = 3`, so the new `k` will be
        `k = negative_count - k + 1 = 2`, which `prod[2] = -8`, which is the
        right answer. Now, let's say that `k=7`, then
        `k = k - negative_count = 3`. Looking only on the non-negative numbers,
        we have `non_neg_prod[3] = 6`, which is correct.

        The idea now is to use Binary Search to find for each number `m` we can
        find `len(prod) == k`, which is our answer. We make a function
        `count_products`, that will count how many products are less than or
        equal to a number `m`. Remembering that we're only looking in one of two
        sides negative or non-negative. If the number of products less or equal
        to `m` is greater than or equal to `k`, we update the `right` side of the
        binary search to `mid`. Otherwise, we update `left` to `mid + 1`. The
        initial state of `left` is 0 and the `right` is `10**10`, which is the
        maximum product we can find based on the constraints. At end of this
        binary search, our answer is on the `left` variable.
        """

        def split(nums):
            pos = []
            neg = []

            for num in nums:
                if num < 0:
                    neg.append(-num)
                else:
                    pos.append(num)

            neg.reverse()
            return pos, neg

        def count_products(A, B, m):
            count = 0
            j = len(B) - 1

            for num in A:
                while j >= 0 and num * B[j] > m:
                    j -= 1

                count += j + 1

            return count

        # A1 and B1 represent the positive part of the array
        # A2 and B2 represent the negative part of the array
        A1, A2 = split(nums1)
        B1, B2 = split(nums2)

        negative_count = len(A1) * len(B2) + len(A2) * len(B1)
        sign = 1

        if k > negative_count:
            # Means that the kth smallest are after the negative numbers
            k -= negative_count
        else:
            # Means that the kth smallest are in the negative numbers
            k = negative_count - k + 1
            sign = -1
            # Invert this two to only multiplicate the negetive numbers
            B1, B2 = B2, B1

        left = 0
        right = 10**10

        while left < right:
            mid = (left + right) // 2

            if count_products(A1, B1, mid) + count_products(A2, B2, mid) >= k:
                right = mid
            else:
                left = mid + 1

        return sign * left

    # Solve but it's too slow. TLE.
    def kthSmallestProduct1(self, nums1: list[int], nums2: list[int], k: int) -> int:
        heap = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heapq.heappush(heap, nums1[i] * nums2[j])

        while k != 0:
            ans = heapq.heappop(heap)
            k -= 1

        return ans


a = Solution()
print(a.kthSmallestProduct(nums1=[2, 5], nums2=[3, 4], k=2))
print(a.kthSmallestProduct(nums1=[-4, -2, 0, 3], nums2=[2, 4], k=6))
print(a.kthSmallestProduct(nums1=[-2, -1, 0, 1, 2], nums2=[-3, -1, 2, 4, 5], k=3))
