class Solution
{
public:
    int findLucky(vector<int> &arr)
    {
        std::unordered_map<int, int> freq;

        for (int num : arr)
        {
            freq[num]++;
        }

        int ans = -1;

        for (const auto &[k, v] : freq)
        {
            if (k == v && k > ans)
                ans = k;
        }

        return ans;
    }
};