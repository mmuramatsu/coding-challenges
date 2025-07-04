class Solution {
public:
    char kthCharacter(int k) {
        std::bitset<320> b(k - 1);

        return char(97 + b.count());
    }
};