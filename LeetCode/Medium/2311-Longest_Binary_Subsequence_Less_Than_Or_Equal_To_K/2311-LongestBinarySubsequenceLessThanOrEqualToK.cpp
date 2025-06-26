class Solution {
public:
    int longestSubsequence(string s, int k) {
        int length = 0;
        int power = 0;
        long long num = 0;

        for (int i = s.size()-1; i >= 0; i--) {
            if (s[i] == '1') {
                if (power < 32 && (num + (1LL << power)) <= k) {
                    num = num + (1LL << power);
                    length++;
                }
            } else {
                length++;
            }

            power++;
        }

        return length;
    }
};