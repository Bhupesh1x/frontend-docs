# Find Most Frequent Vowel and Consonant

## Problem

You are given a string `s` containing only lowercase English letters.

Your task is to:

- Find the vowel (`a`, `e`, `i`, `o`, `u`) with the highest frequency.
- Find the consonant with the highest frequency.
- Return the **sum** of these two frequencies.

If there are no vowels or no consonants, their frequency is considered **0**.

---

## Important Observation

This is a **frequency counting** problem.

Whenever you see words like:

- Count frequency
- Most frequent
- Occurrences
- Repeated characters

Think about using a **Hash Map**.

A Hash Map lets us store:

```text
Character -> Frequency
```

Example:

```text
"successes"

s -> 4
u -> 1
c -> 2
e -> 2
```

Once we have the frequencies, finding the maximum becomes easy.

---

# Solution 1 (Using Two Maps)

## Code

```js
const vowelsMap = new Map([
  ["a", 1],
  ["e", 1],
  ["i", 1],
  ["o", 1],
  ["u", 1],
]);

function isVowel(ch) {
  return vowelsMap.has(ch);
}

var maxFreqSum = function (s) {
  let vMap = new Map();
  let cMap = new Map();

  for (let i = 0; i < s.length; i++) {
    const curr = s[i];

    if (isVowel(curr)) {
      if (vMap.has(curr)) {
        vMap.set(curr, vMap.get(curr) + 1);
      } else {
        vMap.set(curr, 1);
      }
    } else {
      if (cMap.has(curr)) {
        cMap.set(curr, cMap.get(curr) + 1);
      } else {
        cMap.set(curr, 1);
      }
    }
  }

  let vmax = 0;
  let cmax = 0;

  for (const [key, value] of vMap) {
    vmax = Math.max(vmax, value);
  }

  for (const [key, value] of cMap) {
    cmax = Math.max(cmax, value);
  }

  return vmax + cmax;
};
```

---

## Idea

Instead of storing everything together:

- Store vowel frequencies in one map.
- Store consonant frequencies in another map.

Finally,

- Find the maximum vowel frequency.
- Find the maximum consonant frequency.
- Return their sum.

---

## Step-by-Step Algorithm

1. Create one map for vowels.
2. Create one map for consonants.
3. Traverse the string.
4. Increase the frequency in the correct map.
5. Find the maximum value in both maps.
6. Return their sum.

---

## Dry Run

### Input

```text
s = "successes"
```

### Building the Maps

| Character | Vowel? | Vowel Map   | Consonant Map |
| --------- | ------ | ----------- | ------------- |
| s         | ❌     | `{}`        | `{s:1}`       |
| u         | ✅     | `{u:1}`     | `{s:1}`       |
| c         | ❌     | `{u:1}`     | `{s:1,c:1}`   |
| c         | ❌     | `{u:1}`     | `{s:1,c:2}`   |
| e         | ✅     | `{u:1,e:1}` | `{s:1,c:2}`   |
| s         | ❌     | `{u:1,e:1}` | `{s:2,c:2}`   |
| s         | ❌     | `{u:1,e:1}` | `{s:3,c:2}`   |
| e         | ✅     | `{u:1,e:2}` | `{s:3,c:2}`   |
| s         | ❌     | `{u:1,e:2}` | `{s:4,c:2}`   |

Final Maps

```text
Vowel Map

u -> 1
e -> 2

--------------------

Consonant Map

s -> 4
c -> 2
```

Maximum vowel frequency = **2**

Maximum consonant frequency = **4**

Answer = **6**

---

## Visual Dry Run

```text
Input

successes

------------------------

Read 's'

Consonant Map

s -> 1

------------------------

Read 'u'

Vowel Map

u -> 1

------------------------

Read 'c'

Consonant Map

s -> 1
c -> 1

------------------------

Read 'c'

Consonant Map

s -> 1
c -> 2

------------------------

Read 'e'

Vowel Map

u -> 1
e -> 1

------------------------

Read 's'

s -> 2

------------------------

Read 's'

s -> 3

------------------------

Read 'e'

e -> 2

------------------------

Read 's'

s -> 4

------------------------

Maximum vowel = 2

Maximum consonant = 4

Answer = 6
```

---

# Solution 2 (Using One Map)

## Code

```js
const vowelsMap = new Map([
  ["a", 1],
  ["e", 1],
  ["i", 1],
  ["o", 1],
  ["u", 1],
]);

function isVowel(ch) {
  return vowelsMap.has(ch);
}

var maxFreqSum = function (s) {
  let map = new Map();

  for (let i = 0; i < s.length; i++) {
    const curr = s[i];

    if (map.has(curr)) {
      map.set(curr, map.get(curr) + 1);
    } else {
      map.set(curr, 1);
    }
  }

  let vmax = 0;
  let cmax = 0;

  for (const [key, val] of map) {
    if (isVowel(key)) {
      vmax = Math.max(vmax, val);
    } else {
      cmax = Math.max(cmax, val);
    }
  }

  return vmax + cmax;
};
```

