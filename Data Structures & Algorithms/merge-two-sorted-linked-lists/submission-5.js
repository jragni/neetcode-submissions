/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
       // check if l1 -> not return l2
       if (!list1) return list2;
       // check l2 -> not return l1
       if (!list2) return list1;
       // create dummy head
       let head = new ListNode(0, null)
       // set next, a pointer to dummy head
       let next = head;
       // while both l1 and l2
       while(list1 && list2) {
          // check for smaller
            // set next to smaller, iterate smaller
          if (list1.val <= list2.val) {
            next.next = list1;
            list1 = list1.next
          } else {
            next.next = list2;
            list2 = list2.next;
          }
          // iterate next
          next = next.next;
       }
       // if l1 still has nodes append to next
       if (list1) next.next = list1;
       // if l2 still has nodes apppend to next 
       if (list2) next.next = list2;

       return head.next;
    }
}
