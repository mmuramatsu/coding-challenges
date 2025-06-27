class Solution {
public:
    bool is_subsequence(string s, string subseq, int k) {
        int i = 0;
        int j = 0;
        int n = s.size();
        int m = subseq.size();

        while (i < n) {
            if (s[i] == subseq[j]) {
                j++;
                if (j == m) {
                    j = 0;
                    k--;

                    if (k == 0)
                        return true;
                }
            }
            i++;
        }

        return false;
    }

    string longestSubsequenceRepeatedK(string s, int k) {
        std::map<char, int> freq;

        for (char c : s)
            freq[c]++;

        std::vector<char> possible_chars;

         for (const auto& pair : freq) {
            if (pair.second >= k) possible_chars.push_back(pair.first);
         }

         std::sort(possible_chars.begin(), possible_chars.end());

         std::queue<std::string> queue;
         queue.push("");

         std::string ans;

         while (not queue.empty()) {
            std::string curr_string = queue.front();
            queue.pop();
            ans = curr_string;
            cout << ans;

            for (char c : possible_chars) {
                std::string candidate = curr_string + c;
                if (is_subsequence(s, candidate, k))
                    queue.push(candidate);
            }

         }

         return ans;
    }
};