class Solution
{
    int n;
    std::vector<std::vector<int>> memo;
    std::vector<int> next_event;

    int solve(std::vector<std::vector<int>> &events, int event_idx, int k)
    {
        if (k == 0 || event_idx >= n)
            return 0;

        if (memo[event_idx][k] != -1)
            return memo[event_idx][k];

        int skip = solve(events, event_idx + 1, k);
        int attend = solve(events, next_event[event_idx], k - 1) + events[event_idx][2];

        memo[event_idx][k] = max(skip, attend);

        return memo[event_idx][k];
    }

public:
    int maxValue(vector<vector<int>> &events, int k)
    {
        n = events.size();
        std::sort(events.begin(), events.end());
        memo.assign(n, std::vector<int>(k + 1, -1));

        next_event = std::vector<int>(n);

        for (int i = 0; i < n; i++)
            next_event[i] = std::upper_bound(events.begin() + i, events.end(), std::vector<int>{events[i][1] + 1, 0, 0}) - events.begin();

        return solve(events, 0, k);
    }
};