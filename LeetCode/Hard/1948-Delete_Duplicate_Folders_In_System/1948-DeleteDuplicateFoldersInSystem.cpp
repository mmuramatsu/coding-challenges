#include <map>
#include <string>

using namespace std;

class Solution
{
    struct Trie
    {
        string folder;
        bool remove = false;
        map<string, Trie *> childs;
        Trie(string folder)
        {
            this->folder = folder;
        }
    };

    void insert(Trie *root, vector<string> &path)
    {
        for (auto &folder : path)
        {
            if (!root->childs.count(folder))
                root->childs[folder] = new Trie(folder);

            root = root->childs[folder];
        }
    }
    string mark_duplicate(Trie *root, unordered_map<string, Trie *> &visited)
    {
        string subfolder;
        for (auto &[childsfolder, childsnode] : root->childs)
            subfolder += mark_duplicate(childsnode, visited);

        if (subfolder.size())
        {
            if (visited.count(subfolder))
            {
                visited[subfolder]->remove = true;
                root->remove = true;
            }
            else
            {
                visited[subfolder] = root;
            }
        }
        return "[" + root->folder + subfolder + "]";
    }
    void remove_duplicates(Trie *root, vector<string> &stack, vector<vector<string>> &res)
    {
        if (root->remove)
            return;

        stack.push_back(root->folder);
        res.push_back(stack);

        for (auto &[subfolder, childsnode] : root->childs)
            remove_duplicates(childsnode, stack, res);

        stack.pop_back();
    }

public:
    vector<vector<string>> deleteDuplicateFolder(vector<vector<string>> &paths)
    {
        // Add all paths to the Trie tree
        Trie *root = new Trie("/");
        for (auto &path : paths)
            insert(root, path);

        // Mark the duplicates folders
        unordered_map<string, Trie *> visited;
        mark_duplicate(root, visited);

        // Remove the duplicate folders
        vector<vector<string>> res;
        vector<string> stack;
        for (auto &[subfolder, childsnode] : root->childs)
            remove_duplicates(childsnode, stack, res);

        return res;
    }
};