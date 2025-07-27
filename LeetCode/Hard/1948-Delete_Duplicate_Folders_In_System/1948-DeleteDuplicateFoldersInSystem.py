from collections import defaultdict


class Trie:
    def __init__(self, folder):
        self.folder = folder
        self.remove = False
        self.childs = defaultdict()


class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        def insert(root, path):
            for folder in path:
                if folder not in root.childs:
                    root.childs[folder] = Trie(folder)

                root = root.childs[folder]

        def mark_duplicate(root):
            subfolder = []

            for _, child_node in sorted(root.childs.items()):
                subfolder.append(mark_duplicate(child_node))

            code = "".join(subfolder)

            if subfolder:
                if code in visited:
                    visited[code].remove = True
                    root.remove = True
                else:
                    visited[code] = root

            return f"[{root.folder}{code}]"

        def remove_duplicates(root):
            if root.remove:
                return

            stack.append(root.folder)
            ans.append(stack.copy())

            for child_node in root.childs.values():
                remove_duplicates(child_node)

            stack.pop()

        root = Trie("/")

        # Add all paths to the Trie tree
        for path in paths:
            insert(root, path)

        # Mark the duplicates folders
        visited = {}
        mark_duplicate(root)

        # Remove the duplicate folders
        ans = []
        stack = []
        for child_node in root.childs.values():
            remove_duplicates(child_node)

        return ans


a = Solution()
print(
    a.deleteDuplicateFolder(
        paths=[["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]
    )
)
print(
    a.deleteDuplicateFolder(
        paths=[
            ["a"],
            ["c"],
            ["a", "b"],
            ["c", "b"],
            ["a", "b", "x"],
            ["a", "b", "x", "y"],
            ["w"],
            ["w", "y"],
        ]
    )
)
print(a.deleteDuplicateFolder(paths=[["a", "b"], ["c", "d"], ["c"], ["a"]]))
