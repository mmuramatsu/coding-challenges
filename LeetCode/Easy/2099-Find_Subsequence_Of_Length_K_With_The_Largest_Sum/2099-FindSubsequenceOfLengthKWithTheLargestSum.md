Given a list of integer nums and an integer `k` our goal is to find the subsequence of length `k` with greatest sum.

The key point of this problem is that the greatest sum is formed by the `k` greatest numbers of `nums`. So, if we sort the number we know which number form the answer. The only point is that we need to form a subsequence, which requires us to not change the index of this numbers.

The idea is, first create a new list composed of tuples `(num, i)`, where `num` is the number found at `nums[i]`. Then we need to sort this list, based on `num` to find the `k` greatest. Next, we sort again, but based on `i` to find the order of the `k` greatest. Finally, we form the final subsequence with the last list that we create.

Example: `nums = [1,3,4,5,2]`, `k = 2`
* 1. create a list with the tuples: `[(1,0), (3,1), (4,2), (5,3), (2,4)]`;
* 2. sort based on `num`: `[(5,3), (4,2), (3,1), (2,4), (1,0)]`;
* 3. get the `k` greatest: `[(5,3), (4,2)]`;
* 4. sort based on index `i`: `[(4,2), (5,3)]`
* 5. create the answer picking the `num` in each position: `ans = [4, 5]`.