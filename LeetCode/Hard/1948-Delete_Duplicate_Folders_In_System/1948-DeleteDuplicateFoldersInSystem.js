class TrieNode {
    constructor(folder_name) {
        this.folder = folder_name;
        this.remove = false;
        this.childs = new Map();
    }
}

var insert = function (root, path) {
    for (const folder of path) {
        if (!root.childs.has(folder)) {
            root.childs.set(folder, new TrieNode(folder));
        }
        root = root.childs.get(folder);
    }
}

var mark_duplicate = function (root, visited) {
    let subfolder = [];
    const sortedChildKeys = Array.from(root.childs.keys()).sort();
    for (const child_folder of sortedChildKeys) {
        const child_node = root.childs.get(child_folder);
        subfolder.push(mark_duplicate(child_node, visited));
    }

    let code = subfolder.join("");

    if (code.length > 0) {
        if (visited.has(code)) {
            visited.get(code).remove = true;
            root.remove = true;
        } else {
            visited.set(code, root);
        }
    }

    return `[${root.folder}${code}]`;
}

var remove_duplicates = function (root, stack, result) {
    if (root.remove) {
        return;
    }

    if (root.folder !== "/") {
        stack.push(root.folder);
        result.push([...stack]);
    }

    for (const child_folder of root.childs.keys()) {
        const child_node = root.childs.get(child_folder);
        remove_duplicates(child_node, [...stack], result);
    }

    if (root.folder !== "/") {
        stack.pop();
    }
}

/**
 * @param {string[][]} paths
 * @return {string[][]}
 */
var deleteDuplicateFolder = function (paths) {
    // Add all paths to the Trie tree
    const root = new TrieNode("/");
    for (const path of paths) {
        insert(root, path);
    }

    // Mark the duplicates folders
    const visited = new Map();
    mark_duplicate(root, visited);

    // Remove the duplicate folders
    const result = [];
    for (const folder of root.childs.values()) {
        remove_duplicates(folder, [], result);
    }

    return result;
};