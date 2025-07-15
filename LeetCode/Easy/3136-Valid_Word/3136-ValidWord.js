/**
 * @param {string} word
 * @return {boolean}
 */
var isValid = function (word) {
    if (word.length < 3)
        return false;

    let vowel = false;
    let consonant = false;

    for (const c of word) {
        if (/[a-zA-Z]/.test(c)) {
            let low = c.toLowerCase();
            if (low === 'a' || low === 'e' || low === 'i' || low === 'o' || low === 'u')
                vowel = true;
            else
                consonant = true;
        } else if (!/\d/.test(c))
            return false;
    }

    return vowel && consonant;
}
