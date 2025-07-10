class Solution
{
public:
    int maxFreeTime(int eventTime, int k, vector<int> &startTime, vector<int> &endTime)
    {
        startTime.push_back(eventTime);
        endTime.insert(endTime.begin(), 0);

        int n = startTime.size();
        std::vector<int> gaps;

        for (int i = 0; i < n; i++)
            gaps.push_back(startTime[i] - endTime[i]);

        int left = 0;
        int max_free_time = 0;
        int curr_free_time = 0;

        for (int i = 0; i < k; i++)
            curr_free_time += gaps[i];

        for (int right = k; right < n; right++)
        {
            curr_free_time += gaps[right];
            max_free_time = max(max_free_time, curr_free_time);
            curr_free_time -= gaps[left];
            left++;
        }

        return max_free_time;
    }
};