# Split a String in Balanced Strings

## Problem

A balanced string contains an equal number of `'L'` and `'R'` characters.

Given a balanced string `s`, split it into the **maximum number of balanced substrings**.

Return that maximum count.

---

## Important Observation

A substring becomes balanced when:

```text
Number of R == Number of L
```

As soon as this happens, we should immediately split the string.

Why?

Because the question asks for the **maximum** number of balanced substrings.

Making a split as early as possible gives us the maximum answer.

---

# Solution 1 (Using Two Counters)

## Code

```js
var balancedStringSplit = function (s) {
  let r = 0;
  let l = 0;
  let count = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "R") {
      r = r + 1;
    } else {
      l = l + 1;
    }

    if (r === l) {
      count = count + 1;
      r = 0;
      l = 0;
    }
  }

  return count;
};
```

---

## Idea

Keep counting:

- Number of `'R'`
- Number of `'L'`

Whenever both counts become equal:

- We found one balanced substring.
- Increase the answer.
- Reset both counters for the next substring.

---

## Step-by-Step Algorithm

1. Initialize `r = 0`, `l = 0`, `count = 0`.
2. Traverse the string.
3. Increase `r` if the character is `'R'`.
4. Otherwise increase `l`.
5. If `r === l`, one balanced substring is found.
6. Increase `count`.
7. Reset both counters.
8. Continue until the end.

---

## Dry Run

### Input

```text
s = "RLRRLLRLRL"
```

| Step | Character | `R` | `L` | Balanced? | Count |
| ---- | --------- | --- | --- | --------- | ----- |
| Init | —         | 0   | 0   | —         | 0     |
| 1    | R         | 1   | 0   | ❌        | 0     |
| 2    | L         | 1   | 1   | ✅ Reset  | 1     |
| 3    | R         | 1   | 0   | ❌        | 1     |
| 4    | R         | 2   | 0   | ❌        | 1     |
| 5    | L         | 2   | 1   | ❌        | 1     |
| 6    | L         | 2   | 2   | ✅ Reset  | 2     |
| 7    | R         | 1   | 0   | ❌        | 2     |
| 8    | L         | 1   | 1   | ✅ Reset  | 3     |
| 9    | R         | 1   | 0   | ❌        | 3     |
| 10   | L         | 1   | 1   | ✅ Reset  | 4     |

Answer = **4**

---

## Visual Dry Run

```text
Input

R L R R L L R L R L

------------------------

R = 1
L = 0

Not Balanced

------------------------

R = 1
L = 1

Balanced ✅

Count = 1

Reset

------------------------

R = 1
L = 0

------------------------

R = 2
L = 0

------------------------

R = 2
L = 1

------------------------

R = 2
L = 2

Balanced ✅

Count = 2

Reset

------------------------

R = 1
L = 0

------------------------

R = 1
L = 1

Balanced ✅

Count = 3

Reset

------------------------

R = 1
L = 0

------------------------

R = 1
L = 1

Balanced ✅

Count = 4

Answer = 4
```

---

# Solution 2 (Using One Counter)

## Code

```js
var balancedStringSplit = function (s) {
  let temp = 0;
  let count = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "R") {
      temp = temp + 1;
    } else {
      temp = temp - 1;
    }

    if (temp === 0) {
      count = count + 1;
    }
  }

  return count;
};
```

---

## Idea

Instead of maintaining two counters:

Treat:

```text
R = +1

L = -1
```

If both appear equally,

their total becomes **0**.

Example:

```text
R L

+1 -1

Total = 0
```

or

```text
L R

-1 +1

Total = 0
```

So whenever `temp` becomes `0`, we have found one balanced substring.

---

## Step-by-Step Algorithm

1. Initialize `temp = 0`.
2. Traverse the string.
3. Add `1` for every `'R'`.
4. Subtract `1` for every `'L'`.
5. Whenever `temp == 0`, increase the answer.
6. Return the answer.

---

## Dry Run

### Input

```text
s = "RLRRLLRLRL"
```

| Step | Character | `temp` | Balanced? | Count |
| ---- | --------- | ------ | --------- | ----- |
| Init | —         | 0      | —         | 0     |
| 1    | R         | 1      | ❌        | 0     |
| 2    | L         | 0      | ✅        | 1     |
| 3    | R         | 1      | ❌        | 1     |
| 4    | R         | 2      | ❌        | 1     |
| 5    | L         | 1      | ❌        | 1     |
| 6    | L         | 0      | ✅        | 2     |
| 7    | R         | 1      | ❌        | 2     |
| 8    | L         | 0      | ✅        | 3     |
| 9    | R         | 1      | ❌        | 3     |
| 10   | L         | 0      | ✅        | 4     |

Answer = **4**

---

## Visual Dry Run

```text
R = +1

L = -1

------------------------

Read R

temp = 1

------------------------

Read L

temp = 0

Balanced ✅

Count = 1

------------------------

Read R

temp = 1

------------------------

Read R

temp = 2

------------------------

Read L

temp = 1

------------------------

Read L

temp = 0

Balanced ✅

Count = 2

------------------------

Read R

temp = 1

------------------------

Read L

temp = 0

Balanced ✅

Count = 3

------------------------

Read R

temp = 1

------------------------

Read L

temp = 0

Balanced ✅

Count = 4
```

---

## Why Does the One Counter Work?

Think of:

```text
R = +1

L = -1
```

Examples:

```text
RL

+1 -1

= 0
```

```text
RRLL

+1 +1 -1 -1

= 0
```

```text
RLRL

+1 -1 +1 -1

= 0
```

Whenever the total becomes **0**, the number of `R` and `L` is equal.

So we have one balanced substring.

---

## Why Is the One Counter Better?

Two-counter approach:

```text
R = 3

L = 3

Compare them every time.
```

One-counter approach:

```text
temp = 0

Just check

temp == 0
```

Less code.

Less memory.

Same logic.

---

## Code Walkthrough

### Initialize

```js
let temp = 0;
let count = 0;
```

- `temp` keeps the balance.
- `count` stores the answer.

---

### Traverse the string

```js
for (let i = 0; i < s.length; i++)
```

Visit every character once.

---

### Update the balance

```js
if (s[i] === "R") {
  temp++;
} else {
  temp--;
}
```

- `R` increases the balance.
- `L` decreases the balance.

---

### Check if balanced

```js
if (temp === 0) {
  count++;
}
```

Whenever the balance returns to zero, one balanced substring is complete.

---

## Why This Works

Every `'R'` adds `1`.

Every `'L'` subtracts `1`.

If both occur equally, the balance becomes `0`.

Each time the balance reaches `0`, we have found one balanced substring.

Splitting immediately gives the maximum possible number of balanced substrings.

---

## Time Complexity

### Two Counters

```text
O(n)
```

One traversal.

---

### One Counter

```text
O(n)
```

One traversal.

---

## Space Complexity

### Two Counters

```text
O(1)
```

---

### One Counter

```text
O(1)
```

Only two variables are used.

---

# Revision Notes

- Balanced means equal number of `L` and `R`.
- Split immediately whenever the substring becomes balanced.
- Two-counter approach:
  - Count `L`
  - Count `R`
  - Compare them.
- One-counter approach:
  - `R = +1`
  - `L = -1`
  - Balance becomes `0` when equal.
- One-counter solution is shorter and cleaner.

---

# Pattern to Remember

```text
Need to keep track of two opposite things?

Try converting them into:

+1
-1

Instead of storing two counters.

When the running balance becomes zero,
both sides are equal.
```
