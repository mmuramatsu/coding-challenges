class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        int n = s.size();

        if (n % k != 0) {
            s.append((k - (n % k)), fill);
        }

        std::vector<std::string> ans;

        for (int i = 0; i < n; i+=k) {
            ans.push_back(s.substr(i, k));
        }

        return ans;
    }
};