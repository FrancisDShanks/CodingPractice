//
//Created on April 18, 2014
//
//@author: Xufan Du
//


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if(lists.size()==1) return lists[0];
        if(lists.size()<1) return NULL;
        return mergek(lists,0,lists.size()-1);
    }
    
    ListNode *mergek(vector<ListNode *> &lists, int left, int right){
        if(left<right){
            int m=(left+right)/2;
            return merge(mergek(lists,left,m),mergek(lists,m+1,right));
        }
        return lists[left];
    }
    
    ListNode *merge(ListNode *l1, ListNode *l2){
        ListNode *head = new ListNode(0);
        ListNode *cur = head;
        while(l1!=NULL && l2!=NULL){
            if(l1->val < l2->val){
                cur->next = l1;
                l1=l1->next;
                
            }
            else{
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
            
        }
        
        if(l1!=NULL) cur->next = l1;
        else cur->next = l2;
        return head->next;
    }
};
