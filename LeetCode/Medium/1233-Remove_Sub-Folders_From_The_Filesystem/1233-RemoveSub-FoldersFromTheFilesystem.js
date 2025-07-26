/**
 * @param {string[]} folder
 * @return {string[]}
 */
var removeSubfolders = function (folder) {
    folder.sort();

    let ans = [folder[0]];

    for (let i = 1; i < folder.length; i++) {
        if (!folder[i].startsWith(ans[ans.length - 1] + '/'))
            ans.push(folder[i])
    }

    return ans;
};