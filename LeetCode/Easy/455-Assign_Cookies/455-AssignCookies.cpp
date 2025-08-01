#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    int findContentChildren(vector<int> &g, vector<int> &s)
    {
        int n = g.size();
        int m = s.size();

        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int j = 0;
        int count = 0;

        for (int i = 0; i < n; i++)
        {
            while (j < m && g[i] > s[j])
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