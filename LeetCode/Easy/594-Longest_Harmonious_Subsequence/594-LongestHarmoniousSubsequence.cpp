class Solution {
public:
    int findLHS(vector<int>& nums) {
        std::unordered_map<int, int> freq;
        int ans = 0;

        for (int num : nums) {
            freq[num]++;
        }

        for (const auto& [k, v] : freq) {
            if (freq.count(k+1))
                ans = max(ans, v + freq[k + 1]);
        }

        return ans;
    }
};