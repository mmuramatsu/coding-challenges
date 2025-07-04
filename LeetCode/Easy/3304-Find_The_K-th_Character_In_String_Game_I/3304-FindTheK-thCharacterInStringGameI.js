/**
 * @param {number} k
 * @return {character}
 */
var kthCharacter = function (k) {
    k--;

    return String.fromCharCode(97 + (k == 0 ? 0 : k.toString(2).match(/1/g).length));
};