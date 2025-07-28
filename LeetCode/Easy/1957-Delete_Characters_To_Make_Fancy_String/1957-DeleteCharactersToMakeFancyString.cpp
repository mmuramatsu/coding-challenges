#include <string>

class Solution
{
public:
    string makeFancyString(string s)
    {
        if (s.size() < 3)
            return s;

        char prev = s[0];
        int count = 1;
        string ans = "";
        ans.push_back(s[0]);

        for (int i = 1; i < s.size(); i++)
        {
            if (prev == s[i])
                count++;
            else
                count = 1;

            if (count < 3)
                ans.push_back(s[i]);

            prev = s[i];
        }

        return ans;
    }
};