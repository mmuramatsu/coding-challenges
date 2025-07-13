#include <vector>
#include <climits>

using namespace std;

class Solution
{
private:
    bool memo[28][28][28];
    int min_round = INT_MAX;
    int max_round = INT_MIN;
    int n;

public:
    void solve(int alive, int p1, int p2, int l, int r, int round, int l_count, int m_count, int r_count)
    {
        if (l >= r)
            solve(alive, p1, p2, 0, n - 1, round + 1, l_count, m_count, r_count);
        else if ((alive & (1 << l)) == 0)
            solve(alive, p1, p2, l + 1, r, round, l_count, m_count, r_count);
        else if ((alive & (1 << r)) == 0)
            solve(alive, p1, p2, l, r - 1, round, l_count, m_count, r_count);
        else if (l == p1 && r == p2)
        {
            min_round = min(min_round, round);
            max_round = max(max_round, round);
        }
        else if (!memo[l_count][m_count][r_count])
        {
            memo[l_count][m_count][r_count] = true;

            if (l != p1 && l != p2)
            {
                solve(
                    alive ^ (1 << l),
                    p1,
                    p2,
                    l + 1,
                    r - 1,
                    round,
                    l_count - (l < p1),
                    m_count - (l > p1 && l < p2),
                    r_count - (l > p2));
            }

            if (r != p1 && r != p2)
            {
                solve(
                    alive ^ (1 << r),
                    p1,
                    p2,
                    l + 1,
                    r - 1,
                    round,
                    l_count - (r < p1),
                    m_count - (r > p1 && r < p2),
                    r_count - (r > p2));
            }
        }
    }
    vector<int> earliestAndLatest(int n, int firstPlayer, int secondPlayer)
    {
        firstPlayer -= 1;
        secondPlayer -= 1;
        this->n = n;
        int alive = (1 << n) - 1;
        memset(memo, false, sizeof(memo));

        solve(
            alive,
            firstPlayer,
            secondPlayer,
            0,
            n - 1,
            1,
            firstPlayer,
            secondPlayer - firstPlayer - 1,
            n - 1 - secondPlayer);

        return {min_round, max_round};
    }
};