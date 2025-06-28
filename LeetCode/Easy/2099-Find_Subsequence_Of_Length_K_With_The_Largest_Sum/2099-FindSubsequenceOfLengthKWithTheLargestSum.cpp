class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        std::vector<std::pair<int, int>> indexedNums;

        for (int i = 0; i < nums.size(); ++i) {
            indexedNums.push_back({nums[i], i});
        }

         std::sort(indexedNums.begin(), indexedNums.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
            return a.first > b.first; // Sort in descending order of value
        });

        std::vector<std::pair<int, int>> greatest;
        for (int i = 0; i < k; ++i) {
            greatest.push_back(indexedNums[i]);
        }

        std::sort(greatest.begin(), greatest.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
            return a.second < b.second; // Sort in ascending order of original index
        });

        std::vector<int> ans;
        for (const auto& p : greatest) {
            ans.push_back(p.first);
        }

        return ans;
    }
};