# Add Two Numbers

## Problem

You are given two linked lists representing two non-negative integers.

- Each node contains a single digit.
- Digits are stored in reverse order.
- Add the two numbers and return the result as a linked list.

### Example

```js
Input: l1 = [2, 4, 3];
l2 = [5, 6, 4];

Output: [7, 0, 8];
```

Explanation:

```text
342 + 465 = 807
```

Result is stored in reverse:

```text
7 -> 0 -> 8
```

---

# Code

```js
var addTwoNumbers = function (l1, l2) {
  let ans = new ListNode();
  let head = ans;
  let carry = 0;

  while (l1 || l2 || carry) {
    let sum = (l1?.val ?? 0) + (l2?.val ?? 0) + carry;

    carry = Math.floor(sum / 10);
    let digit = sum % 10;

    let node = new ListNode(digit);

    ans.next = node;

    ans = ans.next;
    l1 = l1?.next ? l1?.next : null;
    l2 = l2?.next ? l2?.next : null;
  }

  return head.next;
};
```

---

# Intuition

This problem is exactly like the addition we do on paper.

Example:

```text
  342
+ 465
-----
  807
```

But the digits are stored in reverse:

```text
2 -> 4 -> 3
5 -> 6 -> 4
```

So we can start adding from the head itself.

For every position:

```text
digit1 + digit2 + carry
```

Then:

```text
new digit = sum % 10
carry = Math.floor(sum / 10)
```

Create a node using the new digit and continue.

---

# Core Idea

For every step:

```text
sum = digit1 + digit2 + carry
```

Store:

```text
digit = sum % 10
```

Carry forward:

```text
carry = Math.floor(sum / 10)
```

Example:

```text
8 + 7 = 15
```

Store:

```text
5
```

Carry:

```text
1
```

---

# Why Use a Dummy Node?

Instead of handling the first node separately:

```js
let ans = new ListNode();
let head = ans;
```

The dummy node helps us keep track of the beginning of the answer list.

At the end:

```js
return head.next;
```

---

# Approach

### Step 1: Create Dummy Node

```js
let ans = new ListNode();
let head = ans;
```

---

### Step 2: Maintain Carry

```js
let carry = 0;
```

---

### Step 3: Traverse Both Lists

Continue while:

```js
l1 || l2 || carry;
```

We also need to process the final carry.

---

### Step 4: Calculate Sum

```js
let sum = (l1?.val ?? 0) + (l2?.val ?? 0) + carry;
```

If a list ends:

```js
null => 0
```

---

### Step 5: Extract Digit and Carry

```js
carry = Math.floor(sum / 10);
digit = sum % 10;
```

---

### Step 6: Create New Node

```js
let node = new ListNode(digit);
```

Attach it to answer list.

---

### Step 7: Move Forward

```js
l1 = l1?.next;
l2 = l2?.next;
ans = ans.next;
```

---

# Dry Run

### Input

```js
l1 = [2, 4, 3];
l2 = [5, 6, 4];
```

Represented as:

```text
2 -> 4 -> 3
5 -> 6 -> 4
```

---

## Iteration 1

Current digits:

```text
2 + 5 + carry(0)
```

Sum:

```text
7
```

Digit:

```text
7 % 10 = 7
```

Carry:

```text
Math.floor(7 / 10) = 0
```

Answer:

```text
7
```

---

## Iteration 2

Current digits:

```text
4 + 6 + carry(0)
```

Sum:

```text
10
```

Digit:

```text
10 % 10 = 0
```

Carry:

```text
1
```

Answer:

```text
7 -> 0
```

---

## Iteration 3

Current digits:

```text
3 + 4 + carry(1)
```

Sum:

```text
8
```

Digit:

```text
8
```

Carry:

```text
0
```

Answer:

```text
7 -> 0 -> 8
```

---

## Final Result

```text
7 -> 0 -> 8
```

Return:

```js
[7, 0, 8];
```

---

# Dry Run Table

| Step | l1  | l2  | Carry In | Sum | Digit | Carry Out | Answer        |
| ---- | --- | --- | -------- | --- | ----- | --------- | ------------- |
| 1    | 2   | 5   | 0        | 7   | 7     | 0         | `7`           |
| 2    | 4   | 6   | 0        | 10  | 0     | 1         | `7 -> 0`      |
| 3    | 3   | 4   | 1        | 8   | 8     | 0         | `7 -> 0 -> 8` |

---

# Dry Run (Different Length Lists)

### Input

```js
l1 = [9, 9, 9, 9, 9, 9, 9];
l2 = [9, 9, 9, 9];
```

---

### First Few Iterations

| Step | l1  | l2  | Carry In | Sum | Digit | Carry Out |
| ---- | --- | --- | -------- | --- | ----- | --------- |
| 1    | 9   | 9   | 0        | 18  | 8     | 1         |
| 2    | 9   | 9   | 1        | 19  | 9     | 1         |
| 3    | 9   | 9   | 1        | 19  | 9     | 1         |
| 4    | 9   | 9   | 1        | 19  | 9     | 1         |
| 5    | 9   | 0   | 1        | 10  | 0     | 1         |
| 6    | 9   | 0   | 1        | 10  | 0     | 1         |
| 7    | 9   | 0   | 1        | 10  | 0     | 1         |
| 8    | 0   | 0   | 1        | 1   | 1     | 0         |

Result:

```text
8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1
```

---

# Visual Explanation

Suppose:

```text
4 -> 6
5 -> 7
```

Step 1:

```text
4 + 5 = 9

Answer:
9
```

Step 2:

```text
6 + 7 = 13

Store:
3

Carry:
1
```

Final Carry:

```text
1
```

Answer:

```text
9 -> 3 -> 1
```

---

# Why Loop Uses `l1 || l2 || carry`

Consider:

```text
9 + 1
```

After first addition:

```text
sum = 10
digit = 0
carry = 1
```

Both lists are finished:

```text
l1 = null
l2 = null
```

But we still need:

```text
1
```

So the loop continues because:

```js
carry === 1;
```

Without checking carry, the last digit would be lost.

---



# Complexity Analysis

### Time Complexity

```text
O(max(n, m))
```

Where:

```text
n = length of l1
m = length of l2
```

We process each node once.

---

### Space Complexity

```text
O(max(n, m))
```

The answer linked list stores the result digits.

Ignoring the output list itself, the extra auxiliary space is:

```text
O(1)
```

---

# Key Takeaways

- This is just normal addition with carry.
- Digits are stored in reverse order, so addition starts from the head.
- Use:
  ```js
  digit = sum % 10;
  ```
  to get the current digit.
- Use:
  ```js
  carry = Math.floor(sum / 10);
  ```
  to get carry.
- A dummy node makes answer list construction easy.
- Keep looping while:
  ```js
  l1 || l2 || carry;
  ```
- Don't forget the final carry.
- This is one of the most common linked list pointer problems.
