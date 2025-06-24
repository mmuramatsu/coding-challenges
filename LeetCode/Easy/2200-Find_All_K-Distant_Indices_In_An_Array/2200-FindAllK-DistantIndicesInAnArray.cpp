class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        vector<int> ans;
        int n = nums.size();

        int right = 0;
        int left = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] == key) {
                left = max(right, i - k);
                right = min(n - 1, i + k) + 1;
                for (int idx = left; idx < right; idx++) {
                    ans.push_back(idx);
                }
            }
        }

        return ans;
    }
};
