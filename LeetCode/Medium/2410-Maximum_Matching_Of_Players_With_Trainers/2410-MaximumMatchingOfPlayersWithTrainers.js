/**
 * @param {number[]} players
 * @param {number[]} trainers
 * @return {number}
 */
var matchPlayersAndTrainers = function (players, trainers) {
    let n = players.length;
    let m = trainers.length;

    players.sort((a, b) => a - b);
    trainers.sort((a, b) => a - b);

    let j = 0;
    let count = 0;

    for (let i = 0; i < n; i++) {
        while (j < m && players[i] > trainers[j])
            j++;

        if (j < m) {
            count++;
            j++;
        } else
            break;
    }

    return count;
};