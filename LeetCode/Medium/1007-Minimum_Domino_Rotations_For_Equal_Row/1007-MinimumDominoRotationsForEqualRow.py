from collections import defaultdict


class Solution:
    """Calculate candidates approuch
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        ans = -1
        top_dict = defaultdict(int)
        bottom_dict = defaultdict(int)

        for i in range(len(tops)):
            top_dict[tops[i]] += 1
            bottom_dict[bottoms[i]] += 1

        print(top_dict)
        print(bottom_dict)

        canditate = []

        for k in range(0, 7):
            if top_dict[k] + bottom_dict[k] >= len(tops):
                canditate.append(k)

        print(canditate)

        for key in canditate:
            changes = 0
            aux = tops if top_dict[key] < bottom_dict[key] else bottoms
            counter_part = bottoms if top_dict[key] < bottom_dict[key] else tops
            for i in range(len(tops)):
                if aux[i] == key and counter_part[i] != key:
                    changes += 1

            if (
                top_dict[key] if top_dict[key] > bottom_dict[key] else bottom_dict[key]
            ) + changes == len(tops):
                if ans == -1:
                    ans = changes
                else:
                    ans = changes if changes < ans else ans

        return ans
    """

    ''' Checking only tops[0] and bottoms[0]
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)

        def check(target, sideA, sideB):
            """
            Check how many swaps are needed to make n uniform row of `target` on `sideA`. If impossible, return float('inf').
            """

            swaps = 0
            for i in range(n):
                if sideA[i] != target:
                    if sideB[i] != target:
                        return float("inf")
                    else:
                        swaps += 1

            return swaps

        # I only need to check tops[0] and bottoms[0], because the possible candidates needs to apper in every single position, on top or bottom.
        # If not apper on tops[0] or bottoms[0], then it's impossible.
        ans = min(
            check(tops[0], tops, bottoms),
            check(tops[0], bottoms, tops),
            check(bottoms[0], tops, bottoms),
            check(bottoms[0], bottoms, tops),
        )

        return ans if ans != float("inf") else -1
    '''

    # Optimized version for checking on tops[0] and bottoms[0]
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)

        def check(target):
            """
            Check how many swaps are needed to make n uniform row of `target`. If impossible, return float('inf').
            """

            swaps_top = swaps_bottom = 0
            for i in range(n):
                if tops[i] != target and bottoms[i] != target:
                    return -1
                elif tops[i] != target:
                    swaps_top += 1
                elif bottoms[i] != target:
                    swaps_bottom += 1

            return swaps_top if swaps_top < swaps_bottom else swaps_bottom

        # I only need to check tops[0] and bottoms[0], because the possible candidates needs to apper in every single position, on top or bottom.
        # If not apper on tops[0] or bottoms[0], then it's impossible.
        ans = check(tops[0])

        # If it's possible to form a uniform row with tops[0], then, the check function find the best way to do this
        if ans != -1:
            return ans
        # If it's not and tops[0] != bottoms[0], we check if it's possible for bottoms[0]
        elif tops[0] != bottoms[0]:
            return check(bottoms[0])

        return -1


a = Solution()
print(a.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))
print(a.minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]))
