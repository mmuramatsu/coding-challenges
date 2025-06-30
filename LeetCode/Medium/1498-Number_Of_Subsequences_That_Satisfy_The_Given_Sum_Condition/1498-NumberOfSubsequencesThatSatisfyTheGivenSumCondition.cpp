const int MOD=1e9+7;
const int MAX_N=1e5;

std::vector<long long> powers(MAX_N);

void precompute_powers() {
    powers[0] = 1;

    for (int i = 1; i < MAX_N; i++) {
        powers[i] = (powers[i-1] * 2) % MOD;
    }
}

struct PrecomputationInitializer {
    PrecomputationInitializer() {
        precompute_powers();
    }
};

static PrecomputationInitializer initializer;

class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        long long count = 0;

        std::sort(nums.begin(), nums.end());

        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            if (nums[left] + nums[right] <= target) {
                count += powers[right - left];
                left++;
            } else {
                right--;
            }
        }

        return count % MOD;
    }
};