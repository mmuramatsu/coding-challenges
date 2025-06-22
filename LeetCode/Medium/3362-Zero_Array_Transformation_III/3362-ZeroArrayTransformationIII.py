import heapq


class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        m = len(queries)

        queries.sort(key=lambda x: x[0])

        available_queries = []  # Max heap
        active_queries = []  # Min heap

        k = 0

        for i in range(n):
            # remove expired queries
            while active_queries and active_queries[0] < i:
                heapq.heappop(active_queries)

            # add potential queries to the available_queries
            while k < m and queries[k][0] <= i:
                # Only the end point is important
                heapq.heappush(available_queries, -queries[k][1])
                k += 1

            # pick the best queries from avaliable to make nums[i] == 0 (len(active) >= nums[i]) and place in active heap
            while (
                len(active_queries) < nums[i]
                and available_queries
                and -available_queries[0] >= i
            ):
                heapq.heappush(active_queries, -heapq.heappop(available_queries))

            # check if len(active) < nums[i]: return -1
            if len(active_queries) < nums[i]:
                return -1

        return len(available_queries)


a = Solution()
print(a.maxRemoval([1, 1, 1, 1], [[0, 2], [0, 3]]))
print(a.maxRemoval(nums=[2, 0, 2], queries=[[0, 2], [0, 2], [1, 1]]))
print(a.maxRemoval(nums=[1, 1, 1, 1], queries=[[1, 3], [0, 2], [1, 3], [1, 2]]))
print(a.maxRemoval(nums=[1, 2, 3, 4], queries=[[0, 3]]))
print(a.maxRemoval(nums=[0, 0, 1, 1, 0], queries=[[3, 4], [0, 2], [2, 3]]))  # 2
