#include <vector>

class Solution
{
public:
    int maximumLength(vector<int> &nums)
    {
        int odd = 0;
        int even = 0;
        int alternate_even = 0;
        int alternate_odd = 0;
        bool next_even = true;
        bool next_odd = true;

        for (auto num : nums)
        {
            if (num & 1)
            {
                // Odd
                odd += 1;
                if (next_odd)
                {
                    alternate_odd += 1;
                    next_odd = false;
                }

                if (!next_even)
                {
                    alternate_even += 1;
                    next_even = true;
                }
            }
            else
            {
                // Even
                even += 1;

                if (next_even)
                {
                    alternate_even += 1;
                    next_even = false;
                }

                if (!next_odd)
                {
                    alternate_odd += 1;
                    next_odd = true;
                }
            }
        }

        return max({even, odd, alternate_even, alternate_odd});
    }
};