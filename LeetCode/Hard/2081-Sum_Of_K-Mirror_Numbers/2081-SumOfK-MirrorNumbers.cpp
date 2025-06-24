#include <algorithm>
#include <string>


class Solution {
public:
    std::string to_base_k(long long num, int base) {
        if (num == 0) {
            return "0";
        }

        std::string base_k = "";

        while (num > 0) {
            base_k += static_cast<char>('0' + (num % base));
            num /= base;
        }

        std:reverse(base_k.begin(), base_k.end());

        return base_k;
    }

    bool is_palindrome_str(const std::string& s) {
        std::string reversed_s = s;
        std::reverse(reversed_s.begin(), reversed_s.end());
        return s == reversed_s;
    }

    long long kMirror(int k, int n) {
        int count = 0;
        long long ans = 0;
        long long range_digits = 1;

        while (count < n) {
            for (long long i = range_digits; i < range_digits*10; i++){
                std::string s = std::to_string(i);

                std::string sub;

                if (s.length() <= 1) {
                    sub = ""; // s[:-1] is empty, so reversed is empty
                } else {
                    sub = s.substr(0, s.length() - 1); // Get substring up to last char
                    std::reverse(sub.begin(), sub.end()); // Reverse it
                }

                std::string palindrome = s + sub;

                long long num = std::stoll(palindrome);
                std::string base_k = to_base_k(num, k);

                if (is_palindrome_str(base_k)) {
                    count++;
                    ans += num;

                    if (count == n) return ans;
                }
            }

            for (long long i = range_digits; i < range_digits*10; i++){
                std::string s = std::to_string(i);

                std::string sub = s;
                std::reverse(sub.begin(), sub.end());
                std::string palindrome = s + sub;

                long long num = std::stoll(palindrome);
                std::string base_k = to_base_k(num, k);

                if (is_palindrome_str(base_k)) {
                    count++;
                    ans += num;

                    if (count == n) return ans;
                }
            }

            range_digits *= 10;
        }

        return ans;
    }
};