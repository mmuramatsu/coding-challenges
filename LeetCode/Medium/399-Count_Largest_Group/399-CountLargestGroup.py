from collections import defaultdict


def countLargestGroup(n: int) -> int:
    len_group = defaultdict(int)

    for i in range(1, n + 1):
        # Sum digits
        value = 0
        num = i

        while num > 0:
            value += num % 10  # extract last digit
            num //= 10

        len_group[value] += 1

    # Find the largest size group
    res = list(len_group.values()).count(max(list(len_group.values())))

    return res


print(countLargestGroup(13))
