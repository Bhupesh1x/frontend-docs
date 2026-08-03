# Rotate List

## Problem

Given the head of a linked list, rotate the list to the right by `k` places.

### Example

```js
Input: ((head = [1, 2, 3, 4, 5]), (k = 2));
Output: [4, 5, 1, 2, 3];
```

```js
Input: ((head = [0, 1, 2]), (k = 4));
Output: [2, 0, 1];
```

---

# Code

```js
var rotateRight = function (head, k) {
  if (!head || !head.next || !k) return head;

  let length = 0;
  let curr = head;

  while (curr) {
    curr = curr.next;
    length++;
  }

  k = k % length;

  let slow = head;
  let fast = head;

  for (let i = 0; i < k; i++) {
    fast = fast.next;
  }

  while (fast.next) {
    slow = slow.next;
    fast = fast.next;
  }

  fast.next = head;
  head = slow.next;
  slow.next = null;

  return head;
};
```

---

# Intuition

Rotating right by `k` means taking the last `k` nodes and moving them to the front.

Example:

```text
1 -> 2 -> 3 -> 4 -> 5
```

Rotate by:

```text
k = 2
```

Take:

```text
4 -> 5
```

Move them to the front:

```text
4 -> 5 -> 1 -> 2 -> 3
```

The tricky part is finding where to cut the list.

---

# Important Observation

If:

```text
length = 5
k = 7
```

Rotating 7 times is the same as rotating:

```text
7 % 5 = 2
```

times.

So first:

```js
k = k % length;
```

This avoids unnecessary rotations.

---

# Core Idea

Maintain a gap of `k` nodes between two pointers.

When:

```text
fast reaches the last node
```

then:

```text
slow reaches the node just before
the new head.
```

After that:

1. Connect tail to head.
2. Make the new head.
3. Break the list.

---

# Approach

### Step 1: Handle Edge Cases

```js
if (!head || !head.next || !k) return head;
```

Nothing to rotate.

---

### Step 2: Find Length

Traverse the list and count nodes.

```js
length++;
```

---

### Step 3: Reduce k

```js
k = k % length;
```

Example:

```text
length = 5
k = 12
```

becomes:

```text
k = 2
```

---

### Step 4: Create Two Pointers

```js
slow = head;
fast = head;
```

---

### Step 5: Move Fast k Steps Ahead

```js
for (let i = 0; i < k; i++) {
  fast = fast.next;
}
```

Now the distance between them is:

```text
k nodes
```

---

### Step 6: Move Both Together

Move until:

```js
fast.next === null;
```

When this happens:

```text
fast = last node
slow = node before new head
```

---

### Step 7: Make Circular List

```js
fast.next = head;
```

Now:

```text
tail -> head
```

---

### Step 8: Find New Head

```js
head = slow.next;
```

---

### Step 9: Break the Circle

```js
slow.next = null;
```

---

# Dry Run

### Input

```js
head = [1, 2, 3, 4, 5];
k = 2;
```

Initial List:

```text
1 -> 2 -> 3 -> 4 -> 5
```

---

## Find Length

| Node | Length |
| ---- | ------ |
| 1    | 1      |
| 2    | 2      |
| 3    | 3      |
| 4    | 4      |
| 5    | 5      |

Final:

```js
length = 5;
```

---

## Reduce k

```js
k = 2 % 5;
```

```js
k = 2;
```

---

## Move Fast k Steps

Initial:

```text
S,F
 |
1 -> 2 -> 3 -> 4 -> 5
```

Move 1 step:

```text
S
|
1 -> 2 -> 3 -> 4 -> 5
     ^
     F
```

Move 2 steps:

```text
S
|
1 -> 2 -> 3 -> 4 -> 5
          ^
          F
```

Gap:

```text
2 nodes
```

---

## Move Both Together

### Step 1

```text
S -> 2
F -> 4
```

### Step 2

```text
S -> 3
F -> 5
```

Stop because:

```js
fast.next === null;
```

Current position:

```text
1 -> 2 -> 3 -> 4 -> 5
          ^         ^
        slow      fast
```

---

## Create Circular List

```js
fast.next = head;
```

Result:

```text
1 -> 2 -> 3 -> 4 -> 5
^                   |
|___________________|
```

---

## New Head

```js
head = slow.next;
```

```text
head = 4
```

---

## Break Circle

```js
slow.next = null;
```

Result:

```text
4 -> 5 -> 1 -> 2 -> 3
```

Return:

```js
[4, 5, 1, 2, 3];
```

---

# Dry Run Table

| Step        | slow | fast |
| ----------- | ---- | ---- |
| Init        | 1    | 1    |
| Fast Move 1 | 1    | 2    |
| Fast Move 2 | 1    | 3    |
| Move Both 1 | 2    | 4    |
| Move Both 2 | 3    | 5    |
| Stop        | 3    | 5    |

New head:

```text
slow.next = 4
```

---

# Visual Explanation

### Original

```text
1 -> 2 -> 3 -> 4 -> 5
```

### Tail Connected To Head

```text
1 -> 2 -> 3 -> 4 -> 5
^                   |
|___________________|
```

### Cut After 3

```text
4 -> 5 -> 1 -> 2 -> 3
```

---

# Dry Run (k Greater Than Length)

### Input

```js
head = [0, 1, 2];
k = 4;
```

Length:

```js
3;
```

Reduce:

```js
k = 4 % 3;
```

```js
k = 1;
```

Now rotate only once.

Original:

```text
0 -> 1 -> 2
```

Move last node to front:

```text
2 -> 0 -> 1
```

Return:

```js
[2, 0, 1];
```

---

# Why Does The Two Pointer Trick Work?

Suppose:

```text
1 -> 2 -> 3 -> 4 -> 5
```

and

```js
k = 2;
```

Keep:

```text
fast
```

ahead by:

```text
2 nodes
```

When fast reaches:

```text
5
```

slow automatically reaches:

```text
3
```

And:

```text
3.next = 4
```

which is exactly the new head after rotation.

---

# Complexity Analysis

### Time Complexity

```text
O(n)
```

- One pass to find length.
- One pass using slow and fast pointers.

Overall:

```text
O(n)
```

---

### Space Complexity

```text
O(1)
```

Only a few pointers are used.

---

# Key Takeaways

- Rotating right means moving the last `k` nodes to the front.
- First reduce rotations using:
  ```js
  k = k % length;
  ```
- Keep a gap of `k` nodes between slow and fast.
- When fast reaches the end:
  ```text
  slow is before the new head
  ```
- Connect tail to head to form a circle.
- New head is:
  ```js
  slow.next;
  ```
- Break the circle using:
  ```js
  slow.next = null;
  ```
- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
