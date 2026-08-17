# Jewels and Stones

## Problem

You're given two strings:

- `jewels` → Contains all the types of jewels.
- `stones` → Contains all the stones you have.

Return how many stones are also jewels.

**Note:** Characters are **case-sensitive**, so `'a'` and `'A'` are different.

---

## Important Observation

Whenever a problem asks questions like:

- Does this element exist?
- Is this value present?
- Search repeatedly in an array or string?

Always think about using a **Hash Map** or **Set**.

They allow very fast lookups.

---

# Solution 1 (Two Loops)

## Code

```js
/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function (jewels, stones) {
  let count = 0;

  for (let i = 0; i < stones.length; i++) {
    let currStone = stones[i];

    for (let j = 0; j < jewels.length; j++) {
      if (jewels[j] === currStone) {
        count++;
        break;
      }
    }
  }

  return count;
};

// Time Complexity: O(n × m)
// Space Complexity: O(1)
```

---

## Idea

For every stone:

- Check every jewel.
- If a match is found, increase the count.
- Stop checking the remaining jewels because we already found a match.

---

## Step-by-Step Algorithm

1. Initialize `count = 0`.
2. Traverse every stone.
3. Compare it with every jewel.
4. If they match, increase the count.
5. Break the inner loop.
6. Return the count.

---

## Dry Run

### Input

```text
jewels = "aA"
stones = "aAAbbbb"
```

| Stone | Compare With | Match? | Count |
| ----- | ------------ | ------ | ----- |
| `a`   | `a`          | ✅     | 1     |
| `A`   | `a`, `A`     | ✅     | 2     |
| `A`   | `a`, `A`     | ✅     | 3     |
| `b`   | `a`, `A`     | ❌     | 3     |
| `b`   | `a`, `A`     | ❌     | 3     |
| `b`   | `a`, `A`     | ❌     | 3     |
| `b`   | `a`, `A`     | ❌     | 3     |

Answer = **3**

---

## Visual Dry Run

```text
Jewels

[a] [A]

-------------------------

Stone = a

Compare with a ✅

Count = 1

-------------------------

Stone = A

Compare with a ❌
Compare with A ✅

Count = 2

-------------------------

Stone = A

Compare with a ❌
Compare with A ✅

Count = 3

-------------------------

Stone = b

Compare with a ❌
Compare with A ❌

Not a jewel

-------------------------

Stone = b

Compare with a ❌
Compare with A ❌

Not a jewel

-------------------------

Stone = b

Compare with a ❌
Compare with A ❌

Not a jewel

-------------------------

Stone = b

Compare with a ❌
Compare with A ❌

Not a jewel

Answer = 3
```

---

## Why Do We Use `break`?

```js
if (jewels[j] === currStone) {
    count++;
    break;
}
```

Once a stone matches a jewel, we don't need to compare it with the remaining jewels.

Example:

```text
Stone = 'A'

Compare with 'a' ❌

Compare with 'A' ✅

Count++

Break
```

This avoids unnecessary comparisons.

---

# Solution 2 (Using Set)

## Code

```js
var numJewelsInStones = function (jewels, stones) {
  let set = new Set();
  let count = 0;

  for (let i = 0; i < jewels.length; i++) {
    set.add(jewels[i]);
  }

  for (let i = 0; i < stones.length; i++) {
    if (set.has(stones[i])) {
      count++;
    }
  }

  return count;
};

// Time Complexity: O(n)
// Space Complexity: O(1)
```

> **Note:** In JavaScript, use `set.add()` to insert into a `Set`. `set.set()` is used with `Map`.

---

## Idea

Instead of searching the jewels again and again, store them in a `Set`.

Then every lookup becomes very fast.

Steps:

- Put every jewel inside the set.
- Traverse every stone.
- If the stone exists in the set, increase the count.

---

## Step-by-Step Algorithm

