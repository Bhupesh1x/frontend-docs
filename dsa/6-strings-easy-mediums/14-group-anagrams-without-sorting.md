# Group Anagrams (Using Frequency Array)

## Problem

Given an array of strings, group together all strings that are anagrams of each other.

You can return the groups in any order.

---

## Solution (Using Frequency Array)

```js
var groupAnagrams = function (strs) {
  let map = new Map();

  for (let i = 0; i < strs.length; i++) {
    let currStr = strs[i];

    // Create a frequency array for all 26 lowercase letters
    let freqArr = new Array(26).fill(0);

    // Count the frequency of every character
    for (let j = 0; j < currStr.length; j++) {
      let index = currStr[j].charCodeAt() - "a".charCodeAt();
      freqArr[index] = freqArr[index] + 1;
    }

    // Convert frequency array into a unique string key
    let key = "";
    for (let k = 0; k < 26; k++) {
      key = key + String.fromCharCode(k + "a".charCodeAt()) + freqArr[k];
    }

    if (map.has(key)) {
      let prevVal = map.get(key);
      map.set(key, [...prevVal, currStr]);
    } else {
      map.set(key, [currStr]);
    }
  }

  let res = [];

  for (let [_, value] of map) {
    res.push(value);
  }

  return res;
};
```

---

## Important Observation

Two strings are anagrams if **every character appears the same number of times**.

Instead of sorting,

we can simply count how many times each letter appears.

Example:

```text
eat

a -> 1
e -> 1
t -> 1
```

```text
tea

a -> 1
e -> 1
t -> 1
```

Both have the same frequencies,

so they belong to the same group.

---

## Key Idea

For every string:

1. Count the frequency of all 26 letters.
2. Convert that frequency array into a unique key.
3. Use the key inside a Hash Map.
4. Store all matching words together.

Unlike the sorting solution,

we never sort the characters.

---

## Step-by-Step Algorithm

1. Create an empty Hash Map.
2. Traverse every string.
3. Create a frequency array of size 26.
4. Count every character.
5. Convert the frequency array into a unique key.
6. Store the word using that key.
7. Return all grouped arrays.

---

## Dry Run

### Input

```text
["eat","tea","tan","ate","nat","bat"]
```

| Word | Frequency Key (Simplified) | Map                      |
| ---- | -------------------------- | ------------------------ |
| eat  | a1e1t1                     | a1e1t1 → [eat]           |
| tea  | a1e1t1                     | a1e1t1 → [eat, tea]      |
| tan  | a1n1t1                     | a1n1t1 → [tan]           |
| ate  | a1e1t1                     | a1e1t1 → [eat, tea, ate] |
| nat  | a1n1t1                     | a1n1t1 → [tan, nat]      |
| bat  | a1b1t1                     | a1b1t1 → [bat]           |

Final Result

```text
[
  ["eat","tea","ate"],
  ["tan","nat"],
  ["bat"]
]
```

---

## Visual Dry Run

```text
Word

eat

↓

Frequency

a = 1
e = 1
t = 1

↓

Key

a1b0c0d0e1...t1...

↓

Map

key → [eat]

--------------------------

tea

↓

Frequency

a = 1
e = 1
t = 1

↓

Same Key

↓

Append

[eat, tea]

--------------------------

tan

↓

Frequency

a = 1
n = 1
t = 1

↓

Different Key

↓

New Group

[tan]
```

---

## Why Does the Frequency Array Work?

Consider:

```text
listen

silent

enlist
```

Frequency of every letter is exactly the same.

```text
a -> 0

b -> 0

...

e -> 1

i -> 1

l -> 1

n -> 1

s -> 1

t -> 1
```

Even though the order changes,

the frequency never changes.

That makes it a perfect key.

---

## Why Do We Need 26 Elements?

The problem only contains lowercase English letters.

```text
a

b

c

...

z
```

One position is reserved for every letter.

Example:

```text
Index

0 -> a

1 -> b

2 -> c

...

25 -> z
```

---

## How Does `charCodeAt()` Help?

Suppose the character is:

```text
c
```

ASCII values:

```text
'a' = 97

'c' = 99
```

So

```js
99 - 97 = 2
```

Index becomes:

```text
2
```

which is exactly where `c` belongs.

---

## Example

Word

```text
cab
```

Frequency array

```text
a  b  c

1  1  1
```

All other positions remain:

```text
0
```

---

## Why Convert the Frequency Array into a String?

A JavaScript `Map` compares arrays by reference.

Example:

```js
[1, 0, 2] !== [1, 0, 2];
```

Even though they contain the same values.

So we convert the array into a string.

Example key:

```text
a1b0c2d0e0...
```

Now identical frequency arrays produce identical keys.

---

## Code Walkthrough

### Create frequency array

```js
let freqArr = new Array(26).fill(0);
```

Initially:

```text
[0,0,0,0,...]
```

---

### Count characters

```js
let index = currStr[j].charCodeAt() - "a".charCodeAt();
```

Convert a letter into its array index.

---

### Increase frequency

```js
freqArr[index]++;
```

Update the count for that character.

---

### Create the key

```js
key = key + letter + frequency;
```

Produces a unique string like:

```text
a1b0c0d0e1...
```

---

### Store inside the map

```js
map.set(key, [...prevVal, currStr]);
```

All words with the same key belong to the same group.

---

### Build the answer

```js
for (let [_, value] of map)
```

Push every group into the final result.

---

## Why This Works

Every anagram has exactly the same character frequencies.

Example:

```text
eat

↓

a=1
e=1
t=1
```

```text
tea

↓

a=1
e=1
t=1
```

Both generate the same frequency key,

so they naturally end up in the same group.

---

## Frequency Array vs Sorting

| Sorting Approach        | Frequency Array Approach    |
| ----------------------- | --------------------------- |
| Sort every string       | Count character frequencies |
| Key = Sorted string     | Key = Frequency string      |
| Easier to understand    | Slightly faster             |
| `O(k log k)` per string | `O(k)` per string           |

---

## Time Complexity

Let:

- `n` = number of strings
- `k` = average length of each string

For every string:

- Count characters → `O(k)`
- Build the 26-character key → `O(26)` = `O(1)`

Overall:

```text
O(n × k)
```

---

## Space Complexity

```text
O(n × k)
```

The Hash Map stores all grouped strings.

The frequency array is always of size 26, so it is constant space.

---

# Revision Notes

- Sorting is **not required**.
- Count character frequencies instead.
- Frequency array becomes the unique key.
- Same frequency → Same anagram group.
- More optimized than sorting.

---

# Pattern to Remember

```text
Need to compare strings with the same characters?

Instead of sorting,

count frequencies.

Frequency counting is usually faster than sorting.

When the character set is fixed (like a-z),

a frequency array is often the best choice.
```
