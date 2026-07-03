# Middle of a Linked List

## Problem

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

### Example

```js
Input: head = [1, 2, 3, 4, 5];
Output: [3, 4, 5];
```

---

## Intuition

We need to find the middle node without counting all nodes first.

A simple idea is:

- Use one pointer that moves slowly (`slow`)
- Use another pointer that moves fast (`fast`)

While:

- `slow` moves 1 step at a time
- `fast` moves 2 steps at a time

By the time `fast` reaches the end of the list, `slow` will be standing exactly at the middle node.

This is called the **Slow and Fast Pointer** technique.

---

## Approach

1. Start both `slow` and `fast` from `head`.
2. Move:
   - `slow = slow.next`
   - `fast = fast.next.next`
3. Continue until `fast` reaches the end.
4. Return `slow`.

---

## Code

```js
var middleNode = function (head) {
  let slow = head;
  let fast = head;

  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }

  return slow;
};
```

---

## Dry Run

### Input

```js
head = [1, 2, 3, 4, 5];
```

### Linked List

```text
1 -> 2 -> 3 -> 4 -> 5 -> null
```

| Step   | slow | fast | Action                                |
| ------ | ---- | ---- | ------------------------------------- |
| Init   | 1    | 1    | Start both pointers at head           |
| 1      | 2    | 3    | slow moves 1 step, fast moves 2 steps |
| 2      | 3    | 5    | slow moves 1 step, fast moves 2 steps |
| Stop   | 3    | 5    | fast.next is null, loop ends          |
| Return | 3    | -    | return slow                           |

### Visualization

```text
Initial

S
F
1 -> 2 -> 3 -> 4 -> 5 -> null


After 1st iteration

     S
          F
1 -> 2 -> 3 -> 4 -> 5 -> null


After 2nd iteration

          S
                    F
1 -> 2 -> 3 -> 4 -> 5 -> null
```

Answer:

```text
3 -> 4 -> 5
```

---

## Dry Run (Even Length List)

### Input

```js
head = [1, 2, 3, 4, 5, 6];
```

### Linked List

```text
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
```

| Step   | slow | fast | Action                      |
| ------ | ---- | ---- | --------------------------- |
| Init   | 1    | 1    | Start both pointers at head |
| 1      | 2    | 3    | Move pointers               |
| 2      | 3    | 5    | Move pointers               |
| 3      | 4    | null | Move pointers               |
| Return | 4    | -    | return slow                 |

### Why does it return 4?

Middle nodes are:

```text
1 -> 2 -> 3 -> 4 -> 5 -> 6
          ^    ^
```

The problem asks us to return the **second middle node**, which is `4`.

---

## Why This Works

For every:

```text
1 step by slow
```

`fast` moves:

```text
2 steps
```

So `fast` covers the list twice as quickly.

When `fast` reaches the end:

```text
slow has covered only half the distance
```

which means `slow` is standing at the middle node.

---

## Time Complexity

```text
O(n)
```

We traverse the list only once.

---

## Space Complexity

```text
O(1)
```

Only two pointers are used.

---

## Pattern

```text
Slow and Fast Pointer
```

---

## Revision Notes

- Start both `slow` and `fast` from `head`.
- `slow` moves 1 step.
- `fast` moves 2 steps.
- When `fast` reaches the end, `slow` is at the middle.
- For even length lists, this automatically returns the second middle node.
- Time: `O(n)`
- Space: `O(1)`
- Classic Slow & Fast Pointer problem.
