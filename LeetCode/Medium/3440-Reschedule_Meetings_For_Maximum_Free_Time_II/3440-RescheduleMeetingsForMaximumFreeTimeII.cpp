class Solution
{
public:
    int maxFreeTime(int eventTime, vector<int> &startTime, vector<int> &endTime)
    {
        startTime.push_back(eventTime);
        endTime.insert(endTime.begin(), 0);

        int m = startTime.size();
        std::vector<int> gaps;

        for (int i = 0; i < m; i++)
            gaps.push_back(startTime[i] - endTime[i]);

        std::vector<int> sorted_gaps;
        sorted_gaps.assign(gaps.begin(), gaps.end());
        std::sort(sorted_gaps.begin(), sorted_gaps.end());

        std::vector<int> meetings;

        for (int i = 1; i < m; i++)
            meetings.push_back(endTime[i] - startTime[i - 1]);

        int n = meetings.size();
        int j = 1;
        int max_free_time = 0;
        int curr_free_time = 0;

        for (int duration : meetings)
        {
            bool founded = false;
            bool equal_left = true;
            bool equal_right = true;

            for (int i = m - 1; i >= 0 && i >= m - 4; i--)
            {
                if (sorted_gaps[i] >= duration)
                {
                    if (equal_left && sorted_gaps[i] == gaps[j - 1])
                    {
                        equal_left = false;
                    }
                    else if (equal_right && sorted_gaps[i] == gaps[j])
                    {
                        equal_right = false;
                    }
                    else
                    {
                        founded = true;
                        break;
                    }
                }
            }

            if (founded)
                curr_free_time = gaps[j - 1] + duration + gaps[j];
            else
                curr_free_time = gaps[j - 1] + gaps[j];

            max_free_time = max(max_free_time, curr_free_time);

            j += 1;
        }

        return max_free_time;
    }
};