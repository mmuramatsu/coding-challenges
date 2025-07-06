class FindSumPairs
{
private:
    vector<int> nums2;
    vector<int> keys;

    unordered_map<int, int> freq1;
    unordered_map<int, int> freq2;

public:
    FindSumPairs(vector<int> &nums1, vector<int> &nums2)
    {
        this->nums2 = nums2;

        for (int num : nums1)
        {
            ++freq1[num];
        }

        for (int num : nums2)
        {
            ++freq2[num];
        }

        for (const auto &pair : freq1)
        {
            keys.push_back(pair.first);
        }

        std::sort(keys.begin(), keys.end());
    }

    void add(int index, int val)
    {
        --freq2[nums2[index]];
        nums2[index] += val;
        ++freq2[nums2[index]];
    }

    int count(int tot)
    {
        int count = 0;

        for (int k : keys)
        {
            if (k >= tot)
                break;

            if (freq2.find(tot - k) != freq2.end())
            {
                count += freq1[k] * freq2[tot - k];
            }
        }

        return count;
    }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */