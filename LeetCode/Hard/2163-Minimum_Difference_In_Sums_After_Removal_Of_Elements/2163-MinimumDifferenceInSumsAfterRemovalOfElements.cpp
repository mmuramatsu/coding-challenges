#include <vector>
#include <queue>
#include <numeric>
#include <algorithm>

class Solution
{
public:
    long long minimumDifference(vector<int> &nums)
    {
        int n3 = nums.size();
        int n = n3 / 3;

        std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
        std::vector<long long> suffix_sum(n3, 0);
        long long current_sum_suffix = 0;

        for (int i = n3 - 1; i >= n - 1; --i)
        {
            min_heap.push(nums[i]);
            current_sum_suffix += nums[i];

            if (min_heap.size() > n)
            {
                current_sum_suffix -= min_heap.top();
                min_heap.pop();
            }

            if (min_heap.size() == n)
            {
                suffix_sum[i] = current_sum_suffix;
            }
        }

        std::priority_queue<int> max_heap_prefix;
        long long current_sum_prefix = 0;
        long long min_diff = std::numeric_limits<long long>::max();

        for (int i = 0; i < 2 * n; ++i)
        {
            max_heap_prefix.push(nums[i]);
            current_sum_prefix += nums[i];

            if (max_heap_prefix.size() > n)
            {
                current_sum_prefix -= max_heap_prefix.top();
                max_heap_prefix.pop();
            }

            if (max_heap_prefix.size() == n)
            {
                min_diff = std::min(min_diff, current_sum_prefix - suffix_sum[i + 1]);
            }
        }

        return min_diff;
    }
};