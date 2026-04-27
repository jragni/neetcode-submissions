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
        let listLength = this.length(head);
        // first case: sz = 1
        if (listLength === 1) return null;
        // second case: n = 1 e.g. remove last
        let reversedList = this.reverse(head);
        if (n === 1) {
            return this.reverse((reversedList.next));
        } 
        // general case
        let [curr, prev] = [reversedList, null];
        let count = 1;
        while (count !== n) {
            prev = curr;
            curr = curr.next;
            count++;
        }
        prev.next = curr.next;
        return this.reverse(reversedList);
    }

    reverse (head) {
        let [curr, prev, next] = [head, null, null];
        while (curr) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    length(head) {
        let count = 0;
        while (head) {
            count++;
            head = head.next;
        }
        return count;
    }
}
