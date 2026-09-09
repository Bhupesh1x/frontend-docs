# Group Anagrams (Using Sorting)

## Problem

Given an array of strings, group together all strings that are anagrams of each other.

You can return the groups in any order.

---

## Solution (Using Sorting)

```js
var groupAnagrams = function (strs) {
  let map = new Map();

  for (let i = 0; i < strs.length; i++) {
    let currStr = strs[i];

    // Create a unique key by sorting the characters
    let sortedStr = currStr.split("").sort().join("");

    if (map.has(sortedStr)) {
      let val = map.get(sortedStr);
      map.set(sortedStr, [...val, currStr]);
    } else {
      map.set(sortedStr, [currStr]);
    }
  }

  let result = [];

  for (let [key, value] of map) {
    result.push(value);
  }

  return result;
};
```

---

## Important Observation

All anagrams become **exactly the same string after sorting**.

Example:

```text
eat

↓

aet
```

```text
tea

↓

aet
```

```text
ate

↓

aet
```

Since all three become:

```text
aet
```

they belong to the same group.

This sorted string becomes our **Hash Map key**.

---

## Key Idea

For every word:

1. Sort its characters.
2. Use the sorted string as the key.
3. Store the original word in that key's array.

Finally,

return all the arrays stored in the map.

---

## Step-by-Step Algorithm

1. Create an empty hash map.
2. Traverse every string.
3. Sort the string.
4. Use the sorted string as the key.
5. If the key already exists, append the word.
6. Otherwise create a new array.
7. Return all grouped arrays.

---

## Dry Run

### Input

```text
["eat","tea","tan","ate","nat","bat"]
```

| Word | Sorted Key | Map                   |
| ---- | ---------- | --------------------- |
| eat  | aet        | aet → [eat]           |
| tea  | aet        | aet → [eat, tea]      |
| tan  | ant        | ant → [tan]           |
| ate  | aet        | aet → [eat, tea, ate] |
| nat  | ant        | ant → [tan, nat]      |
| bat  | abt        | abt → [bat]           |

Final Map

```text
aet → [eat, tea, ate]

ant → [tan, nat]

abt → [bat]
```

Result

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
eat

↓

Sort

↓

aet

Map

aet → [eat]

---------------------

tea

↓

Sort

↓

aet

Already exists

aet → [eat, tea]

---------------------

tan

↓

Sort

↓

ant

New key

ant → [tan]

---------------------

ate

↓

Sort

↓

aet

Append

aet → [eat, tea, ate]

---------------------

nat

↓

Sort

↓

ant

Append

ant → [tan, nat]

---------------------

bat

↓

Sort

↓

abt

New key

abt → [bat]
```

---

## Why Does Sorting Work?

Consider:

```text
eat

tea

ate
```

Sort each one.

```text
eat

↓

aet

---------------

tea

↓

aet

---------------

ate

↓

aet
```

Every anagram produces the same sorted string.

So we can easily group them together.

---

## Another Example

### Input

```text
[""]
```

Sorted

```text
""
```

Map

```text
"" → [""]
```

Answer

```text
[
  [""]
]
```

---

## Another Example

### Input

```text
["a"]
```

Sorted

```text
a
```

Map

```text
a → ["a"]
```

Answer

```text
[
  ["a"]
]
```

---

## Code Walkthrough

### Create a Hash Map

```js
let map = new Map();
```

The key will be the sorted string.

The value will be an array of original strings.

---

### Sort the current string

```js
currStr.split("").sort().join("");
```

Example:

```text
tea

↓

["t","e","a"]

↓

["a","e","t"]

↓

"aet"
```

---

### Existing group

```js
if (map.has(sortedStr))
```

If we've already seen this sorted string,

append the current word.

---

### Create a new group

```js
map.set(sortedStr, [currStr]);
```

First word with this sorted key.

---

### Build the answer

```js
for (let [key, value] of map)
```

We only need the grouped arrays,

so push every value into the result.

---

## Why This Works

Every anagram has the same characters.

Sorting those characters always produces the same string.

Example:

```text
listen

↓

eilnst

silent

↓

eilnst

enlist

↓

eilnst
```

Since they all have the same key,

they naturally get stored in the same group.

---

## Time Complexity

Let:

- `n` = number of strings
- `k` = average length of each string

Sorting one string takes:

```text
O(k log k)
```

Doing this for all strings:

```text
O(n × k log k)
```

---

## Space Complexity

```text
O(n × k)
```

The hash map stores all the strings in the output groups.

The sorted keys also require extra space.

---

# Revision Notes

- Anagrams become identical after sorting.
- Use the sorted string as the Hash Map key.
- Store original strings as the value.
- Return all values from the map.
- Very common Hash Map + Sorting interview problem.

---

# Pattern to Remember

```text
Need to group strings that contain the same characters?

Create a common representation (key).

Sorting is one way to create that key.

Strings with the same sorted version belong to the same group.

Whenever multiple inputs should be grouped,

think:

Hash Map

key → common representation

value → list of matching items
```
