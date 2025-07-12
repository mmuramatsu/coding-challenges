#include <iostream>
#include <algorithm>
#include <utility>

class Solution
{
public:
    int mostBooked(int n, vector<vector<int>> &meetings)
    {
        std::sort(meetings.begin(), meetings.end());

        std::priority_queue<int, std::vector<int>, std::greater<int>> free_rooms;
        std::priority_queue<std::pair<long long, int>, std::vector<std::pair<long long, int>>, std::greater<std::pair<long long, int>>> occupied_rooms;
        std::vector<int> rooms_count(n, 0);

        for (int i = 0; i < n; i++)
            free_rooms.push(i);

        for (int i = 0; i < meetings.size(); i++)
        {
            long long start_time = meetings[i][0];
            long long end_time = meetings[i][1];

            while (!occupied_rooms.empty() && occupied_rooms.top().first <= start_time)
            {
                auto [prev_end, room] = occupied_rooms.top();
                occupied_rooms.pop();
                free_rooms.push(room);
            }

            if (!free_rooms.empty())
            {
                occupied_rooms.push({end_time, free_rooms.top()});
                rooms_count[free_rooms.top()]++;
                free_rooms.pop();
            }
            else
            {
                auto [prev_end, room] = occupied_rooms.top();
                occupied_rooms.pop();
                occupied_rooms.push({end_time + (prev_end - start_time), room});
                rooms_count[room]++;
            }
        }

        int max_count = 0;
        int max_index;

        for (int i = 0; i < n; i++)
        {
            if (rooms_count[i] > max_count)
            {
                max_index = i;
                max_count = rooms_count[i];
            }
        }

        return max_index;
    }
};