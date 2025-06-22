from bisect import bisect_left


class Solution:
    def maxTaskAssign(
        self, tasks: list[int], workers: list[int], pills: int, strength: int
    ) -> int:
        tasks.sort()
        workers.sort()

        n, m = len(tasks), len(workers)
        ans = 0

        def check(k):
            """
            This function checks if it's possible to complete `k` tasks.

            Args:
                k (int): number of tasks that need to be done by `k` workers.

            Returns:
                bool: Return True if all `k` tasks could be completed.
            """

            if k > len(workers):
                return False

            # Consider the 'k' easiest tasks.
            easiest_k_tasks = tasks[:k]

            # Consider the 'k' strongest workers.
            strongest_k_workers = workers[
                len(workers) - k :
            ].copy()  # Create a copy to avoid modifying the original list

            remaining_pills = pills
            tasks_completed = 0

            # Iterate through the 'k' easiest tasks from hardest to easiest.
            i = len(easiest_k_tasks) - 1

            while i >= 0:
                # Try to assign the current task to the strongest available worker without using a pill.
                if (
                    strongest_k_workers
                    and strongest_k_workers[-1] >= easiest_k_tasks[i]
                ):
                    tasks_completed += 1
                    strongest_k_workers.pop()  # Assign the strongest worker (remove from the list).
                    i -= 1
                else:
                    # If the strongest worker can't do it without a pill (No one can do without pills), check if we have pills left.
                    if remaining_pills > 0:
                        # Use binary search to find the weakest worker who can do the task with a pill.
                        index = bisect_left(
                            strongest_k_workers, easiest_k_tasks[i] - strength
                        )

                        # If a suitable worker is found (index is within bounds).
                        if index < len(strongest_k_workers):
                            remaining_pills -= 1
                            tasks_completed += 1
                            strongest_k_workers.pop(
                                index
                            )  # Assign the worker (remove from the list).
                            i -= 1
                        else:
                            # If no worker can do the task even with a pill, it's impossible to complete 'k' tasks.
                            return False
                    else:
                        # If no pills are left and the strongest worker can't do the task, it's impossible.
                        return False

            # Return True if all 'k' easiest tasks could be completed.
            return tasks_completed == k

        # Binary search to find the maximum number of tasks that can be assigned.
        low = 0
        # The high will be the min(n, m) (the shorter)
        high = n if n < m else m

        while low <= high:
            mid = (high + low) // 2
            # Check if it's possible to complete 'mid' tasks.
            if check(mid):
                ans = mid
                # If it's possible, try for a larger number of tasks.
                low = mid + 1
            else:
                # If it's not possible, try for a smaller number of tasks.
                high = mid - 1

        return ans


a = Solution()


print(a.maxTaskAssign([10, 1, 10], [5], 1, 1))
print(a.maxTaskAssign([3, 2, 1], [0, 3, 3], 1, 1))
print(a.maxTaskAssign([5, 4], [0, 0, 0], 1, 5))
print(a.maxTaskAssign([10, 15, 30], [0, 10, 10, 10, 10], 3, 10))
print(a.maxTaskAssign([5, 9, 8, 5, 9], [1, 6, 4, 2, 6], 1, 5))
print(a.maxTaskAssign([2, 5], [1, 3, 4], 1, 1))

"""
print(check(0, [1, 2, 3], [0, 3, 3], 1, 1))
print(check(1, [1, 2, 3], [0, 3, 3], 1, 1))
print(check(2, [1, 2, 3], [0, 3, 3], 1, 1))
print(check(3, [1, 2, 3], [0, 3, 3], 1, 1))
print(check(1, [1, 10, 10], [5], 1, 1))
print(check(2, [1, 10, 10], [2, 5], 1, 1))
"""
