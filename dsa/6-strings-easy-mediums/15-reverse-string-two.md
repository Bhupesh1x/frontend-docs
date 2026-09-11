# Reverse String II

## Problem

Given a string `s` and an integer `k`:

- Reverse the first `k` characters for every `2k` characters.
- If fewer than `k` characters are left, reverse all of them.
- If between `k` and `2k` characters are left, reverse only the first `k` characters.

Return the modified string.

---

## Solution

```js
function swap(arr, left, right) {
  let temp = arr[left];
  arr[left] = arr[right];
  arr[right] = temp;
}

var reverseStr = function (s, k) {
  let str = s.split("");

  for (let x = 0; x < str.length; x = x + 2 * k) {
    let n = k;

    for (let i = 0; i < n / 2; i++) {
      let l = x + i;
      let r = x + n - i - 1;
      swap(str, l, r);
    }
  }

  return str.join("");
};
```

---

## Important Observation

We **do not reverse the whole string**.

Instead,

we process the string in blocks of size:

```text
2k
```

For every block:

- Reverse the first `k` characters.
- Leave the next `k` characters unchanged.

Repeat until the string ends.

---

## Key Idea

Think of the string as chunks of size `2k`.

Example:

```text
abcdefghijk

k = 2

ab cd ef gh ij k
```

Process each chunk:

```text
ab -> ba

cd -> unchanged

ef -> fe

gh -> unchanged

ij -> ji

k -> reverse (only one character)
```

Final answer:

```text
bacdfeghjik
```

---

## Step-by-Step Algorithm

1. Convert the string into an array.
2. Start from index `0`.
3. Jump by `2 * k` each time.
4. Reverse the first `k` characters of that block.
5. Continue until the string ends.
6. Join the array back into a string.

---

## Dry Run

### Input

```text
s = "abcdefg"

k = 2
```

| Step | `x` | Block | Reverse | Array   |
| ---- | --- | ----- | ------- | ------- |
| Init | 0   | abcd  | ab → ba | bacdefg |
| 2    | 4   | efg   | ef → fe | bacdfeg |
| Done | —   | —     | —       | bacdfeg |

Answer

```text
bacdfeg
```

---

## Visual Dry Run

```text
abcdefg

↓

Split into blocks of 2k

abcd | efg

-----------------------

Reverse first k

ab

↓

ba

Result

bacd

-----------------------

Next block

efg

Reverse

ef

↓

fe

Result

bacdfeg
```

---

## Another Example

### Input

```text
s = "abcd"

k = 2
```

First block:

```text
ab

↓

ba
```

Second part remains the same:

```text
cd
```

Answer

```text
bacd
```

---

## Example with Fewer Than `k` Characters Left

### Input

```text
s = "abcdef"

k = 4
```

Remaining characters:

```text
abcdef
```

Since fewer than `2k` characters exist,

reverse only the first `4`.

```text
abcd

↓

dcba
```

Result

```text
dcbaef
```

---

## Example with Less Than `k` Characters Left

### Input

```text
s = "abc"

k = 4
```

Remaining characters:

```text
abc
```

Reverse all of them.

```text
abc

↓

cba
```

Answer

```text
cba
```

This is exactly why we use:

```js
Math.min(k, str.length - x);
```

---

## Why Do We Jump by `2 * k`?

Suppose:

```text
abcdefgh

k = 2
```

Blocks:

```text
ab cd

ef gh
```

We reverse:

```text
ab

↓

ba
```

Skip:

```text
cd
```

Then jump directly to:

```text
ef
```

That's why:

```js
x = x + 2 * k;
```

---

## Visual Understanding

```text
abcdefghijk

k = 2

|----2k----|

ab cd

↑

Reverse

↓

ba cd

Jump

      |----2k----|

      ef gh

      ↑

Reverse

↓

fe gh

Jump

          ij k

Reverse

ji k
```

---

## Code Walkthrough

### Convert string to array

```js
let str = s.split("");
```

Strings are immutable.

So we convert it into an array for swapping.

---

### Traverse every `2k` block

```js
for (let x = 0; x < str.length; x += 2 * k)
```

Each iteration starts at the beginning of a new block.

---

### Calculate characters to reverse

```js
let n = Math.min(k, str.length - x);
```

If fewer than `k` characters remain,

reverse only those.

---

### Find left and right pointers

```js
let l = x + i;

let r = x + n - i - 1;
```

These point to the current pair being swapped.

---

### Swap characters

```js
swap(str, l, r);
```

Reverse the selected portion.

---

### Return the final string

```js
return str.join("");
```

Convert the array back into a string.

---

## Why This Works

Every iteration handles exactly one block.

```text
Reverse first k

↓

Skip next k

↓

Repeat
```

By jumping `2k` positions every time,

we never touch the characters that should remain unchanged.

---

## Time Complexity

```text
O(n)
```

Every character is visited at most once.

---

## Space Complexity

```text
O(n)
```

The string is converted into a character array.

---

# Revision Notes

- Process the string in blocks of `2k`.
- Reverse only the first `k` characters.
- Skip the next `k`.
- Use `Math.min()` for the last incomplete block.
- Convert to an array because strings are immutable.

---

# Pattern to Remember

```text
Need to process a string in fixed-size chunks?

Think block-by-block.

Move the starting index by the block size.

Process only the required part inside each block.

This chunk-processing pattern is common in string problems.
```
