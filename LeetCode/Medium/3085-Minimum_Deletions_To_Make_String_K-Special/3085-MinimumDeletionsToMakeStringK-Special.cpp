class Solution {
public:
    int minimumDeletions(string word, int k) {
        std::unordered_map<char, int> freq;

        // Iterate through the string and update character counts in the map
        for (char c : word) {
            freq[c]++;
        }

        int ans = word.size();

        for (const auto& [_, x] : freq) {
            int deletions = 0;
            for (const auto& [_, y] : freq) {
                if (x > y) {
                    deletions += y;
                } else if (y > x + k) {
                    deletions += y - (x + k);
                }
            }
            ans = min(ans, deletions);
        }

        return ans;
    }
};