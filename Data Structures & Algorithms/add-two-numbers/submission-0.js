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
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1, l2) {
        if(!l1) return l2;
        if(!l2) return l1;
        let carry = 0;
        let head = new ListNode(0);
        let ptr = head;
        while (carry || l1 || l2) {
            const l1Val = l1 ? l1.val : 0;
            const l2Val = l2 ? l2.val : 0;
            const sum = l1Val + l2Val + carry;
            carry = Math.floor(sum / 10);
            ptr.next = new ListNode(sum % 10);
            l1 = l1 ? l1.next : null;
            l2 = l2 ? l2.next : null;
            ptr = ptr.next;
        }
        return head.next;
    }
}
