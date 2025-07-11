class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: list[int], endTime: list[int]
    ) -> int:
        startTime.append(eventTime)
        endTime = [0] + endTime

        m = len(startTime)
        gaps = [startTime[i] - endTime[i] for i in range(m)]
        sorted_gaps = sorted(gaps)

        meetings = [endTime[i] - startTime[i - 1] for i in range(1, m)]
        n = len(meetings)

        j = 1
        curr_free_time = 0
        max_free_time = 0

        for duration in meetings:
            # find an gap that can fit this meeting
            founded = False

            equal_left = True
            equal_right = True
            for i in range(n - 1, -1, -1):
                if sorted_gaps[i] >= duration:
                    if equal_left and sorted_gaps[i] == gaps[j - 1]:
                        equal_left = False
                    elif equal_right and sorted_gaps[i] == gaps[j]:
                        equal_right = False
                    else:
                        founded = True
                        break

            # If is founded, curr_free_time = gaps[j-1] + duration + gaps[j]
            if founded:
                curr_free_time = gaps[j - 1] + duration + gaps[j]
            else:
                # If not, curr_free_time = gaps[j-1] + gaps[j]
                curr_free_time = gaps[j - 1] + gaps[j]

            # max_free_time = max(max_free_time, curr_free_time)
            max_free_time = max(max_free_time, curr_free_time)

            j += 1

        return max_free_time


a = Solution()
print(a.maxFreeTime(eventTime=5, startTime=[1, 3], endTime=[2, 5]))
print(a.maxFreeTime(eventTime=10, startTime=[0, 7, 9], endTime=[1, 8, 10]))
print(a.maxFreeTime(eventTime=10, startTime=[0, 3, 7, 9], endTime=[1, 4, 8, 10]))
print(a.maxFreeTime(eventTime=5, startTime=[0, 1, 2, 3, 4], endTime=[1, 2, 3, 4, 5]))
