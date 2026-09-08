# Isomorphic Strings

## Problem

Two strings are **isomorphic** if every character in the first string can be replaced to get the second string.

Rules:

- One character can map to only one character.
- Two different characters cannot map to the same character.
- A character can map to itself.

Return `true` if the strings are isomorphic, otherwise return `false`.

---

## Solution

```js
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
  if (s.length !== t.length) return false;

  // Store mappings in both directions
  let mapStoT = new Map();
  let mapTtoS = new Map();

  for (let i = 0; i < s.length; i++) {
    let currS = s[i];
    let currT = t[i];

    // Existing mapping from s -> t must remain the same
    if (mapStoT.has(currS) && mapStoT.get(currS) !== currT) {
      return false;
    }

    // Existing mapping from t -> s must remain the same
    if (mapTtoS.has(currT) && mapTtoS.get(currT) !== currS) {
      return false;
    }

    // Store the mapping
    mapStoT.set(currS, currT);
    mapTtoS.set(currT, currS);
  }

  return true;
};
```

---

## Important Observation

This problem is **not about frequency**.

It is about **consistent mapping**.

Example:

```text
egg

↓

add
```

Mapping:

```text
e → a

g → d
```

Every time we see `g`, it maps to `d`.

Everything is consistent.

Answer:

```text
true
```

---

## Why Do We Need Two Maps?

Many people think one map is enough.

It isn't.

We need to verify both:

```text
s → t

AND

t → s
```

Because:

- One character cannot map to two different characters.
- Two different characters cannot map to the same character.

Both conditions must be checked.

---

## Key Idea

Maintain two mappings.

```text
Map 1

s → t

Map 2

t → s
```

While traversing the strings:

- If an existing mapping changes → return `false`.
- Otherwise store the mapping.

---

## Step-by-Step Algorithm

1. If lengths are different, return `false`.
2. Create two hash maps.
3. Traverse both strings together.
4. Check if `s[i]` is already mapped.
5. Check if `t[i]` is already mapped.
6. If either mapping conflicts, return `false`.
7. Otherwise store the mapping.
8. Return `true`.

---

## Dry Run

### Input

```text
s = "egg"

t = "add"
```

| Step | `s[i]` | `t[i]` | `s → t` Map  | `t → s` Map  | Action        |
| ---- | ------ | ------ | ------------ | ------------ | ------------- |
| 1    | e      | a      | {e→a}        | {a→e}        | Store mapping |
| 2    | g      | d      | {e→a, g→d}   | {a→e, d→g}   | Store mapping |
| 3    | g      | d      | Same mapping | Same mapping | Continue      |
| Done | —      | —      | —            | —            | Return `true` |

---

## Visual Dry Run

```text
s

e g g

t

a d d

---------------------

Read

e

↓

a

Store

e → a

a → e

---------------------

Read

g

↓

d

Store

g → d

d → g

---------------------

Read

g

↓

d

Already mapped

g → d ✅

d → g ✅

Answer = true
```

---

## Example 2

### Input

```text
s = "foo"

t = "bar"
```

| Step  | Mapping | Result   |
| ----- | ------- | -------- |
| f → b | ✅      | Continue |
| o → a | ✅      | Continue |
| o → r | ❌      | Conflict |

Return

```text
false
```

---

## Visual Dry Run

```text
foo

bar

First

f → b

Good

----------------

Second

o → a

Good

----------------

Third

o

Already mapped to

a

But current character is

r

Conflict ❌

Answer = false
```

---

## Example 3

### Input

```text
s = "far"

t = "boo"
```

| Step  | Mapping | Result                                |
| ----- | ------- | ------------------------------------- |
| f → b | ✅      | Continue                              |
| a → o | ✅      | Continue                              |
| r → o | ❌      | Two letters mapping to same character |

Return

```text
false
```

---

## Visual Dry Run

```text
far

boo

Read

f → b

Good

----------------

Read

a → o

Good

----------------

Read

r → o

But

o

already maps back to

a

Conflict ❌

Answer = false
```

---

## Example 4

### Input

```text
s = "paper"

t = "title"
```

Mappings

```text
p → t

a → i

p → t ✅

e → l

r → e
```

No conflicts.

Answer:

```text
true
```

---

## Why Isn't One Map Enough?

Consider:

```text
ab

cc
```

Using only:

```text
a → c

b → c
```

Everything looks valid.

But this is **wrong**.

Two different characters cannot map to the same character.

That's why we also need:

```text
c → a
```

When `b` tries to map to `c`,

the second map immediately detects the conflict.

---

## Code Walkthrough

### Check lengths

```js
if (s.length !== t.length)
```

Different lengths can never be isomorphic.

---

### Create two maps

```js
let mapStoT = new Map();
let mapTtoS = new Map();
```

One stores:

```text
s → t
```

The other stores:

```text
t → s
```

---

### Check existing mapping

```js
if (mapStoT.has(currS) && mapStoT.get(currS) !== currT)
```

If the character already maps somewhere else,

return `false`.

---

### Check reverse mapping

```js
if (mapTtoS.has(currT) && mapTtoS.get(currT) !== currS)
```

If another character already maps to this character,

return `false`.

---

### Store mapping

```js
mapStoT.set(currS, currT);
mapTtoS.set(currT, currS);
```

Create the mapping for future comparisons.

---

### Return answer

```js
return true;
```

No conflicts were found.

---

## Why This Works

Both maps always stay consistent.

Example:

```text
paper

title
```

Forward map:

```text
p → t

a → i

e → l

r → e
```

Reverse map:

```text
t → p

i → a

l → e

e → r
```

If any mapping changes,

one of the maps will detect it immediately.

---

## Time Complexity

```text
O(n)
```

We traverse both strings only once.

Each hash map operation takes `O(1)` on average.

---

## Space Complexity

```text
O(k)
```

`k` is the number of unique characters.

In the worst case, every character is different.

---

# Revision Notes

- This is a **mapping** problem, not a frequency problem.
- Check lengths first.
- Use **two hash maps**.
- One map stores `s → t`.
- Another stores `t → s`.
- If either mapping conflicts, return `false`.
- Otherwise return `true`.

---

# Pattern to Remember

```text
Whenever two things need a one-to-one relationship,

think of two hash maps.

Forward mapping checks:

One item maps to only one value.

Reverse mapping checks:

One value belongs to only one item.

Two-way mapping is a common interview pattern.
```
