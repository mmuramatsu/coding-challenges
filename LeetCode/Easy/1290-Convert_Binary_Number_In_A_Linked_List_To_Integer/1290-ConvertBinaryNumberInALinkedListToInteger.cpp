/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    int getDecimalValue(ListNode *head)
    {
        int num = 0;
        ListNode *curr = head;

        while (curr != nullptr)
        {
            num = (num << 1) + curr->val;
            curr = curr->next;
        }

        return num;
    }
};