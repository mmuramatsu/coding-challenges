class Solution {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        int t = 0;
        long long current_len = 1;
        k--;

        while (current_len <= k) {
            current_len *= 2;
            t++;
        }

        char final_char = 'a';

        while (current_len > 1) {
            current_len /= 2;
            t--;

            if (k >= current_len) {
                k -= current_len;

                if (operations[t] == 1)
                    final_char++;

                if (final_char > 'z')
                    final_char = 'a';
            }
        }

        return final_char;
    }
};