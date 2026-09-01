# Valid Anagram

## Problem

Two strings are **anagrams** if:

- They contain exactly the same characters.
- Every character appears the same number of times.
- The order of characters does **not** matter.

Return `true` if `t` is an anagram of `s`, otherwise return `false`.

---

## Solution

```js
var isAnagram = function (s, t) {
  // If lengths are different, they can never be anagrams
  if (s.length !== t.length) return false;

  let mapS = new Map();
  let mapT = new Map();

  // Count frequency of characters in s
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    let val = mapS.get(char);
    mapS.set(char, val ? val + 1 : 1);
  }

  // Count frequency of characters in t
  for (let i = 0; i < t.length; i++) {
    let char = t[i];
    let val = mapT.get(char);
    mapT.set(char, val ? val + 1 : 1);
  }

  // Compare both frequency maps
  for (const [key, value] of mapS) {
    if (mapT.get(key) !== value) {
      return false;
    }
  }

  return true;
};
```

---

## Important Observation

The order of characters does **not** matter.

Only the **frequency** matters.

Example:

```text
anagram

nagaram
```

Both contain:

```text
a -> 3
n -> 1
g -> 1
r -> 1
m -> 1
```

Since every frequency matches,

they are anagrams.

---

## Key Idea

Instead of sorting,

count how many times each character appears.

If both strings have exactly the same frequencies,

they are anagrams.

This is a classic **Hash Map frequency-counting** problem.

---

## Step-by-Step Algorithm

1. If the lengths are different, return `false`.
2. Create one frequency map for `s`.
3. Create another frequency map for `t`.
4. Count the occurrences of every character.
5. Compare both maps.
6. If any frequency differs, return `false`.
7. Otherwise return `true`.

---

## Dry Run

### Input

```text
s = "anagram"

t = "nagaram"
```

### Build Frequency Map for `s`

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

### Build Frequency Map for `t`

| Character | Map                   |
| --------- | --------------------- |
| n         | {n:1}                 |
| a         | {n:1,a:1}             |
| g         | {n:1,a:1,g:1}         |
| a         | {n:1,a:2,g:1}         |
| r         | {n:1,a:2,g:1,r:1}     |
| a         | {n:1,a:3,g:1,r:1}     |
| m         | {n:1,a:3,g:1,r:1,m:1} |

Both maps are identical.

Answer:

```text
true
```

---

## Visual Dry Run

```text
String 1

anagram

↓

Frequency Map

a -> 3
n -> 1
g -> 1
r -> 1
m -> 1

--------------------------

String 2

nagaram

↓

Frequency Map

n -> 1
a -> 3
g -> 1
r -> 1
m -> 1

--------------------------

Compare

a

3 == 3 ✅

n

1 == 1 ✅

g

1 == 1 ✅

r

1 == 1 ✅

m

1 == 1 ✅

Answer = true
```

---

## Another Example

### Input

```text
s = "rat"

t = "car"
```

Frequency Maps

```text
rat

r -> 1
a -> 1
t -> 1

------------------

car

c -> 1
a -> 1
r -> 1
```

Comparison

```text
t

mapS = 1

mapT = undefined

Mismatch ❌
```

Return

```text
false
```

---

## Why Do We Check Length First?

Suppose:

```text
abc

ab
```

Different lengths.

Even before checking frequencies,

we know they cannot be anagrams.

So this simple check saves extra work.

```js
if (s.length !== t.length) {
  return false;
}
```

---

## Why Use a Hash Map?

Without a map,

for every character,

we would have to search the whole string repeatedly.

Instead,

we store frequencies.

Example:

```text
banana

↓

Map

b -> 1
a -> 3
n -> 2
```

Now comparing frequencies becomes very easy.

---

## Code Walkthrough

### Check lengths

```js
if (s.length !== t.length)
```

Different lengths means they cannot be anagrams.

---

### Create two maps

```js
let mapS = new Map();
let mapT = new Map();
```

One stores frequencies for `s`.

The other stores frequencies for `t`.

---

### Count frequencies

```js
let val = mapS.get(char);

mapS.set(char, val ? val + 1 : 1);
```

If the character already exists,

increase its count.

Otherwise,

insert it with frequency `1`.

---

### Compare both maps

```js
if (mapT.get(key) !== value)
```

If any character has a different frequency,

return `false`.

---

### Return answer

```js
return true;
```

All frequencies matched.

---

## Why This Works

Two strings are anagrams **only if**:

- Every character exists in both strings.
- Every character appears the same number of times.

The frequency maps store exactly this information.

If the maps match,

the strings are anagrams.

---

## Time Complexity

```text
O(n)
```

- Build first map → `O(n)`
- Build second map → `O(n)`
- Compare maps → At most 26 lowercase letters (or at most `n` unique characters)

Overall:

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

For lowercase English letters, the maps store at most **26** unique characters.

If the character set is unrestricted (full Unicode), the space complexity would be **O(k)**, where `k` is the number of unique characters.

---

# Revision Notes

- Anagrams have the same characters with the same frequencies.
- Check lengths first.
- Use frequency maps.
- Compare frequencies.
- If any frequency differs → `false`.
- Otherwise → `true`.

---

# Pattern to Remember

```text
Need to compare two strings regardless of order?

Think Frequency Map.

Count characters in both strings.

If every frequency matches,

the strings represent the same collection of characters.
```
