# Odd Even Linked List

## Problem

Given the head of a singly linked list, group all nodes at odd indices together followed by all nodes at even indices.

The relative order inside the odd group and inside the even group must remain the same.

### Example

```js
Input: head = [1, 2, 3, 4, 5];
Output: [1, 3, 5, 2, 4];
```

```js
Input: head = [2, 1, 3, 5, 6, 4, 7];
Output: [2, 3, 6, 7, 1, 5, 4];
```

---

# Code

```js
var oddEvenList = function (head) {
  if (!head || !head.next) return head;

  let odd = head;
  let even = head.next;

  let evenStart = even;

  while (odd.next && even.next) {
    odd.next = odd.next.next;
    even.next = even.next.next;

    odd = odd.next;
    even = even.next;
  }

  odd.next = evenStart;

  return head;
};
```

---

# Intuition

The important thing to notice is:

```text
We are grouping by position (index),
not by node value.
```

For:

```text
1 -> 2 -> 3 -> 4 -> 5
```

Indices are:

```text
1st -> 1 (Odd)
2nd -> 2 (Even)
3rd -> 3 (Odd)
4th -> 4 (Even)
5th -> 5 (Odd)
```

We want:

```text
Odd nodes  : 1 -> 3 -> 5
Even nodes : 2 -> 4
```

Then combine them:

```text
1 -> 3 -> 5 -> 2 -> 4
```

Instead of creating new lists, we can rearrange the existing pointers.

---

# Core Idea

Maintain two chains:

```text
Odd Chain
1 -> 3 -> 5
```

```text
Even Chain
2 -> 4
```

Store the start of the even chain.

At the end:

```text
Odd Chain + Even Chain
```

---

# Approach

### Step 1: Handle Edge Cases

If there are fewer than 2 nodes:

```js
if (!head || !head.next) return head;
```

Nothing needs to be changed.

---

### Step 2: Create Odd and Even Pointers

```js
odd = head;
even = head.next;
```

Example:

```text
1 -> 2 -> 3 -> 4 -> 5
^    ^
odd  even
```

---

### Step 3: Save Start of Even List

```js
evenStart = even;
```

We will need it later to connect both lists.

---

### Step 4: Separate Odd and Even Nodes

Odd skips over even:

```js
odd.next = odd.next.next;
```

Even skips over odd:

```js
even.next = even.next.next;
```

Then move both pointers forward.

---

### Step 5: Connect Odd and Even Lists

At the end:

```js
odd.next = evenStart;
```

---

# Dry Run

### Input

```js
head = [1, 2, 3, 4, 5];
```

Initial List:

```text
1 -> 2 -> 3 -> 4 -> 5
```

Pointers:

```text
odd = 1
even = 2
evenStart = 2
```

---

## Iteration 1

Current:

```text
1 -> 2 -> 3 -> 4 -> 5
^    ^
odd  even
```

### Update Odd

```js
odd.next = odd.next.next;
```

```text
1 -------> 3 -> 4 -> 5
```

List becomes:

```text
1 -> 3 -> 4 -> 5
2 -> 3 -> 4 -> 5
```

---

### Update Even

```js
even.next = even.next.next;
```

```text
2 -------> 4 -> 5
```

Now:

```text
Odd Chain:
1 -> 3 -> 4 -> 5

Even Chain:
2 -> 4 -> 5
```

---

### Move Pointers

```js
odd = odd.next;
even = even.next;
```

```text
1 -> 3 -> 4 -> 5
     ^

2 -> 4 -> 5
     ^
```

```text
odd = 3
even = 4
```

---

## Iteration 2

Current:

```text
1 -> 3 -> 4 -> 5
     ^

2 -> 4 -> 5
     ^
```

### Update Odd

```js
odd.next = odd.next.next;
```

```text
3 -------> 5
```

Odd chain:

```text
1 -> 3 -> 5
```

---

### Update Even

```js
even.next = even.next.next;
```

```text
4 -------> null
```

Even chain:

```text
2 -> 4
```

---

### Move Pointers

```text
odd = 5
even = null
```

Loop stops.

---

## Connect Both Lists

Before:

```text
Odd Chain:
1 -> 3 -> 5

Even Chain:
2 -> 4
```

Operation:

```js
odd.next = evenStart;
```

After:

```text
1 -> 3 -> 5 -> 2 -> 4
```

Return:

```js
[1, 3, 5, 2, 4];
```

---

# Dry Run Table

| Step    | odd | even | Odd Chain               | Even Chain |
| ------- | --- | ---- | ----------------------- | ---------- |
| Init    | 1   | 2    | `1`                     | `2`        |
| 1       | 3   | 4    | `1 -> 3`                | `2 -> 4`   |
| 2       | 5   | null | `1 -> 3 -> 5`           | `2 -> 4`   |
| Connect | —   | —    | `1 -> 3 -> 5 -> 2 -> 4` | Done       |

---

# Visual Explanation

### Original List

```text
1 -> 2 -> 3 -> 4 -> 5
```

Separate into:

```text
Odd:
1 -> 3 -> 5
```

```text
Even:
2 -> 4
```

Combine:

```text
1 -> 3 -> 5 -> 2 -> 4
```

---

# Why Do We Store evenStart?

During traversal:

```text
even moves forward
```

Eventually:

```text
even = null
```

If we don't save the first even node:

```js
evenStart = even;
```

we lose the starting point of the even list.

Then we cannot attach it to the odd list later.

---

# Complexity Analysis

### Time Complexity

```text
O(n)
```

Each node is visited once.

---

### Space Complexity

```text
O(1)
```

No extra list is created.

Only a few pointers are used.

---

# Key Takeaways

- Group nodes by index, not by value.
- Maintain two separate chains:
  - Odd chain
  - Even chain
- Save the start of the even chain.
- Odd pointer skips even nodes.
- Even pointer skips odd nodes.
- At the end:
  ```js
  odd.next = evenStart;
  ```
- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
- This is a pointer manipulation problem, not a value swapping problem.
