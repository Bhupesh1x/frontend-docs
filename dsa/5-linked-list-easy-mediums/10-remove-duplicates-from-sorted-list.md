# Remove Duplicates from Sorted List

## Problem

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.

Return the linked list in sorted order.

### Example

```js
Input: head = [1, 1, 2];
Output: [1, 2];
```

```js
Input: head = [1, 1, 2, 3, 3];
Output: [1, 2, 3];
```

---

# Code

```js
var deleteDuplicates = function (head) {
  let curr = head;

  while (curr && curr.next) {
    if (curr.val == curr.next.val) {
      curr.next = curr.next.next;
    } else {
      curr = curr.next;
    }
  }

  return head;
};
```

---

# Intuition

Since the linked list is already sorted, duplicate values will always be next to each other.

Example:

```text
1 -> 1 -> 2 -> 3 -> 3
```

Notice:

```text
Duplicate values are adjacent.
```

So we only need to compare:

```js
curr.val;
```

with

```js
curr.next.val;
```

If both are equal:

- Remove the next node.

Otherwise:

- Move forward.

---

# Approach

### Step 1: Start from Head

```js
let curr = head;
```

---

### Step 2: Compare Current and Next Node

If values are equal:

```js
curr.val === curr.next.val;
```

remove the duplicate.

---

### Step 3: Remove Duplicate

```js
curr.next = curr.next.next;
```

This skips the duplicate node.

---

### Step 4: Move Forward

If values are different:

```js
curr = curr.next;
```

---

### Step 5: Return Head

The original head remains unchanged.

```js
return head;
```

---

# Dry Run

### Input

```js
head = [1, 1, 2, 3, 3];
```

Initial List:

```text
1 -> 1 -> 2 -> 3 -> 3
```

---

## Traversal

| Step | curr | curr.next | Equal? | List State              | Action           |
| ---- | ---- | --------- | ------ | ----------------------- | ---------------- |
| Init | 1    | 1         | ✅     | `1 -> 1 -> 2 -> 3 -> 3` | start            |
| 1    | 1    | 1         | ✅     | `1 -> 2 -> 3 -> 3`      | remove duplicate |
| 2    | 1    | 2         | ❌     | `1 -> 2 -> 3 -> 3`      | move curr        |
| 3    | 2    | 3         | ❌     | `1 -> 2 -> 3 -> 3`      | move curr        |
| 4    | 3    | 3         | ✅     | `1 -> 2 -> 3`           | remove duplicate |
| Done | 3    | null      | —      | `1 -> 2 -> 3`           | return head      |

---

# Visual Explanation

### Removing First Duplicate

Before:

```text
1 -> 1 -> 2
```

Current:

```text
curr
 |
 v
1 -> 1 -> 2
```

Operation:

```js
curr.next = curr.next.next;
```

After:

```text
1 -------> 2
```

Result:

```text
1 -> 2
```

---

### Removing Last Duplicate

Before:

```text
3 -> 3 -> null
```

Operation:

```js
curr.next = curr.next.next;
```

After:

```text
3 -------> null
```

Result:

```text
3
```

---

# Why Don't We Move curr After Removing?

Consider:

```text
1 -> 1 -> 1 -> 2
```

Current:

```text
curr = first 1
```

After removing one duplicate:

```text
1 -> 1 -> 2
```

There is still another duplicate.

If we move `curr` immediately:

```js
curr = curr.next;
```

we might skip checking it.

So after deletion:

```js
curr.next = curr.next.next;
```

we stay on the same node and check again.

---

# Dry Run (Multiple Duplicates)

### Input

```js
head = [1, 1, 1, 1, 2];
```

Initial List:

```text
1 -> 1 -> 1 -> 1 -> 2
```

| Step | curr | curr.next | Action | List State         |
| ---- | ---- | --------- | ------ | ------------------ |
| 1    | 1    | 1         | remove | `1 -> 1 -> 1 -> 2` |
| 2    | 1    | 1         | remove | `1 -> 1 -> 2`      |
| 3    | 1    | 1         | remove | `1 -> 2`           |
| 4    | 1    | 2         | move   | `1 -> 2`           |
| Done | 2    | null      | return | `1 -> 2`           |

---

# Why Sorting Matters

This solution works because the list is sorted.

Example:

```text
1 -> 1 -> 2 -> 3 -> 3
```

Duplicates are adjacent.

But if the list were:

```text
1 -> 3 -> 1 -> 2
```

the duplicates are not next to each other.

Comparing only adjacent nodes would not work.

That's why the problem specifically says:

```text
Sorted Linked List
```

---

# Complexity Analysis

### Time Complexity

```text
O(n)
```

Each node is visited at most once.

---

### Space Complexity

```text
O(1)
```

Only one pointer (`curr`) is used.

---

# Key Takeaways

- The list is sorted, so duplicates are always next to each other.
- Compare only adjacent nodes.
- If values are equal:
  ```js
  curr.next = curr.next.next;
  ```
- After deletion, do not move `curr`.
- Move `curr` only when values are different.
- No extra space is needed.
- This is a classic linked list deletion problem.
