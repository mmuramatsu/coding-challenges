import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        sorted_heap = []

        for n in nums:
            heapq.heappush(sorted_heap, n)

            if len(sorted_heap) > k:
                heapq.heappop(sorted_heap)

        return sorted_heap[0]


a = Solution()
print(a.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
print(a.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
