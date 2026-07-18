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

This solution handles the head node separately.

The main challenge is that the head itself may contain the value we want to remove.

So first:

- Keep moving `head` forward while `head.val === val`.

After we get a valid head:

- Traverse the list using `curr`.
- If `curr.next` contains the target value, remove it.
- Otherwise move `curr` forward.

This way all matching nodes are removed.

---

# Code

```js
var removeElements = function (head, val) {
  if (!head || !head?.val) return head;

  while (head?.val === val) {
    head = head.next;
  }

  let curr = head;

  while (curr && curr.next) {
    if (curr.next.val === val) {
      curr.next = curr.next.next;
    } else {
      curr = curr.next;
    }
  }

  return head;
};
```

---

# Approach

### Step 1: Handle head nodes

Keep moving the head while its value equals `val`.

```js
while (head?.val === val) {
  head = head.next;
}
```

Example:

```text
7 -> 7 -> 7 -> 3 -> 4
```

becomes

```text
3 -> 4
```

---

### Step 2: Traverse remaining list

Use a pointer `curr`.

If next node should be removed:

```js
curr.next = curr.next.next;
```

Otherwise:

```js
curr = curr.next;
```

---

# Dry Run

### Input

```js
head = [1, 2, 6, 3, 4, 5, 6];
val = 6;
```

Initial List:

```text
1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
```

### Head Processing

| Step | Head Value | Equals val? | Action |
| ---- | ---------- | ----------- | ------ |
| 1    | 1          | ❌          | stop   |

Head remains:

```text
1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
```

---

### Main Traversal

| Step | curr | curr.next | Equals val? | List State                        | Action      |
| ---- | ---- | --------- | ----------- | --------------------------------- | ----------- |
| Init | 1    | 2         | ❌          | `1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6` | start       |
| 1    | 1    | 2         | ❌          | `1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6` | move curr   |
| 2    | 2    | 6         | ✅          | `1 -> 2 -> 3 -> 4 -> 5 -> 6`      | remove 6    |
| 3    | 2    | 3         | ❌          | `1 -> 2 -> 3 -> 4 -> 5 -> 6`      | move curr   |
| 4    | 3    | 4         | ❌          | `1 -> 2 -> 3 -> 4 -> 5 -> 6`      | move curr   |
| 5    | 4    | 5         | ❌          | `1 -> 2 -> 3 -> 4 -> 5 -> 6`      | move curr   |
| 6    | 5    | 6         | ✅          | `1 -> 2 -> 3 -> 4 -> 5`           | remove 6    |
| Done | —    | —         | —           | `1 -> 2 -> 3 -> 4 -> 5`           | return head |

---

# Dry Run (Important Edge Case)

### Input

```js
head = [7, 7, 7, 7];
val = 7;
```

### Removing From Head

| Step | Head Value | Action    |
| ---- | ---------- | --------- |
| 1    | 7          | move head |
| 2    | 7          | move head |
| 3    | 7          | move head |
| 4    | 7          | move head |
| Done | null       | stop      |

Final List:

```text
null
```

Return:

```js
[];
```

---

# Visual Removal

Removing a middle node:

```text
Before

2 ----> 6 ----> 3

After

2 ------------> 3
```

Removing a tail node:

```text
Before

5 ----> 6 ----> null

After

5 ------------> null
```

---

# Why We Don't Move curr After Deletion

Suppose:

```text
1 -> 6 -> 6 -> 3
```

Current node:

```text
curr = 1
```

After removing first `6`:

```text
1 -> 6 -> 3
```

If we immediately move `curr` forward, the second `6` would be skipped.

That's why after deletion:

```js
curr.next = curr.next.next;
```

we stay at the same `curr` and check again.

---

# Complexity Analysis

### Time Complexity

```text
O(n)
```

- Head adjustment takes at most `n` steps.
- Traversal takes at most `n` steps.
- Overall still `O(n)`.

### Space Complexity

```text
O(1)
```

Only one pointer (`curr`) is used.

---

# Key Takeaways

- This solution handles head deletions separately.
- First remove all matching nodes from the beginning of the list.
- After that, normal linked list deletion becomes easy.
- To delete a node:
  ```js
  curr.next = curr.next.next;
  ```
- After deletion, do not move `curr`.
- Move `curr` only when no deletion happens.
- This approach avoids using a dummy/sentinel node.
  ```**````**
