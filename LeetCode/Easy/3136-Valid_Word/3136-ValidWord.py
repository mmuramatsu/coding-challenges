from collections import Counter
import re


class Solution:
    def isValid(self, word: str) -> bool:
        return bool(
            re.fullmatch(
                r"^(?=.*[aeiou])(?=.*[^aeiou0-9])[a-z0-9]{3,}$", word, re.IGNORECASE
            )
        )

    def isValid2(self, word: str) -> bool:
        if len(word) < 3:
            return False

        if not re.fullmatch(r"[A-Za-z0-9]+", word):
            return False

        if not re.search(r"[aeiouAEIOU]+", word):
            return False

        if not re.search(r"[^aeiouAEIOU0-9]+", word):
            return False

        return True

    def isValid1(self, word: str) -> bool:
        if len(word) < 3:
            return False

        freq = Counter(word)

        if "@" in freq or "#" in freq or "$" in freq:
            return False

        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        vowel = False
        consonant = False

        for k, _ in freq.items():
            if not vowel and k in vowels:
                vowel = True

            if not consonant and not k.isdigit() and k not in vowels:
                consonant = True

            if vowel and consonant:
                break

        return vowel and consonant


a = Solution()
print(a.isValid(word="234Adas"))
print(a.isValid(word="b3"))
print(a.isValid(word="a3$e"))
