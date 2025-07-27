# Problem: 1948 - Delete Duplicate Folders in System (HARD)

## Problem statement:

It's given an array of arrays `paths`, where `paths[i]` is an array of strings like `["a", "b", "c"]`, which represents the path `"/a/b/c"`. Two folders are considered identical if they contain the same **non-empty** set of identical subfolders and underlying subfolders structure. They don't need to be in at the same level. Our task is to find the duplicated folders and remove, returning just the valid ones.

## Intuition:

We need Trie to solve this problem. The goal of this problem is to identify equal substructures in the Trie Tree. Basically if a node `x` has the as childs `a` and `b`, and a node `y` also has as childs `a` and `b`, then `x` and `y` are identical and need to be removed, as well as, `a` and `b`.

So, first we're going to add all folders to our Trie structure. Our Trie class will have three variables, `folder`, `remove`, `childs`, which represents, the folder name, a flag that mark if needs to be removed and a Hash Map to store the childs of this node, respectively.

The insert function needs to take a `path` from `paths`, starting from the `root` node equal to `/`. For each `folder` in `path`, if the current node has a child with this name we move on to this child, is not, we add `folder` as child of this node and move to it. We're going to repeat this until all `folders` are processed and we'll do this for each `path` in `paths`. After that we have all the folder in our Trie structure.

Next step is to mark the duplicate ones. To accomplish this, we'll use a technique called Tree Serialization, which consists in converting a tree data structure into a linear sequence of bits or a string representation. The idea here is to use some kind of DFS to create a string representation of our tree in post order sequence. In our case we going to use `"("` and `")"` as delimeters for each node. Using the example showed before, the node `x` can be represented as `"(x(a)(b))"`. Here, the outer parentesis serialize everything that is in `x` node and below. The two leaf nodes `a` and `b`, as they have none childs they are represented as `(a)` and `(b)`. If we have a node `z` pointing to `x`, the representation of `z` will be `"(z(x(a)(b)))"`, repeating same thing again, the current node followed by their childs.

Using this representation we notice that the representation of `x` and `y` are differing only of the root folder name. The `y` representation is `"(y(a)(b))"`. The `"(a)(b)"` part is the same for both nodes `x` and `y`, which means that they are identical and need to be removed.

The idea is to serialize and mark the duplicates at the same time. For this, we're going to use a Hash Map, where the keys as the serialized representation of the child of the node and the value is a reference for the Trie Node object of the node. So, we recursively move to a node, serialize the childs of this node, and check if we already seen this key in our Hash Map. If not, we simple add to the Hash Map. If we have seen, then we mark the current node and the node in which we see the exactly serializetion to be removed, by changing the variable `remove` in the Trie Node object. We add the curret folder to the serialization and return to the parent node to repeat the process.

Having the node marked, we just need to remove it. We need to using a Stack to correctly write the paths in the answer. The idea is to use DFS to transverse the Trie Tree and removing. For each node we check if is marked to be removed, if it is, we simple return and move to the next. If is node, we add to the stack the folder name and add the stack to the `ans`. Then, we recursively call the same function to all of it's childs and repeat. After that we pop an element from our stack. Imagine that we have the following structure:

    a
    |
    b
    | \
    c  d

Suppose that none of this will be removed. First we add `a` to the stack, and the stack to the answer, getting `ans = [["a"]]`. Then, we move on to `b` and repeat, getting `ans = [["a"], ["a", "b"]]`. We go to `c`, and repeat, `ans = [["a"], ["a", "b"], ["a", "b", "c"]]`. Now we pop `c` from the stack, return to `b` and call for `d`, getting `ans = [["a"], ["a", "b"], ["a", "b", "c"], ["a", "b", "d"]]`. Then we return everything the end the function, getting the exactly result that we need. If in some point we need to remove a node, we simple don't process this branch, so it will never be in the stack neither in the answer.