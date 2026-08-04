# Swap Nodes in Pairs

## Problem

Given a linked list, swap every two adjacent nodes and return the new head.

You must swap the nodes themselves, not just their values.

### Example

```js
Input: head = [1, 2, 3, 4];
Output: [2, 1, 4, 3];
```

```js
Input: head = [1, 2, 3];
Output: [2, 1, 3];
```

---

# Intuition

We need to swap every pair of adjacent nodes.

Example:

```text
1 -> 2 -> 3 -> 4
```

becomes

```text
2 -> 1 -> 4 -> 3
```

Instead of swapping values, we change the links between nodes.

To make pointer updates easier (especially when swapping the first pair), we use a **sentinel (dummy) node**.

---

# Core Idea

For every pair:

```text
Previous -> Current -> Next -> Remaining
```

Convert it into:

```text
Previous -> Next -> Current -> Remaining
```

Then move to the next pair.

---

# Approach

### Step 1: Handle Edge Cases

If there are fewer than two nodes:

```js
if (!head || !head.next) return head;
```

Nothing needs to be swapped.

---

### Step 2: Create Sentinel Node

```text
sentinel -> head
```

This helps swap the first pair without special handling.

---

### Step 3: Create Three Pointers

```js
p = sentinel;
c = head;
n = head.next;
```

Where:

- `p` = previous node
- `c` = current node (first node of pair)
- `n` = next node (second node of pair)

Example:

```text
sentinel -> 1 -> 2 -> 3 -> 4
             ^    ^
             c    n

p
```

---

### Step 4: Swap the Pair

#### Connect previous to second node

```js
p.next = n;
```

#### Connect first node to remaining list

```js
c.next = n.next;
```

#### Connect second node back to first

```js
n.next = c;
```

The pair is now swapped.

---

### Step 5: Move to Next Pair

Move pointers forward.

```js
p = c;
c = p.next;
n = c?.next;
```

Repeat until no complete pair remains.

---

# Dry Run

### Input

```js
head = [1, 2, 3, 4];
```

Initial List:

```text
sentinel -> 1 -> 2 -> 3 -> 4
```

Pointers:

```text
p = sentinel
c = 1
n = 2
```

---

## Iteration 1

Current:

```text
sentinel -> 1 -> 2 -> 3 -> 4
              c    n
```

### Step 1

```js
p.next = n;
```

```text
sentinel -> 2
```

---

### Step 2

```js
c.next = n.next;
```

```text
1 -> 3
```

---

### Step 3

```js
n.next = c;
```

Result:

```text
sentinel -> 2 -> 1 -> 3 -> 4
```

---

### Move Pointers

```text
p = 1
c = 3
n = 4
```

---

## Iteration 2

Current:

```text
sentinel -> 2 -> 1 -> 3 -> 4
                         c    n
```

### Step 1

```js
p.next = n;
```

### Step 2

```js
c.next = n.next;
```

### Step 3

```js
n.next = c;
```

Result:

```text
sentinel -> 2 -> 1 -> 4 -> 3
```

---

### Move Pointers

```text
p = 3
c = null
n = null
```

Loop ends.

Return:

```text
2 -> 1 -> 4 -> 3
```

---

# Dry Run Table

| Step   | p        | c    | n    | List State         |
| ------ | -------- | ---- | ---- | ------------------ |
| Init   | sentinel | 1    | 2    | `1 -> 2 -> 3 -> 4` |
| Swap 1 | 1        | 3    | 4    | `2 -> 1 -> 3 -> 4` |
| Swap 2 | 3        | null | null | `2 -> 1 -> 4 -> 3` |
| Done   | —        | —    | —    | `2 -> 1 -> 4 -> 3` |

---

# Visual Explanation

### Before Swap

```text
p
|
v

1 -> 2 -> 3

^    ^
c    n
```

---

### Step 1

```js
p.next = n;
```

```text
p
|
v

2

1 -> 3
```

---

### Step 2

```js
c.next = n.next;
```

```text
1 -> 3
```

---

### Step 3

```js
n.next = c;
```

Final:

```text
2 -> 1 -> 3
```

---

# Dry Run (Odd Number of Nodes)

### Input

```js
head = [1, 2, 3];
```

Swap first pair:

```text
1 -> 2 -> 3
```

becomes

```text
2 -> 1 -> 3
```

Now:

```text
c = 3
n = null
```

Loop stops because there is no second node to swap.

Return:

```text
2 -> 1 -> 3
```

---

# Why Use a Sentinel Node?

Without a sentinel:

```text
1 -> 2 -> 3
```

After swapping:

```text
2 -> 1 -> 3
```

The head changes from:

```text
1
```

to

```text
2
```

This requires special handling.

With a sentinel:

```text
sentinel -> 1 -> 2 -> 3
```

We simply do:

```js
p.next = n;
```

No extra condition is needed.

---

# Code

```js
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

    p = c;
    c = p.next;
    n = c?.next && c?.next;
  }

  return sentinel.next;
};
```

---

# Complexity Analysis

### Time Complexity

```text
O(n)
```

Each node is visited only once.

---

### Space Complexity

```text
O(1)
```

Only a few pointers are used.

---

# Pointer Update Order (Very Important)

Always perform the updates in this order:

```js
p.next = n;
c.next = n.next;
n.next = c;
```

Changing the order can break the links and lose part of the list.

---

# Key Takeaways

- Swap nodes, not their values.
- A sentinel node makes swapping the first pair easy.
- Maintain three pointers:
  - `p` → previous node
  - `c` → first node of the pair
  - `n` → second node of the pair
- Swap pointers in this order:
  ```js
  p.next = n;
  c.next = n.next;
  n.next = c;
  ```
- Move all pointers to the next pair and repeat.
- Stop when fewer than two nodes remain.
- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
