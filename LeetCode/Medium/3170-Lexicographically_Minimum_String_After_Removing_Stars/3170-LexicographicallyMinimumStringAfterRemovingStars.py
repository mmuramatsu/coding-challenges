from collections import defaultdict
import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        """
        We're receiving a string `s` that can contain some "*" characters which
        need to be removed from the string. Every time find a "*" in the string
        we need to remove this "*" and the smallest non-"*" character on the
        left of this. Our task is to process all the "*" and return the string
        after that transformations.

        The key point of this problem is that we always need to know a list of
        the smallest characters we seem so far in order and the indexes of each
        one. We're going to use two data structure to deal with this. The first
        one is a Min Heap, which will store the characters that we already seem
        and every time that we need to know what is the last smallest character
        we pop the smallest. The second data struct that we going to use is a
        Map, to store a list of the indexes where each character has been
        founded.

        The idea is, for every character `c`, if `c` it's a non-"*", we gonna
        push this into our Heap and add store the index of `c` in our Map. If
        `c` is a "*", then we mark this position to be removed, get the smallest
        character by popping from our Heap and mark the last added index of
        this character on our Map to be removed.

        Note that we can't remove the characters during this loop, because this
        will ruin the indexes we have saved so far. We're going to maintain a
        boolean array with the same size of `s`, in which, each position of this
        array, if it's True, means that we need to keep the `s[i]` character,
        otherwise, we need to remove.

        Finally, we run a loop to reconstruct the final string.
        """
        n = len(s)
        indexes = defaultdict(list)
        min_heap = []
        keep = [True] * n

        for i in range(n):
            if s[i] == "*":
                keep[i] = False
                char_to_remove = heapq.heappop(min_heap)
                keep[indexes[char_to_remove][-1]] = False
                indexes[char_to_remove].pop(-1)
            else:
                heapq.heappush(min_heap, s[i])
                indexes[s[i]].append(i)

        ans = []

        for i, c in enumerate(s):
            if keep[i]:
                ans.append(c)

        return "".join(ans)


a = Solution()
print(a.clearStars(s="aaba*"))
print(a.clearStars(s="aaba**"))
print(a.clearStars(s="abc"))
