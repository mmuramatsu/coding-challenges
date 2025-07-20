#include <vector>

using namespace std;

class Solution
{
public:
    int maximumLength(vector<int> &nums, int k)
    {
        vector<vector<int>> dp(k, std::vector<int>(k, 0));
        int longest = 0;

        for (int num : nums)
        {
            int curr = num % k;

            for (int prev = 0; prev < k; prev++)
            {
                dp[curr][prev] = dp[prev][curr] + 1;
                longest = max(longest, dp[curr][prev]);
            }
        }

        return longest;
    }
};