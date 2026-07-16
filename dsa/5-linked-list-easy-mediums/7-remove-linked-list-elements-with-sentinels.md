# Remove Linked List Elements

## Problem

Given the head of a linked list and an integer `val`, remove all nodes whose value is equal to `val` and return the new head.

### Example

```js
Input: ((head = [1, 2, 6, 3, 4, 5, 6]), (val = 6));
Output: [1, 2, 3, 4, 5];
```

---

# Intuition

The tricky part is when the node to be removed is the head node itself.

To avoid handling the head separately, we create a dummy node (`sentinel`) before the actual head.

Now every node has a previous node, making deletion easy.

While traversing:

- If `prev.next.val == val`, skip that node.
- Otherwise move `prev` forward.

---

# Code

```js
var removeElements = function (head, val) {
  let sentinel = new ListNode();
  sentinel.next = head;

  let prev = sentinel;

  while (prev && prev.next) {
    if (prev.next.val == val) {
      prev.next = prev.next.next;
    } else {
      prev = prev.next;
    }
  }

  return sentinel.next;
};
```

---

# Approach

1. Create a dummy node (`sentinel`).
2. Point `sentinel.next` to `head`.
3. Start `prev` from `sentinel`.
4. Traverse while `prev.next` exists.
5. If the next node contains `val`:
   - Remove it by connecting `prev.next` to `prev.next.next`.
6. Otherwise move `prev` forward.
7. Return `sentinel.next`.

---

# Dry Run

### Input

```js
head = [1, 2, 6, 3, 4, 5, 6];
val = 6;
```

Initial List:

```text
sentinel -> 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> null
```

| Step | prev Value | prev.next Value | Equals val? | List State                        | Action    |
| ---- | ---------- | --------------- | ----------- | --------------------------------- | --------- |
| Init | sentinel   | 1               | ❌          | `1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6` | start     |
| 1    | 1          | 2               | ❌          | `1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6` | move prev |
| 2    | 2          | 6               | ✅          | `1 -> 2 -> 3 -> 4 -> 5 -> 6`      | remove 6  |
| 3    | 2          | 3               | ❌          | `1 -> 2 -> 3 -> 4 -> 5 -> 6`      | move prev |
| 4    | 3          | 4               | ❌          | `1 -> 2 -> 3 -> 4 -> 5 -> 6`      | move prev |
| 5    | 4          | 5               | ❌          | `1 -> 2 -> 3 -> 4 -> 5 -> 6`      | move prev |
| 6    | 5          | 6               | ✅          | `1 -> 2 -> 3 -> 4 -> 5`           | remove 6  |
| Done | —          | —               | —           | `1 -> 2 -> 3 -> 4 -> 5`           | return    |

---

# Visual Removal

Removing first `6`

```text
Before

2 ----> 6 ----> 3

After

2 ------------> 3
```

Removing last `6`

```text
Before

5 ----> 6 ----> null

After

5 ------------> null
```

---

# Why We Don't Move prev After Deletion

Suppose:

```text
1 -> 6 -> 6 -> 3
```

When first `6` is removed:

```text
1 -> 6 -> 3
```

If we move `prev` immediately, the second `6` would be skipped.

That's why after deletion:

```js
prev.next = prev.next.next;
```

we stay on the same `prev` and check again.

---

# Complexity Analysis

### Time Complexity

```text
O(n)
```

We visit each node at most once.

### Space Complexity

```text
O(1)
```

Only a few extra pointers are used.

---

# Key Takeaways

- Use a dummy/sentinel node whenever the head might be removed.
- To delete a node:
  ```js
  prev.next = prev.next.next;
  ```
- After deletion, do not move `prev`.
- Move `prev` only when no deletion happens.
- Sentinel node helps avoid special handling for head deletions.
