class Solution:
    def removeSubfolders(self, folder) -> list[str]:
        folder.sort()

        ans = [folder[0]]

        for path in folder[1:]:
            prev_folder = "".join([ans[-1], "/"])

            if not path.startswith(prev_folder):
                ans.append(path)

        return ans

    def removeSubfolders1(self, folder) -> list[str]:
        class Trie:
            def __init__(self):
                self.root = {}

            def insert(self, path):
                splited_path = path.split("/")
                curr_node = self.root

                for folder in splited_path:
                    if folder == "":
                        continue

                    if folder not in curr_node:
                        curr_node[folder] = {}

                    curr_node = curr_node[folder]

                curr_node["_is_end_"] = True

            def is_subfolder(self, path):
                splited_path = path.split("/")
                curr_node = self.root

                for folder in splited_path:
                    if folder == "":
                        continue

                    if "_is_end_" in curr_node.keys():
                        return True

                    if folder not in curr_node:
                        return False

                    curr_node = curr_node[folder]

                return False

        trie = Trie()

        for path in folder:
            trie.insert(path)

        ans = []

        for path in folder:
            if not trie.is_subfolder(path):
                ans.append(path)

        return ans


a = Solution()
print(a.removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
print(a.removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"]))
print(a.removeSubfolders(folder=["/a/b/c", "/a/b/ca", "/a/b/d"]))
