# Swap Nodes in Pairs (Recursive)

## Problem

Given a linked list, swap every two adjacent nodes and return the new head.

You must swap the nodes themselves, not just their values.

### Example

```js
Input: head = [1,2,3,4]
Output: [2,1,4,3]
```

```js
Input: head = [1,2,3]
Output: [2,1,3]
```

---

# Intuition

Instead of swapping the entire list at once, recursion lets us solve one pair at a time.

For every recursive call:

1. Swap the first two nodes.
2. Ask recursion to swap the remaining list.
3. Attach the swapped remaining list back.
4. Return the new head of the current pair.

Think of it like this:

```text
Swap first pair

↓

Recursively swap remaining list

↓

Connect both results
```

---

# Core Idea

For every pair:

```text
l -> r -> Remaining List
```

Recursively swap the remaining list first.

Then make:

```text
r -> l -> Swapped Remaining List
```

Return:

```text
r
```

because it becomes the new head of this pair.

---

# Approach

### Step 1: Base Case

If there are fewer than two nodes:

```js
if (!head || !head.next) return head;
```

Nothing needs to be swapped.

---

### Step 2: Store First Two Nodes

```js
l = head;
r = head.next;
```

Example:

```text
1 -> 2 -> 3 -> 4

l = 1
r = 2
```

---

### Step 3: Recursively Swap Remaining List

Swap everything after `r`.

```js
l.next = swapPairs(r.next);
```

For the example:

```text
swapPairs(3 -> 4)
```

returns

```text
4 -> 3
```

Now:

```text
1 -> 4 -> 3
```

---

### Step 4: Complete Current Swap

Make the second node point to the first.

```js
r.next = l;
```

Now:

```text
2 -> 1 -> 4 -> 3
```

---

### Step 5: Return New Head

Return:

```js
return r;
```

because `r` is now the first node of the swapped pair.

---

# Dry Run

### Input

```js
head = [1,2,3,4]
```

Initial List:

```text
1 -> 2 -> 3 -> 4
```

---

## Recursive Calls

### Call 1

Current List:

```text
1 -> 2 -> 3 -> 4
```

```text
l = 1
r = 2
```

Need:

```text
swapPairs(3 -> 4)
```

---

### Call 2

Current List:

```text
3 -> 4
```

```text
l = 3
r = 4
```

Need:

```text
swapPairs(null)
```

---

### Call 3

Input:

```text
null
```

Base case:

```js
return null;
```

---

## Returning Back

### Return to Call 2

Current:

```text
3 -> 4
```

Step 1

```js
l.next = null;
```

Step 2

```js
r.next = l;
```

Result:

```text
4 -> 3
```

Return:

```text
4
```

---

### Return to Call 1

Current:

```text
1 -> 2
```

Recursive result:

```text
4 -> 3
```

Step 1

```js
l.next = 4;
```

Now:

```text
1 -> 4 -> 3
```

Step 2

```js
r.next = l;
```

Result:

```text
2 -> 1 -> 4 -> 3
```

Return:

```text
2
```

Final Answer:

```text
2 -> 1 -> 4 -> 3
```

---

# Dry Run Table

| Recursive Call | Current Pair | Recursive Result | Returned List |
|----------------|--------------|------------------|---------------|
| 3 | `null` | Base Case | `null` |
| 2 | `3 -> 4` | `null` | `4 -> 3` |
| 1 | `1 -> 2` | `4 -> 3` | `2 -> 1 -> 4 -> 3` |

---

# Visual Explanation

### Original

```text
1 -> 2 -> 3 -> 4
```

---

### Swap Remaining First

```text
swapPairs(3 -> 4)

↓

4 -> 3
```

---

### Attach Remaining

```text
1 -> 4 -> 3
```

---

### Swap Current Pair

```text
2 -> 1 -> 4 -> 3
```

---

# Recursion Tree

```text
swapPairs(1)

│
├── swapPairs(3)
│
│   ├── swapPairs(null)
│   │
│   └── returns 4 -> 3
│
└── returns 2 -> 1 -> 4 -> 3
```

---

# Dry Run (Odd Number of Nodes)

### Input

```js
head = [1,2,3]
```

Call 1:

```text
1 -> 2
```

Needs:

```text
swapPairs(3)
```

Since:

```text
3
```

has no partner,

Base case returns:

```text
3
```

Current swap:

```text
2 -> 1 -> 3
```

Return:

```text
2 -> 1 -> 3
```

---

# Why Do We Return `r`?

Initially:

```text
1 -> 2
```

After swapping:

```text
2 -> 1
```

The head of this pair changes from:

```text
1
```

to

```text
2
```

So every recursive call returns:

```js
return r;
```

because `r` becomes the new head of the swapped pair.

---

# Code

```js
var swapPairs = function (head) {
  if (!head || !head.next) return head;

  let l = head;
  let r = head.next;

  l.next = swapPairs(r.next);
  r.next = l;

  return r;
};
```

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
O(n)
```

Because of the recursive call stack.

---

# Recursive Flow Summary

For every recursive call:

```text
Current Pair

↓

Swap Remaining List

↓

Attach Remaining List

↓

Swap Current Pair

↓

Return New Head
```

---

# Key Takeaways

- Solve one pair at a time using recursion.
- First recursively swap the remaining list.
- Connect the first node to the swapped remaining list:
  ```js
  l.next = swapPairs(r.next);
  ```
- Complete the current swap:
  ```js
  r.next = l;
  ```
- Return `r` because it becomes the new head of the current pair.
- Base case is when there are fewer than two nodes.
- Time Complexity: `O(n)`
- Space Complexity: `O(n)` (recursive call stack)