# Reverse a Linked List

## Problem

Given the head of a singly linked list, reverse the list and return the new head.

### Example

```js
Input: head = [1, 2, 3, 4, 5];
Output: [5, 4, 3, 2, 1];
```

---

## Intuition

While reversing a linked list, the biggest challenge is:

```text
If we change a node's next pointer, we might lose the rest of the list.
```

For example:

```text
1 -> 2 -> 3 -> 4 -> 5
```

If we directly do:

```js
1.next = null;
```

then we lose access to:

```text
2 -> 3 -> 4 -> 5
```

To avoid this, we first save the next node in a temporary variable.

Then:

1. Save next node
2. Reverse the current link
3. Move pointers forward

---

## Approach

We use three pointers:

- `prev` → previous node
- `curr` → current node
- `temp` → stores next node

For every node:

1. Store `curr.next` inside `temp`
2. Reverse the link (`curr.next = prev`)
3. Move `prev` forward
4. Move `curr` forward

At the end:

- `curr` becomes `null`
- `prev` points to the new head

Return `prev`.

---

## Code

```js
var reverseList = function (head) {
  let prev = null;
  let curr = head;

  while (curr !== null) {
    let temp = curr.next;

    curr.next = prev;

    prev = curr;
    curr = temp;
  }

  head = prev;
  return head;
};
```

---

## Dry Run

### Input

```js
head = [1, 2, 3, 4, 5];
```

### Initial List

```text
1 -> 2 -> 3 -> 4 -> 5 -> null
```

| Step | prev | curr | temp | Action                 |
| ---- | ---- | ---- | ---- | ---------------------- |
| Init | null | 1    | -    | Start                  |
| 1    | null | 1    | 2    | Save next node         |
| 1    | 1    | 2    | 2    | Reverse link: 1 → null |
| 2    | 1    | 2    | 3    | Save next node         |
| 2    | 2    | 3    | 3    | Reverse link: 2 → 1    |
| 3    | 2    | 3    | 4    | Save next node         |
| 3    | 3    | 4    | 4    | Reverse link: 3 → 2    |
| 4    | 3    | 4    | 5    | Save next node         |
| 4    | 4    | 5    | 5    | Reverse link: 4 → 3    |
| 5    | 4    | 5    | null | Save next node         |
| 5    | 5    | null | null | Reverse link: 5 → 4    |
| Done | 5    | null | -    | Return prev            |

---

## Step-by-Step Visualization

### Initial

```text
prev = null
curr = 1

1 -> 2 -> 3 -> 4 -> 5 -> null
^
curr
```

---

### Iteration 1

Store next node:

```text
temp = 2
```

Reverse link:

```text
1 -> null

prev = 1
curr = 2
```

Current state:

```text
Reversed Part:
1 -> null

Remaining Part:
2 -> 3 -> 4 -> 5 -> null
```

---

### Iteration 2

Store next node:

```text
temp = 3
```

Reverse link:

```text
2 -> 1 -> null

prev = 2
curr = 3
```

Current state:

```text
Reversed Part:
2 -> 1 -> null

Remaining Part:
3 -> 4 -> 5 -> null
```

---

### Iteration 3

Store next node:

```text
temp = 4
```

Reverse link:

```text
3 -> 2 -> 1 -> null

prev = 3
curr = 4
```

Current state:

```text
Reversed Part:
3 -> 2 -> 1 -> null

Remaining Part:
4 -> 5 -> null
```

---

### Iteration 4

Store next node:

```text
temp = 5
```

Reverse link:

```text
4 -> 3 -> 2 -> 1 -> null

prev = 4
curr = 5
```

Current state:

```text
Reversed Part:
4 -> 3 -> 2 -> 1 -> null

Remaining Part:
5 -> null
```

---

### Iteration 5

Store next node:

```text
temp = null
```

Reverse link:

```text
5 -> 4 -> 3 -> 2 -> 1 -> null

prev = 5
curr = null
```

Loop ends.

---

## Final Result

```text
5 -> 4 -> 3 -> 2 -> 1 -> null
```

Return:

```js
prev;
```

which points to:

```text
5
```

---

## Why We Need temp?

Without:

```js
let temp = curr.next;
```

when we do:

```js
curr.next = prev;
```

the original next node gets lost.

Example:

```text
1 -> 2 -> 3
```

After:

```js
1.next = null;
```

we can no longer reach:

```text
2 -> 3
```

That's why we save:

```js
curr.next;
```

before reversing the link.

---

## Why This Works

At every step:

```text
prev stores the already reversed part
curr stores the current node being processed
temp stores the remaining list
```

So we never lose access to any node.

When the loop finishes:

```text
curr = null
```

and

```text
prev
```

points to the completely reversed list.

---

## Time Complexity

```text
O(n)
```

Each node is visited exactly once.

---

## Space Complexity

```text
O(1)
```

Only a few pointers are used.

---

## Pattern

```text
Linked List Pointer Manipulation
```

This pattern is commonly used in:

- Reverse Linked List
- Reverse Linked List II
- Reverse Nodes in K Group
- Palindrome Linked List
- Reorder List

---

## Revision Notes

- Use three pointers:
  - `prev`
  - `curr`
  - `temp`
- Save next node before changing links.
- Reverse link using:

```js
curr.next = prev;
```

- Move pointers forward.
- At the end, `prev` becomes the new head.
- Return `prev`.
- Time: `O(n)`
- Space: `O(1)`
- Most important step:

```js
let temp = curr.next;
```

Otherwise the remaining list will be lost.
