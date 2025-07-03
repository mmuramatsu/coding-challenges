static const int MOD = 1000000007;

class Solution {
public:
    int possibleStringCount(string word, int k) {
        std::vector<int> groups;
        int n = word.size();

        int count = 1;

        for (int i = 1; i < n; i++) {
            if (word[i - 1] == word[i]) {
                count++;
            } else {
                groups.push_back(count);
                count = 1;
            }
        }

        groups.push_back(count);

        long long total = 1;

        for (int size: groups) {
            total = (total * size) % MOD;
        }

        if (groups.size() >= k)
            return total;

        std::vector<long long> prefix_sum(k, 1);
        std::vector<long long> dp;

        for (int size : groups) {
            dp = std::vector<long long>(k, 0);

            for (int length = 1; length < k; length++) {
                dp[length] = prefix_sum[length - 1];

                if (length - size - 1 >= 0)
                    dp[length] = (dp[length] - prefix_sum[length - size - 1] + MOD) % MOD;
            }

            prefix_sum = std::vector<long long>(k, 0);

            for (int i = 1; i < k; i++) {
                prefix_sum[i] = (prefix_sum[i - 1] + dp[i]) % MOD;
            }
        }

        return (total - prefix_sum[k - 1] + MOD) % MOD;
    }
};