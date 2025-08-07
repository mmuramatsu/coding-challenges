#include <algorithm>
#include <stack>
#include <string>

using namespace std;

class Solution
{
public:
    string remove(string s, string sub)
    {
        stack<char> stack;

        for (char c : s)
        {
            if (c == sub[1] && !stack.empty() && stack.top() == sub[0])
                stack.pop();
            else
                stack.push(c);
        }

        string res;

        while (!stack.empty())
        {
            res.push_back(stack.top());
            stack.pop();
        }

        reverse(res.begin(), res.end());
        return res;
    }

    int maximumGain(string s, int x, int y)
    {
        int ans = 0;
        string first;
        string second;
        if (y > x)
        {
            first = "ba";
            second = "ab";
        }
        else
        {
            first = "ab";
            second = "ba";
        }

        string new_s = remove(s, first);
        ans += ((s.size() - new_s.size()) / 2) * max(x, y);
        ans += ((new_s.size() - remove(new_s, second).size()) / 2) * min(x, y);

        return ans;
    }
};