1. Create an empty set.
2. Insert every jewel into the set.
3. Traverse every stone.
4. Check if the current stone exists in the set.
5. If yes, increase the count.
6. Return the count.

---

## Dry Run

### Input

```text
jewels = "aA"
stones = "aAAbbbb"
```

### Build the Set

| Step | Character | Set      |
| ---- | --------- | -------- |
| 1    | `a`       | `{a}`    |
| 2    | `A`       | `{a, A}` |

---

### Traverse Stones

| Stone | `set.has()` | Count |
| ----- | ----------- | ----- |
| `a`   | ✅          | 1     |
| `A`   | ✅          | 2     |
| `A`   | ✅          | 3     |
| `b`   | ❌          | 3     |
| `b`   | ❌          | 3     |
| `b`   | ❌          | 3     |
| `b`   | ❌          | 3     |

Answer = **3**

---

## Visual Dry Run

```text
Step 1

Store jewels inside Set

Set

{ a, A }

-------------------------

Traverse stones

Stone = a

Exists in Set?
YES ✅

Count = 1

-------------------------

Stone = A

Exists in Set?
YES ✅

Count = 2

-------------------------

Stone = A

Exists in Set?
YES ✅

Count = 3

-------------------------

Stone = b

Exists in Set?
NO ❌

Count = 3

-------------------------

Stone = b

Exists in Set?
NO ❌

Count = 3

-------------------------

Stone = b

Exists in Set?
NO ❌

Count = 3

-------------------------

Stone = b

Exists in Set?
NO ❌

Count = 3

Answer = 3
```

---

## Why is Set Better?

Without a set:

```text
For every stone,
search every jewel.
```

Example:

```text
Stone 1 -> Search jewels

Stone 2 -> Search jewels

Stone 3 -> Search jewels

Stone 4 -> Search jewels
```

Lots of repeated searching.

---

With a set:

```text
Build Set once

{a, A}

Now every lookup is fast.

Stone -> Set.has()
Stone -> Set.has()
Stone -> Set.has()
Stone -> Set.has()
```

No repeated searching.

---

## Code Walkthrough

### Create the Set

```js
let set = new Set();
```

Stores all jewel types.

---

### Insert every jewel

```js
set.add(jewels[i]);
```

Now the set contains every jewel exactly once.

---

### Traverse every stone

```js
for (let i = 0; i < stones.length; i++)
```

Visit each stone.

---

### Check whether it is a jewel

```js
if (set.has(stones[i]))
```

If the stone exists inside the set, it is a jewel.

---

### Increase the answer

```js
count++;
```

Count one more jewel.

---

## Why This Works

The set stores every jewel.

Whenever we see a stone:

- If it's inside the set, it's a jewel.
- Otherwise, ignore it.

Every stone is checked exactly once.

---

## Time Complexity

### Two Loops

```text
O(n × m)
```

- `n` = number of stones
- `m` = number of jewels

---

### Set Approach

```text
O(n + m)
```

- Build the set once.
- Traverse the stones once.

This is usually written as **O(n)** when discussing the optimized solution.

---

## Space Complexity

### Two Loops

```text
O(1)
```

No extra data structure.

---

### Set Approach

```text
O(1)
```

The set can contain at most:

- 26 lowercase letters
- 26 uppercase letters

Maximum = **52** unique characters.

Since this never grows with the input size, it is considered constant space.

---

# Revision Notes

- Repeated searching usually means **Hash Map** or **Set**.
- Two loops work but repeat the same search many times.
- Store all jewels in a set first.
- Use `set.has()` for quick lookup.
- `Set` stores only unique values.
- In JavaScript:
  - `set.add(value)` → Insert
  - `set.has(value)` → Check
  - `set.delete(value)` → Remove

---

# Pattern to Remember

```text
Need to repeatedly check whether something exists?

→ Think Hash Map or Set.

Store all searchable values first.

Then use fast lookups instead of searching again and again.
```
