#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    int matchPlayersAndTrainers(vector<int> &players, vector<int> &trainers)
    {
        int n = players.size();
        int m = trainers.size();

        sort(players.begin(), players.end());
        sort(trainers.begin(), trainers.end());

        int j = 0;
        int count = 0;

        for (int i = 0; i < n; i++)
        {
            while (j < m && players[i] > trainers[j])
                j++;

            if (j < m)
            {
                count++;
                j++;
            }
            else
                break;
        }

        return count;
    }
};