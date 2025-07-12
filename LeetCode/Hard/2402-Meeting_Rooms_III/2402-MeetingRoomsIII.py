import heapq


class Solution:
    # Min Heap solution. Beats 99.54%.
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: x[0])

        free_rooms = list(range(n))
        occupied_rooms = []
        rooms_count = [0] * n

        for s, e in meetings:
            # Remove from occupied
            while occupied_rooms and occupied_rooms[0][0] <= s:
                _, room = heapq.heappop(occupied_rooms)
                heapq.heappush(free_rooms, room)

            # Book a meeting
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(occupied_rooms, (e, room))
            else:
                prev_end, room = heapq.heappop(occupied_rooms)
                heapq.heappush(occupied_rooms, (e + (prev_end - s), room))

            rooms_count[room] += 1

        print(rooms_count)

        return rooms_count.index(max(rooms_count))


a = Solution()
print(a.mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]))
print(a.mostBooked(n=3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))
print(a.mostBooked(n=2, meetings=[[4, 11], [1, 13], [8, 15], [9, 18], [0, 17]]))
print(
    a.mostBooked(
        n=4,
        meetings=[
            [48, 49],
            [22, 30],
            [13, 31],
            [31, 46],
            [37, 46],
            [32, 36],
            [25, 36],
            [49, 50],
            [24, 34],
            [6, 41],
        ],
    )
)
print(a.mostBooked(n=3, meetings=[[0, 10], [1, 9], [2, 8], [3, 7], [4, 6]]))
