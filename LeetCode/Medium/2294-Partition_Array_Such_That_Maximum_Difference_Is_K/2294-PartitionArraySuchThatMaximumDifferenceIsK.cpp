class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int ans = 1;
        int max_value = nums[0] + k;

        for(int i = 1; i < nums.size(); i++) {
            if (nums[i] > max_value) {
                ans++;
                max_value = nums[i] + k;
            }
        }

        return ans;
    }
};