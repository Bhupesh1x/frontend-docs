# Swap Nodes in Pairs

```
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Examples

  Input: head = [1,2,3,4]

  Output: [2,1,4,3]

  Input: head = []

  Output: []

  Input: head = [1,2,3]

  Output: [2,1,3]
```

**code**

```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function (head) {
  if (!head || !head.next) return head;

  let sentinel = new ListNode();
  sentinel.next = head;

  let p = sentinel;
  let c = head;
  let n = head.next;

  while (c && n) {
    p.next = n;
    c.next = n.next;
    n.next = c;

    // Move pointers ahead
    p = c;
    c = p.next;
    // curr next can be null so conditionally move it ahead.
    n = c?.next && c?.next;
  }

  return sentinel.next;
};
```
