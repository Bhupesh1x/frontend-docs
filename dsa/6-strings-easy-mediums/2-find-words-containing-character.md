# Find Words Containing Character

## Problem

You are given a 0-indexed array of strings `words` and a character `x`.

Return an array of indices representing the words that contain the character `x`.

---

## Solution (Using JavaScript `includes()`)

```js
var findWordsContaining = function (words, x) {
  let res = [];

  for (let i = 0; i < words.length; i++) {
    let currWord = words[i];

    // includes() checks whether the current word contains x
    if (currWord.includes(x)) {
      res.push(i);
    }
  }

  return res;
};
```

---

## Solution (Without using built in method)

```js
var findWordsContaining = function (words, x) {
  let res = [];

  for (let i = 0; i < words.length; i++) {
    let currWord = words[i];

    for (let k = 0; k < currWord.length; k++) {
      if (x === currWord[k]) {
        res?.push(i);
        break;
      }
    }
  }

  return res;
};
```

---

## Idea

We need to find **which words contain the given character**.

For every word:

- Check whether it contains `x`.
- If yes, store its index.
- Continue until all words are checked.

Finally, return the list of indices.

---

## Step-by-Step Algorithm

1. Create an empty result array.
2. Loop through every word.
3. Use `includes()` to check whether the current word contains `x`.
4. If it does, add its index to the result.
5. Return the result.

---

## Dry Run

### Input

```text
words = ["abc","bcd","aaaa","cbc"]
x = "a"
```

| Step | `i` | Current Word | `includes("a")` | Result         |
| ---- | --- | ------------ | --------------- | -------------- |
| Init | —   | —            | —               | `[]`           |
| 1    | 0   | `"abc"`      | ✅              | `[0]`          |
| 2    | 1   | `"bcd"`      | ❌              | `[0]`          |
| 3    | 2   | `"aaaa"`     | ✅              | `[0,2]`        |
| 4    | 3   | `"cbc"`      | ❌              | `[0,2]`        |
| Done | —   | —            | —               | Return `[0,2]` |

---

## Visual Dry Run

```text
words = ["abc","bcd","aaaa","cbc"]
          |      |      |      |

i = 0
Word = "abc"

Contains 'a' ?
YES ✅

Result = [0]

-------------------------

i = 1
Word = "bcd"

Contains 'a' ?
NO ❌

Result = [0]

-------------------------

i = 2
Word = "aaaa"

Contains 'a' ?
YES ✅

Result = [0, 2]

-------------------------

i = 3
Word = "cbc"

Contains 'a' ?
NO ❌

Result = [0, 2]

Answer = [0, 2]
```

---

## Another Example

### Input

```text
words = ["leet","code"]
x = "e"
```

| Step | `i` | Current Word | `includes("e")` | Result         |
| ---- | --- | ------------ | --------------- | -------------- |
| Init | —   | —            | —               | `[]`           |
| 1    | 0   | `"leet"`     | ✅              | `[0]`          |
| 2    | 1   | `"code"`     | ✅              | `[0,1]`        |
| Done | —   | —            | —               | Return `[0,1]` |

---

## Example Where Nothing Matches

### Input

```text
words = ["abc","bcd","aaaa","cbc"]
x = "z"
```

| Step | `i` | Current Word | `includes("z")` | Result      |
| ---- | --- | ------------ | --------------- | ----------- |
| Init | —   | —            | —               | `[]`        |
| 1    | 0   | `"abc"`      | ❌              | `[]`        |
| 2    | 1   | `"bcd"`      | ❌              | `[]`        |
| 3    | 2   | `"aaaa"`     | ❌              | `[]`        |
| 4    | 3   | `"cbc"`      | ❌              | `[]`        |
| Done | —   | —            | —               | Return `[]` |

---

## What Does `includes()` Do?

```js
currWord.includes(x);
```

It checks whether the character `x` exists anywhere inside the current word.

Examples:

```js
"apple".includes("a"); // true

"apple".includes("p"); // true

"apple".includes("z"); // false
```

Internally, `includes()` also checks the characters one by one until it finds a match or reaches the end of the string.

So although our code looks simple, `includes()` is doing the character-by-character search for us.

---

## Code Walkthrough

### Create the answer array

```js
let res = [];
```

This stores the indices of matching words.

---

### Traverse every word

```js
for (let i = 0; i < words.length; i++)
```

Visit each word exactly once.

---

### Get the current word

```js
let currWord = words[i];
```

Store the current word to make the code easier to read.

---

### Check whether the word contains the character

```js
if (currWord.includes(x))
```

If the character exists inside the word, continue.

---

### Store the index

```js
res.push(i);
```

Add the current index to the answer.

---

### Return the answer

```js
return res;
```

Return all matching indices.

---

## Why This Works

We check every word exactly once.

For each word:

- If it contains the required character, save its index.
- Otherwise, ignore it.

After checking all words, the result contains exactly the indices we need.

---

## Time Complexity

```text
O(n × m)
```

- `n` = number of words
- `m` = average length of each word

For every word, `includes()` may scan the whole word.

---

## Space Complexity

```text
O(k)
```

- `k` = number of matching words.

The result array stores only the matching indices.

---

# Revision Notes

- Traverse every word.
- Use `includes()` to check if the character exists.
- If yes, store the index.
- Return the result array.
- `includes()` internally checks the string character by character.

---

# Pattern to Remember

```text
Need to find which elements satisfy a condition?

→ Loop through the array.
→ Check the condition.
→ If true, store the index (or value).
→ Return the collected results.
```
