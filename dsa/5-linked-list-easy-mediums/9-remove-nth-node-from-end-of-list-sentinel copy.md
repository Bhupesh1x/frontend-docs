# Remove Nth Node From End of List (Two Pass + Sentinel)

## Problem

Given the head of a linked list, remove the `nth` node from the end of the list and return the head.

### Example

```js
Input: ((head = [1, 2, 3, 4, 5]), (n = 2));
Output: [1, 2, 3, 5];
```

---

# Intuition

Removing a node from a linked list is easy when we know the node before it.

The problem gives us the position from the end, but linked lists can only be traversed from the beginning.

So:

1. First calculate the length of the linked list.
2. Convert the position from the end into a position from the beginning.
3. Move to the node just before the node we want to remove.
4. Skip the target node.

A sentinel (dummy) node is used so that removing the head node becomes easy and we don't need special handling.

---

# Code

```js
var removeNthFromEnd = function (head, n) {
  let sentinel = new ListNode();
  sentinel.next = head;

  let length = 0;

  let curr = head;
  while (curr) {
    curr = curr.next;
    length = length + 1;
  }

  let pos = length - n;

  let prev = sentinel;
  for (let i = 0; i < pos; i++) {
    prev = prev.next;
  }

  prev.next = prev.next.next;

  return sentinel.next;
};
```

---

# Approach

### Step 1: Create Sentinel Node

```text
sentinel -> head
```

This helps when the node to remove is the first node.

---

### Step 2: Find Length

Traverse the linked list and count nodes.

```js
length++;
```

---

### Step 3: Find Position From Start

```js
pos = length - n;
```

This gives the index of the node just before the node we want to remove.

---

### Step 4: Reach Previous Node

Start from sentinel and move `pos` times.

```js
prev = prev.next;
```

---

### Step 5: Remove Node

Skip the target node.

```js
prev.next = prev.next.next;
```

---

### Step 6: Return New Head

```js
return sentinel.next;
```

---

# Dry Run

### Input

```js
head = [1, 2, 3, 4, 5];
n = 2;
```

Initial List:

```text
sentinel -> 1 -> 2 -> 3 -> 4 -> 5
```

---

## Pass 1: Calculate Length

| Step | curr | Length |
| ---- | ---- | ------ |
| Init | 1    | 0      |
| 1    | 1    | 1      |
| 2    | 2    | 2      |
| 3    | 3    | 3      |
| 4    | 4    | 4      |
| 5    | 5    | 5      |
| Done | null | 5      |

Final Length:

```js
length = 5;
```

---

## Calculate Position

```js
pos = length - n;
```

```js
pos = 5 - 2;
```

```js
pos = 3;
```

This means we need to reach the node before the target.

---

## Pass 2: Reach Previous Node

Start from sentinel.

| Step | prev     |
| ---- | -------- |
| Init | sentinel |
| 1    | 1        |
| 2    | 2        |
| 3    | 3        |

Now:

```text
sentinel -> 1 -> 2 -> 3 -> 4 -> 5
                         ^
                        prev
```

Target node:

```text
4
```

---

## Remove Node

Before:

```text
3 -> 4 -> 5
```

Operation:

```js
prev.next = prev.next.next;
```

After:

```text
3 -------> 5
```

Full List:

```text
1 -> 2 -> 3 -> 5
```

---

# Visual Explanation

Before removal:

```text
sentinel -> 1 -> 2 -> 3 -> 4 -> 5
                         ^
                        prev
```

After:

```text
sentinel -> 1 -> 2 -> 3 -------> 5
```

Node `4` is removed.

---

# Dry Run (Removing Head)

### Input

```js
head = [1];
n = 1;
```

Initial List:

```text
sentinel -> 1
```

Length:

```js
length = 1;
```

Position:

```js
pos = length - n;
```

```js
pos = 1 - 1;
```

```js
pos = 0;
```

Since `pos = 0`, `prev` stays at sentinel.

Before:

```text
sentinel -> 1
```

Remove:

```js
prev.next = prev.next.next;
```

After:

```text
sentinel -> null
```

Return:

```js
[];
```

This is exactly why the sentinel node is useful.

---

# Why Use a Sentinel Node?

Without a sentinel:

```text
1 -> 2 -> 3
```

If we remove `1`, the head changes.

We would need special logic.

With a sentinel:

```text
sentinel -> 1 -> 2 -> 3
```

We always remove using:

```js
prev.next = prev.next.next;
```

No special case needed.

---

# Complexity Analysis

### Time Complexity

```text
O(n)
```

- First pass to find length → `O(n)`
- Second pass to reach previous node → `O(n)`

Overall:

```text
O(n)
```

---

### Space Complexity

```text
O(1)
```

Only a few pointers and variables are used.

---

# Key Takeaways

- Linked lists cannot move backward, so first find the length.
- Convert "nth from end" into a position from the beginning.
- Use a sentinel node to handle head deletion easily.
- To remove a node:
  ```js
  prev.next = prev.next.next;
  ```
- `pos = length - n` gives how many steps to move from sentinel.
- Two-pass solution is simple and easy to understand.
