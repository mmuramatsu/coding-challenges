#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#include <algorithm>

class Solution
{
public:
    int maxEvents(vector<vector<int>> &events)
    {
        int n = events.size();
        int count = 0;
        std::sort(events.begin(), events.end(), [](const std::vector<int> &a, const std::vector<int> &b)
                  { return a[0] < b[0]; });

        int day = 0;
        int j = 0;
        std::priority_queue<int, std::vector<int>, std::greater<int>> available;

        while (j < n || !available.empty())
        {

            if (available.empty() && j < n)
                day = max(day, events[j][0]);

            while (j < n && events[j][0] == day)
            {
                available.push(events[j][1]);
                j++;
            }

            while (!available.empty() && available.top() < day)
                available.pop();

            if (!available.empty())
            {
                available.pop();
                count++;
                day++;
            }
        }

        return count;
    }
};