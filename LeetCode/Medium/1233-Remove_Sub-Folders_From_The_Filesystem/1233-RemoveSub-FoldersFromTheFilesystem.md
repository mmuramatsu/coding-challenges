# Problem: 1233 - Remove Sub-Folders from the Filesystem (MEDIUM)

# Problem statement

Given a strign array `folder`, where `folder[i]` is a string that represent a path to a folder format using `"/"` as a delimeter character, resulting in something like this: `"/a/b/c"`.

Our goal is to remove all paths that are sub-folder and return only the ones that are not.

# Intuition:

This problem can be solved by two strategies, Trie or Sorting.

## Trie solution

We can use a Trie, which is a data structure known as Prefix Tree used for storing a dynamic set of strings or keys. For this problem each node of this will be a folder. For example, the path `"/a/b/c"`, will have three nodes. The first one is the node `"a"`, that point to `"b"`, which points to `"c"`. At node `"c"` we have a variable `"_is_end_"` that mark the end of the path that we parse. That will be important to find sub-folders after.

To represent a Trie Node, we can use objects, struct or nested Hash Maps. In my solution, I used nested Hash Maps. We, initially have a empty Hash Map called `root`. When parsing `"/a/b/c"`, we add `"a"` to `root` as a key, and the value will be another Hash Map, which we will add `"b"` as key. We repead this to `"c"`. As this one is the end of our path, we also add the key `"_is_end_" = True` to mark the end of this path in `"c"` Hash Map.

So, the algorithm to solve this problem is:
- parse all the paths in `folder` and add to our Trie;
- for each path in `folder`, iterate through our Trie finding some node with the key `_is_end_`. If none is finded, then this node is not a sub-folder, otherwise, it is a sub-folder.

We just need to append the ones that are not a sub-folder to a list and return.

### Complexity:

Let $N$ be the length of `folder` array and $L$ be the maximum length of a folder path.

- Time complexity: $O(N \cdot L)$
    - we take $O(L)$ to parse each path;
    - the insert function takes $O(L)$. As we need to add $N$ path to the Trie, it takes  $O(N \cdot L)$;
    - the search function takes $O(L)$. As we need to check $N$ paths if they are sub-folders, it takes  $O(N \cdot L)$;

- Space complexity: $O(N \cdot L)$
    - each path, in the worst case, have $L$ nodes. As we need to store $N$ paths, we have, in the worst case, $O(N \cdot L)$.

## Sorting solution

A more simple solution can be done by taking advantage of the lexicographically order of the paths. For example, the paths, `folder = ["/a", "/c/d/e", "/a/b"]`. It's clearly that the thrid is sub-folder of the first one and is the only one that needs to be removed.

If we sort this array, we going to have this order `folder = ["/a", "/a/b", "/c/d/e"]`. We know that if a word is prefix of another, this one will be small compared to the other in the lexicographically order, and this is exactly what happens to the folders and sub-folders path. The folder `"/a/b"` is considered sub-folder of `"/a"` because `"/a" + "/"` is prefix of `"/a/b"`.

So the idea to solve this problem is sort the `folder` array and then, with a simple for loop, check if the last appended path in `ans` is prefix of the current path. If it is, then we do not add to `ans`, otherwise, we append the current path to `ans`.

### Complexity:

Let $N$ be the length of `folder` array and $L$ be the maximum length of a folder path.

- Time complexity: $O(N \cdot L \ \log N)$
    - Sorting the `folder` array takes $O(N \log N)$ comparisons, but can involve $L$ characters, turning into $O(N \cdot L \ \log N)$;
    - the main loop takes $O(N \cdot L)$;
        - to append `"/"` to the `prev_path`, we take $O(L)$;
        - to check if is a prefix we take $O(L)$;

- Space complexity: $O(N)$
    - the in-build sort algorithm uses $O(N)$ space.
