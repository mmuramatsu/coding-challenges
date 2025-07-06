from collections import Counter


class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums2 = nums2

        self.freq_nums1 = Counter(nums1)
        self.freq_nums2 = Counter(nums2)

        self.keys_nums1 = sorted(self.freq_nums1.keys())

    def add(self, index: int, val: int) -> None:
        self.freq_nums2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq_nums2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        count = 0

        for k in self.keys_nums1:
            if k >= tot:
                break
            if self.freq_nums2[tot - k] != 0:
                count += self.freq_nums1[k] * self.freq_nums2[tot - k]

        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
