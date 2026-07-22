# Remove Nth Node From End of List (One Pass + Two Pointers + Sentinel)

## Problem

Given the head of a linked list, remove the `nth` node from the end of the list and return the head.

### Example

```js
Input: ((head = [1, 2, 3, 4, 5]), (n = 2));
Output: [1, 2, 3, 5];
```

---

# Intuition

Instead of calculating the length first, we can use two pointers.

The idea is:

- Keep `firstPointer` ahead by `n` nodes.
- Start `secondPointer` from the beginning.
- Move both pointers together.
- When `firstPointer` reaches the end, `secondPointer` will be standing just before the node we need to remove.

A sentinel node is used so that removing the head node becomes easy.

---

# Code

```js
var removeNthFromEnd = function (head, n) {
  let sentinel = new ListNode();
  sentinel.next = head;

  let secondPointer = sentinel;
  let firstPointer = sentinel;

  for (let i = 0; i < n; i++) {
    firstPointer = firstPointer?.next;
  }

  while (firstPointer && firstPointer?.next) {
    firstPointer = firstPointer?.next;
    secondPointer = secondPointer?.next;
  }

  secondPointer.next = secondPointer?.next?.next;

  return sentinel.next;
};
```

---

# Core Idea

Maintain a gap of `n` nodes between both pointers.

```text
Gap = n
```

When the front pointer reaches the end:

```text
firstPointer -> end

secondPointer -> node before target
```

Now we can remove the target node easily.

---

# Approach

### Step 1: Create Sentinel Node

```text
sentinel -> head
```

This helps handle head deletion without extra conditions.

---

### Step 2: Create Two Pointers

```js
firstPointer = sentinel;
secondPointer = sentinel;
```

Both start from sentinel.

---

### Step 3: Move First Pointer n Steps Ahead

```js
for (let i = 0; i < n; i++) {
  firstPointer = firstPointer.next;
}
```

Now the distance between pointers is `n`.

---

### Step 4: Move Both Together

```js
while (firstPointer && firstPointer.next)
```

Move both by one step.

```js
firstPointer = firstPointer.next;
secondPointer = secondPointer.next;
```

Eventually:

```text
firstPointer -> last node

secondPointer -> node before target
```

---

### Step 5: Remove Target Node

```js
secondPointer.next = secondPointer.next.next;
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

## Move First Pointer n Steps

### Initial

```text
F,S
 |
sentinel -> 1 -> 2 -> 3 -> 4 -> 5
```

### Move 1 Step

```text
S
|
sentinel -> 1 -> 2 -> 3 -> 4 -> 5
            ^
            F
```

### Move 2 Steps

```text
S
|
sentinel -> 1 -> 2 -> 3 -> 4 -> 5
                 ^
                 F
```

Gap is now:

```text
2 nodes
```

---

## Move Both Together

| Step  | firstPointer | secondPointer |
| ----- | ------------ | ------------- |
| Start | 2            | sentinel      |
| 1     | 3            | 1             |
| 2     | 4            | 2             |
| 3     | 5            | 3             |

Loop stops because:

```text
firstPointer.next = null
```

Current position:

```text
sentinel -> 1 -> 2 -> 3 -> 4 -> 5
                    ^
                    S
```

Target node:

```text
4
```

---

## Remove Target

Before:

```text
3 -> 4 -> 5
```

Operation:

```js
secondPointer.next = secondPointer.next.next;
```

After:

```text
3 -------> 5
```

Final List:

```text
1 -> 2 -> 3 -> 5
```

---

# Visual Explanation

Before removal:

```text
sentinel -> 1 -> 2 -> 3 -> 4 -> 5
                    ^
                    secondPointer
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

Move first pointer 1 step:

```text
sentinel -> 1
             ^
             F
```

Loop does not run because:

```js
firstPointer.next === null;
```

`secondPointer` is still at sentinel.

Remove:

```js
secondPointer.next = secondPointer.next.next;
```

After:

```text
sentinel -> null
```

Return:

```js
[];
```

---

# Why Does This Work?

Suppose:

```text
1 -> 2 -> 3 -> 4 -> 5
```

and

```js
n = 2;
```

Keep a gap of 2:

```text
secondPointer      firstPointer
       |                 |
       v                 v

1 -> 2 -> 3 -> 4 -> 5
```

Every time the front pointer moves:

```text
+1
```

the back pointer also moves:

```text
+1
```

So the gap always stays:

```text
2
```

When the front pointer reaches the end:

```text
firstPointer -> 5
```

the back pointer automatically lands at:

```text
3
```

which is exactly the node before the target.

---

# Sentinel Advantage

Without a sentinel:

```text
1 -> 2 -> 3
```

Removing the first node requires special handling.

With a sentinel:

```text
sentinel -> 1 -> 2 -> 3
```

We always use:

```js
secondPointer.next = secondPointer.next.next;
```

No special case needed.

---

# Complexity Analysis

### Time Complexity

```text
O(n)
```

- First pointer moves through the list once.
- Second pointer also moves through the list once.
- Total traversal is still linear.

---

### Space Complexity

```text
O(1)
```

Only a few pointers are used.

---

# Two Pass vs One Pass

| Two Pass             | One Pass                      |
| -------------------- | ----------------------------- |
| Find length first    | Uses two pointers             |
| Traverse list twice  | Traverse list once            |
| Easier to understand | Slightly harder to understand |
| O(n) Time            | O(n) Time                     |
| O(1) Space           | O(1) Space                    |

---

# Key Takeaways

- Keep `firstPointer` ahead by `n` nodes.
- Move both pointers together.
- When front pointer reaches the end, back pointer reaches the node before the target.
- Use a sentinel node to handle head deletion.
- Remove node using:
  ```js
  secondPointer.next = secondPointer.next.next;
  ```
- One pass solution avoids calculating the length.
- Space complexity remains `O(1)`.
