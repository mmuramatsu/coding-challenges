import heapq


class Solution:
    # Optimized version. Beats 83.73%.
    def minimumDifference(self, nums: list[int]) -> int:
        n3 = len(nums)
        n = n3 // 3

        left = [-x for x in nums[:n]]
        right = [x for x in nums[2 * n :]]
        heapq.heapify(left)
        heapq.heapify(right)

        sum_first = [-sum(left)]
        sum_second = [sum(right)]

        for i in range(n, 2 * n):
            j = (n3 - 1) - i

            sum_first.append(
                sum_first[-1] + heapq.heappushpop(left, -nums[i]) + nums[i]
            )
            sum_second.append(
                sum_second[-1] - heapq.heappushpop(right, nums[j]) + nums[j]
            )

        return min(map(lambda x, y: x - y, sum_first, sum_second[::-1]))

    def minimumDifference2(self, nums: list[int]) -> int:
        n3 = len(nums)
        n = n3 // 3

        heap = [-x for x in nums[:n]]
        heapq.heapify(heap)
        sum_elements = sum(heap) * -1
        prefix_sum = [0] * (n3 + 1)
        prefix_sum[0] = sum_elements

        for i in range(n, 2 * n):
            heapq.heappush(heap, -nums[i])
            sum_elements += nums[i]

            sum_elements -= -heapq.heappop(heap)
            prefix_sum[i - (n - 1)] = sum_elements

        heap = [x for x in nums[2 * n : n3]]
        heapq.heapify(heap)
        sum_elements = sum(heap)
        ans = prefix_sum[n] - sum_elements

        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(heap, nums[i])
            sum_elements += nums[i]

            sum_elements -= heapq.heappop(heap)
            ans = min(ans, prefix_sum[i - n] - sum_elements)

        return ans

    def minimumDifference1(self, nums: list[int]) -> int:
        n3 = len(nums)
        n = n3 // 3

        heap = []
        suffix_sum = [0] * n3
        sum_elements = 0

        for i in range(n3 - 1, n - 1, -1):
            heapq.heappush(heap, nums[i])
            sum_elements += nums[i]

            if len(heap) > n:
                sum_elements -= heapq.heappop(heap)

            if len(heap) == n:
                suffix_sum[i] = sum_elements

        sum_elements = 0
        ans = float("inf")
        heap = []

        for i in range(0, 2 * n):
            heapq.heappush(heap, -nums[i])
            sum_elements += nums[i]

            if len(heap) > n:
                sum_elements -= -heapq.heappop(heap)

            if len(heap) == n:
                ans = min(ans, sum_elements - suffix_sum[i + 1])

        return ans


a = Solution()
print(a.minimumDifference(nums=[3, 1, 2]))
print(a.minimumDifference(nums=[7, 9, 5, 8, 1, 3]))
print(a.minimumDifference(nums=[2, 3, 1, 8, 5, 4]))
