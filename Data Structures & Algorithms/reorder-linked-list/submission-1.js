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
     * @return {void}
     */
    reorderList(head) {
       if(!head.next) return head;
       let [first, second] = this.getHalves(head);
       let reversedSecond = this.reverse(second);
       return this.mergeList(first, reversedSecond);
    }
    /** Returns 1st half, and 2nd half */
    getHalves = (head) => {
        let slow = head;
        let fast = head.next.next;
        let ptr = head;
        while (fast && fast.next) {
           slow = slow.next;
           fast = fast.next.next;
        }
        let secondHalf = slow.next;
        slow.next = null;
        return [ptr, secondHalf];
    }
    mergeList = (list1, list2) => {
        if(!list1) return list2;
        if(!list2) return list1;
        let head = new ListNode ({ val: 0, next: list1 });
        let ptr = head;
        while(list1 && list2) {
            ptr.next = list1;
            list1 = list1.next;
            ptr = ptr.next;
            ptr.next = list2;
            list2 = list2.next
            ptr = ptr.next;
        }
        if (list1) ptr.next = list1;
        if (list2) ptr.next = list2;
        return head.next;
    }
    reverse = (head) => {
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