---

## Idea

Instead of maintaining two separate maps:

Store the frequency of **every character** in one map.

Later,

- Check whether each character is a vowel or consonant.
- Update the corresponding maximum.

This reduces the amount of code.

---

## Step-by-Step Algorithm

1. Create one frequency map.
2. Count every character.
3. Traverse the map.
4. If the character is a vowel, update `vmax`.
5. Otherwise, update `cmax`.
6. Return `vmax + cmax`.

---

## Dry Run

### Input

```text
s = "successes"
```

### Build Frequency Map

| Character | Map                 |
| --------- | ------------------- |
| s         | `{s:1}`             |
| u         | `{s:1,u:1}`         |
| c         | `{s:1,u:1,c:1}`     |
| c         | `{s:1,u:1,c:2}`     |
| e         | `{s:1,u:1,c:2,e:1}` |
| s         | `{s:2,u:1,c:2,e:1}` |
| s         | `{s:3,u:1,c:2,e:1}` |
| e         | `{s:3,u:1,c:2,e:2}` |
| s         | `{s:4,u:1,c:2,e:2}` |

Final Map

```text
s -> 4
u -> 1
c -> 2
e -> 2
```

Now traverse the map.

| Character | Frequency | Type      | Maximum  |
| --------- | --------- | --------- | -------- |
| s         | 4         | Consonant | cmax = 4 |
| u         | 1         | Vowel     | vmax = 1 |
| c         | 2         | Consonant | cmax = 4 |
| e         | 2         | Vowel     | vmax = 2 |

Answer =

```text
2 + 4 = 6
```

---

## Visual Dry Run

```text
Step 1

Build Frequency Map

s -> 4
u -> 1
c -> 2
e -> 2

------------------------

Traverse Map

s

Consonant

cmax = 4

------------------------

u

Vowel

vmax = 1

------------------------

c

Consonant

cmax = max(4,2)

= 4

------------------------

e

Vowel

vmax = max(1,2)

= 2

------------------------

Answer

2 + 4 = 6
```

---

## Why is One Map Better?

The first approach separates vowels and consonants while counting.

The second approach stores everything together.

Instead of maintaining two maps:

```text
Vowel Map

e -> 2
u -> 1

Consonant Map

s -> 4
c -> 2
```

we only keep

```text
Frequency Map

s -> 4
c -> 2
u -> 1
e -> 2
```

Then, while finding the maximum, we simply check whether each character is a vowel or not.

Less code, same result.

---

## Code Walkthrough

### Create Frequency Map

```js
let map = new Map();
```

Stores the frequency of every character.

---

### Count frequencies

```js
if (map.has(curr)) {
  map.set(curr, map.get(curr) + 1);
} else {
  map.set(curr, 1);
}
```

Increase the frequency if the character already exists.

Otherwise, insert it with frequency `1`.

---

### Find the maximum

```js
if (isVowel(key)) {
  vmax = Math.max(vmax, val);
} else {
  cmax = Math.max(cmax, val);
}
```

Update the maximum frequency depending on whether the character is a vowel or consonant.

---

### Return the answer

```js
return vmax + cmax;
```

---

## Why This Works

Every character's frequency is counted exactly once.

Then we simply separate them into:

- Highest vowel frequency
- Highest consonant frequency

Finally, return their sum.

---

## Time Complexity

### Two Maps

```text
O(n)
```

- Build both maps → `O(n)`
- Find maximum values → At most 26 letters

Overall:

```text
O(n)
```

---

### One Map

```text
O(n)
```

Still only one traversal of the string.

---

## Space Complexity

### Two Maps

```text
O(1)
```

Only lowercase English letters exist.

Maximum unique characters = **26**.

So the maps never grow beyond 26 entries.

---

### One Map

```text
O(1)
```

The map still stores at most **26** unique characters.

---

# Revision Notes

- This is a frequency-counting problem.
- Think **Hash Map** whenever frequency is involved.
- Two Maps → Separate vowels and consonants while counting.
- One Map → Count everything first, then classify later.
- The One Map approach is shorter and cleaner.
- Use `Map.has()`, `Map.get()`, and `Map.set()` to update frequencies.

---

# Pattern to Remember

```text
Need to count frequencies?

→ Use a Hash Map.

Need the most frequent element?

→ Count everything first.

→ Traverse the map once to find the maximum.
```
