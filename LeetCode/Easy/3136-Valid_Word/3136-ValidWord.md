# Problem: 3136. Valid Word (EASY)

## Problem statement:

Given a string `word`, we need to check if it is valid. To be valid, a word must have
- A length greater than or equal to 3;
- Contains only digits (0-9) and English letters (upper and lower case);
- Contains at least one vowel;
- Contains at least one consonant.

## Intuition:

We can solve this in two way. The first one is to check character by character. First we check if the length is greater than or equal to 3, if not, we return `False`. We need to maintain two flags `vowel` and `consonat` initialize as `False`, to sign if we find a vowel of a consonant. If we find any character that are not alphanumeric we return `False`. At the end we return `vowel and consonant`. If we find both, the result is `True`, otherwise `False`.

The other way to solve this is by Regex. We can verify if `word` full match this regex `"[A-Za-z0-9]+"`. With this we verify if `word` has only alphanumeric characters, if not, we return `False`. We can check if `word` has at least one vowel with `"[aeiouAEIOU]+"` and if has at least one consonant with `"[^aeiouAEIOU0-9]+"`. If it pass all verification we return `True`.

We can also join everything in one regex:

    `(?i)^(?=.*[aeiou])(?=.*[^aeiou0-9])[a-z0-9]{3,}$`

- `(?i)` : Case-insensitive;
- `^`: Anchors the match to the beginning of the string;
- `(?=.*[aeiou])`: Positive lookahead for at least one vowel anywhere in the string. The `.*` asserts that somewhere after the current position we have a vowel;
- `(?=.*[^aeiou0-9])`: Positive lookahead for at least one consonant anywhere in the string;
- `^[a-z0-9]{3,}`: Ensure the string is at least 3 alphanumeric chars long, from start to end;
- `$`: Anchors the match to the end of the string.

### Complexity:
- Time complexity: $O(N)$

- Space complexity: $O(1)$