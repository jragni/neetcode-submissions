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
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        return this.reverse(this.remove(this.reverse(head), n));
    }
    remove(head, n) {
        if (!head) return null;
        if (n === 1) return head.next;
        let curr = head;
        let count = 1;
        while (n !== count + 1) {
            curr = curr.next 
            count++;
        }
        curr.next = curr.next.next;
        return head;
    }
    reverse(head) {
        if (!head) return null;
        let [curr, prev, next] = [head, null, null];
        while (curr) {
            next = curr.next;
            curr.next = prev;
            
            prev = curr;
            curr = next;
        }
        return prev;
    }
}
