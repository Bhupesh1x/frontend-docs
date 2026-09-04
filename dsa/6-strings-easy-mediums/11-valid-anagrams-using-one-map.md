# Valid Anagram (Using One Map)

## Problem

Two strings are **anagrams** if:

- They contain exactly the same characters.
- Every character appears the same number of times.
- The order of characters does **not** matter.

Return `true` if `t` is an anagram of `s`, otherwise return `false`.

---

## Solution (Using One Hash Map)

```js
var isAnagram = function (s, t) {
  // Different lengths can never be anagrams
  if (s.length !== t.length) return false;

  let map = new Map();

  // Count frequencies of characters in s
  for (let i = 0; i < s.length; i++) {
    let val = map.get(s[i]);
    map.set(s[i], val ? val + 1 : 1);
  }

  // Remove frequencies using t
  for (let i = 0; i < t.length; i++) {
    let char = t[i];
    let val = map.get(char);

    if (!map.has(char) || val <= 0) {
      return false;
    } else {
      map.set(char, val - 1);
    }
  }

  return true;
};
```

---

## Important Observation

Instead of creating **two frequency maps**, we can use **just one**.

Think of it like this:

- The first string **adds** characters.
- The second string **removes** characters.

If everything cancels out correctly, the strings are anagrams.

---

## Key Idea

### Step 1

Count every character in `s`.

Example:

```text
anagram

↓

a -> 3
n -> 1
g -> 1
r -> 1
m -> 1
```

### Step 2

Traverse `t`.

Whenever you see a character,

reduce its count.

Example:

```text
a -> 2
a -> 1
a -> 0
```

If you ever try to reduce:

- a character that doesn't exist, or
- a character whose count is already `0`

then the strings are not anagrams.

---

## Step-by-Step Algorithm

1. If the lengths are different, return `false`.
2. Create one frequency map.
3. Count every character of `s`.
4. Traverse `t`.
5. Reduce the frequency for every character.
6. If a character doesn't exist or its count becomes negative, return `false`.
7. Otherwise return `true`.

---

## Dry Run

### Input

```text
s = "anagram"

t = "nagaram"
```

### Build Frequency Map

| Character | Map                   |
| --------- | --------------------- |
| a         | {a:1}                 |
| n         | {a:1,n:1}             |
| a         | {a:2,n:1}             |
| g         | {a:2,n:1,g:1}         |
| r         | {a:2,n:1,g:1,r:1}     |
| a         | {a:3,n:1,g:1,r:1}     |
| m         | {a:3,n:1,g:1,r:1,m:1} |

---

### Traverse `t`

| Character | Before | After |
| --------- | ------ | ----- |
| n         | 1      | 0     |
| a         | 3      | 2     |
| g         | 1      | 0     |
| a         | 2      | 1     |
| r         | 1      | 0     |
| a         | 1      | 0     |
| m         | 1      | 0     |

Every character was successfully removed.

Answer:

```text
true
```

---

## Visual Dry Run

```text
Step 1

Count characters

anagram

↓

Map

a -> 3
n -> 1
g -> 1
r -> 1
m -> 1

------------------------

Now process

nagaram

Read n

n

1 → 0

------------------------

Read a

3 → 2

------------------------

Read g

1 → 0

------------------------

Read a

2 → 1

------------------------

Read r

1 → 0

------------------------

Read a

1 → 0

------------------------

Read m

1 → 0

Everything matched

Answer = true
```

---

## Another Example

### Input

```text
s = "rat"

t = "car"
```

Build map

```text
r -> 1
a -> 1
t -> 1
```

Process `t`

```text
Read c

Doesn't exist ❌

Return false
```

---

## Another Example

### Input

```text
s = "aa"

t = "ab"
```

Build map

```text
a -> 2
```

Process

```text
Read a

2 → 1

Read b

Doesn't exist ❌

Return false
```

---

## Why Do We Check Length First?

Example:

```text
abc

ab
```

Different lengths.

They can never be anagrams.

So we return immediately.

```js
if (s.length !== t.length) {
  return false;
}
```

---

## Why Do We Check `val <= 0`?

Consider:

```text
s = "ab"

t = "aa"
```

Frequency map

```text
a -> 1
b -> 1
```

Processing `t`

First `a`

```text
a

1 → 0
```

Second `a`

Current count:

```text
0
```

There are no more `a` characters left.

So:

```js
val <= 0;
```

means the strings are different.

Return `false`.

---

## Code Walkthrough

### Check lengths

```js
if (s.length !== t.length)
```

Different lengths cannot be anagrams.

---

### Create the frequency map

```js
let map = new Map();
```

Stores character frequencies.

---

### Count characters

```js
map.set(char, val ? val + 1 : 1);
```

Increase the count for every character in `s`.

---

### Remove frequencies

```js
map.set(char, val - 1);
```

Every matching character decreases its count.

---

### Invalid character

```js
if (!map.has(char) || val <= 0)
```

Return `false` if:

- the character never existed, or
- we've already used all of its occurrences.

---

### Return answer

```js
return true;
```

Every character matched successfully.

---

## Why This Works

Think of the frequency map as an inventory.

Example:

```text
anagram

↓

a -> 3
```

Every time we see an `a` in `t`,

we remove one.

```text
3

↓

2

↓

1

↓

0
```

If we ever try to remove more than we have,

the strings are different.

---

## One Map vs Two Maps

| Two Maps                           | One Map                                         |
| ---------------------------------- | ----------------------------------------------- |
| Count frequencies for both strings | Count only the first string                     |
| Compare both maps at the end       | Decrease counts while reading the second string |
| Slightly easier to understand      | More optimized and shorter                      |
| Uses two hash maps                 | Uses one hash map                               |

---

## Time Complexity

```text
O(n)
```

- Count characters → `O(n)`
- Remove characters → `O(n)`

Overall:

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

For lowercase English letters, the map stores at most **26** unique characters.

For a general character set, it would be **O(k)**, where `k` is the number of unique characters.

---

# Revision Notes

- Check lengths first.
- Count frequencies of the first string.
- Traverse the second string.
- Reduce the frequency for each character.
- If a character doesn't exist or its count becomes negative, return `false`.
- One map is cleaner than maintaining two maps.

---

# Pattern to Remember

```text
Need to compare two collections?

Instead of building two frequency maps,

build one map.

Add using the first input.

Remove using the second input.

If everything cancels out correctly,

the two collections are identical.
```
