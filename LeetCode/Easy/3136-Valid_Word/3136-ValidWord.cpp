#include <string>

class Solution
{
public:
    bool isValid(string word)
    {
        if (word.size() < 3)
            return false;

        bool vowel = false;
        bool consonant = false;

        for (auto c : word)
        {
            if (!isalnum(c))
                return false;

            if (isalpha(c))
            {
                char low = tolower(c);
                if (low == 'a' || low == 'e' || low == 'i' || low == 'o' || low == 'u')
                    vowel = true;
                else
                    consonant = true;
            }
        }

        return vowel && consonant;
    }
};