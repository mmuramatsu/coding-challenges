#include <vector>

using namespace std;

class Solution
{
public:
    int maximumUniqueSubarray(vector<int> &nums)
    {
        set<int> elements = {nums[0]};
        int sum_elements = nums[0];
        int ans = nums[0];

        int left = 0;

        for (int right = 1; right < nums.size(); right++)
        {
            if (elements.find(nums[right]) != elements.end())
            {
                while (nums[left] != nums[right])
                {
                    sum_elements -= nums[left];
                    elements.erase(nums[left]);
                    left += 1;
                }

                sum_elements -= nums[left];
                elements.erase(nums[left]);
                left += 1;
            }

            elements.insert(nums[right]);
            sum_elements += nums[right];
            ans = max(ans, sum_elements);
        }

        return ans;
    }
};