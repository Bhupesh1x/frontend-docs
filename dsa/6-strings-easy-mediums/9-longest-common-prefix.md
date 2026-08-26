# Longest Common Prefix

## Problem

Given an array of strings, return the **longest common prefix** among all the strings.

If there is no common prefix, return an empty string `""`.

---

## Solution

```js
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  let x = 0;
  const firstStr = strs[0];

  // Keep checking characters of the first string
  while (x <= firstStr.length) {
    // Compare the current character with all other strings
    for (let i = 1; i < strs.length; i++) {
      let currStr = strs[i];

      // If characters don't match or another string ends,
      // return the common prefix found so far.
      if (currStr[x] !== firstStr[x] || x >= currStr.length) {
        return firstStr.substring(0, x);
      }
    }

    // Move to the next character
    x++;
  }

  // The first string itself is the common prefix
  return firstStr;
};
```

---

## Important Observation

Every common prefix must start from the **first character**.

Example:

```text
flower
flow
flight
```

All strings start with:

```text
f
```

Then

```text
fl
```

After that,

```text
flower -> o

flight -> i
```

Mismatch.

So the answer is:

```text
fl
```

---

## Key Idea

Use the **first string** as the reference.

Check its characters one by one.

For every character:

- Compare it with the same position in every other string.
- If every string matches, continue.
- As soon as one string differs, stop.

Everything before that position is the longest common prefix.

---

## Step-by-Step Algorithm

1. Take the first string.
2. Start from index `0`.
3. Compare that character with every other string.
4. If all strings match, move to the next character.
5. If one doesn't match, return the prefix till now.
6. If the whole first string matches, return it.

---

## Dry Run

### Input

```text
strs = ["flower","flow","flight"]
```

| Position (`x`) | First String | Second | Third | Match? |
| -------------- | ------------ | ------ | ----- | ------ |
| 0              | f            | f      | f     | ✅     |
| 1              | l            | l      | l     | ✅     |
| 2              | o            | o      | i     | ❌     |

Return

```text
"fl"
```

---

## Visual Dry Run

```text
flower
flow
flight

Check index 0

f
f
f

All same ✅

----------------------

Check index 1

l
l
l

All same ✅

----------------------

Check index 2

o
o
i

Mismatch ❌

Return

fl
```

---

## Another Example

### Input

```text
strs = ["dog","racecar","car"]
```

| Position | First | Second | Third | Match? |
| -------- | ----- | ------ | ----- | ------ |
| 0        | d     | r      | c     | ❌     |

Return

```text
""
```

---

## Another Example

### Input

```text
strs = ["apple","app","application"]
```

| Position | Character | Match?               |
| -------- | --------- | -------------------- |
| 0        | a         | ✅                   |
| 1        | p         | ✅                   |
| 2        | p         | ✅                   |
| 3        | l         | ❌ (`app` ends here) |

Return

```text
app
```

---

## Visual Dry Run

```text
apple
app
application

a ✅

p ✅

p ✅

Next character

apple -> l

app -> End

Stop

Answer = app
```

---

## Why Do We Use the First String?

Every common prefix must also be a prefix of the first string.

Example:

```text
flower

flow

flight
```

The answer can never be:

```text
light
```

because prefixes always start from index `0`.

So using the first string as the reference is enough.

---

## Why Return `substring(0, x)`?

Suppose:

```text
flower

flow

flight
```

Mismatch happens at:

```text
Index = 2
```

Characters before index `2` are:

```text
fl
```

So

```js
firstStr.substring(0, x);
```

returns

```text
fl
```

which is exactly the longest common prefix.

---

## Code Walkthrough

### Take the first string

```js
const firstStr = strs[0];
```

We'll compare every other string with this one.

---

### Start from index `0`

```js
let x = 0;
```

`x` represents the current character position.

---

### Compare with every string

```js
for (let i = 1; i < strs.length; i++)
```

Check whether every string has the same character at index `x`.

---

### Stop on mismatch

```js
if (currStr[x] !== firstStr[x] || x >= currStr.length)
```

Stop when:

- Characters are different.
- Another string has already ended.

---

### Return the common prefix

```js
return firstStr.substring(0, x);
```

Everything before the mismatch is the answer.

---

### Move to the next character

```js
x++;
```

Continue checking the next position.

---

### Return the whole first string

```js
return firstStr;
```

If every character matches,

the first string itself is the common prefix.

---

## Why This Works

We compare characters **column by column**.

Example:

```text
flower

flow

flight
```

```text
Column 0

f
f
f

✅

Column 1

l
l
l

✅

Column 2

o
o
i

❌

Stop
```

Everything before the mismatch is common to every string.

---

## Time Complexity

```text
O(n × m)
```

- `n` = number of strings
- `m` = length of the shortest/common prefix being checked

For each character position, we compare all strings.

---

## Space Complexity

```text
O(1)
```

Only a few variables are used.

---

# Revision Notes

- Use the first string as the reference.
- Compare one character at a time.
- Check the same index in every string.
- Stop immediately when a mismatch is found.
- Return the prefix before the mismatch.
- If no mismatch occurs, return the first string.

---

# Pattern to Remember

```text
Need something common across multiple strings?

Use one string as the reference.

Compare character by character.

Stop as soon as one string disagrees.

The characters before that point are the common answer.
```
