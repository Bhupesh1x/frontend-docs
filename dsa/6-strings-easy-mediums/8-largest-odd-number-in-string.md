# Largest Odd Number in String

## Problem

You are given a string `num` representing a large integer.

Return the **largest-valued odd integer** (as a string) that is a **non-empty substring** of `num`.

If no odd number exists, return an empty string `""`.

---

## Solution

```js
function isOdd(char) {
  return char % 2 !== 0;
}

var largestOddNumber = function (num) {
  let n = num.length - 1;

  while (n >= 0) {
    if (isOdd(num[n])) {
      return num.substring(0, n + 1);
    }

    n--;
  }

  return "";
};
```

---

## Important Observation

A number is **odd** if its **last digit** is odd.

Examples:

```text
135 → Odd ✅

5721 → Odd ✅

820 → Even ❌

2468 → Even ❌
```

Notice that we **don't need to check the whole number**.

We only need to know whether its **last digit** is odd.

---

## Key Idea

We want the **largest** possible substring.

That means:

- Keep the starting index at `0`.
- Find the **rightmost odd digit**.
- Return everything from the beginning up to that digit.

There is no need to check every possible substring.

---

## Step-by-Step Algorithm

1. Start from the last character.
2. Check whether the digit is odd.
3. If it is, return the substring from index `0` to that digit.
4. Otherwise move one position left.
5. If no odd digit is found, return `""`.

---

## Dry Run

### Input

```text
num = "52"
```

| Step | `n` | Digit | Odd? | Action       |
| ---- | --- | ----- | ---- | ------------ |
| Init | 1   | 2     | ❌   | Move left    |
| 1    | 0   | 5     | ✅   | Return `"5"` |

Answer:

```text
"5"
```

---

## Visual Dry Run

```text
Input

5 2
  ↑

2 is even ❌

Move left

5 2
↑

5 is odd ✅

Return substring

0 → 0

"5"
```

---

## Another Example

### Input

```text
num = "4206"
```

| Step | Digit | Odd?      |
| ---- | ----- | --------- |
| 6    | ❌    | Move left |
| 0    | ❌    | Move left |
| 2    | ❌    | Move left |
| 4    | ❌    | Move left |

No odd digit found.

Answer:

```text
""
```

---

## Visual Dry Run

```text
4 2 0 6
      ↑

Even

Move

4 2 0 6
    ↑

Even

Move

4 2 0 6
  ↑

Even

Move

4 2 0 6
↑

Even

No odd digit found

Answer = ""
```

---

## Another Example

### Input

```text
num = "35427"
```

| Step | `n` | Digit | Odd? | Action               |
| ---- | --- | ----- | ---- | -------------------- |
| Init | 4   | 7     | ✅   | Return entire string |

Answer:

```text
"35427"
```

---

## Visual Dry Run

```text
3 5 4 2 7
        ↑

7 is odd ✅

Return substring

0 → 4

35427
```

---

## Why Do We Traverse from the End?

Suppose:

```text
35428
```

If we scan from the beginning,

we don't know where the largest odd substring ends.

Instead,

starting from the end lets us quickly find the **last odd digit**.

Example:

```text
3 5 4 2 8
        ↑

Even

Move

3 5 4 2 8
      ↑

2

Even

Move

3 5 4 2 8
    ↑

4

Even

Move

3 5 4 2 8
  ↑

5

Odd ✅

Return

355? ❌

Actually return:

Substring(0,2)

"35"
```

So the answer becomes:

```text
35
```

which is the largest odd substring.

---

## Why Does Returning `substring(0, n + 1)` Work?

Suppose:

```text
1234567
```

The last digit is already odd.

Largest odd substring:

```text
1234567
```

Now consider:

```text
1234568
```

Move left until:

```text
12345
```

Everything after the last odd digit must be removed because an even last digit makes the whole number even.

So we return:

```js
num.substring(0, n + 1);
```

---

## What Does `substring()` Do?

```js
num.substring(start, end);
```

It returns characters from:

```text
start

up to

end - 1
```

Example:

```js
"abcdef".substring(0, 3);
```

returns

```text
abc
```

So if:

```text
n = 4
```

we need:

```js
substring(0, 5);
```

because the ending index is **exclusive**.

---

## Code Walkthrough

### Check whether a digit is odd

```js
function isOdd(char) {
  return char % 2 !== 0;
}
```

Returns `true` if the digit is odd.

---

### Start from the end

```js
let n = num.length - 1;
```

The last digit decides whether the number is odd.

---

### Traverse backwards

```js
while (n >= 0)
```

Keep moving left until an odd digit is found.

---

### Found an odd digit

```js
return num.substring(0, n + 1);
```

Return the largest possible prefix ending at that digit.

---

### No odd digit exists

```js
return "";
```

No odd substring can be formed.

---

## Why This Works

An integer is odd only if its **last digit is odd**.

To get the largest possible substring,

we keep as many digits as possible.

So we simply find the **rightmost odd digit** and return everything before it.

---

## Time Complexity

```text
O(n)
```

In the worst case,

we scan the string once from right to left.

---

## Space Complexity

```text
O(1)
```

No extra data structure is used.

The returned substring is the required output, so it isn't counted as extra space.

---

# Revision Notes

- A number is odd if its last digit is odd.
- Traverse from the end.
- Find the first odd digit.
- Return the prefix ending at that digit.
- If no odd digit exists, return `""`.
- No need to generate every substring.

---

# Pattern to Remember

```text
When only the last character determines the answer,

start checking from the end.

As soon as the condition is satisfied,

return immediately.

This avoids unnecessary work.
```
