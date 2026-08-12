# Length of Last Word

## Problem

Given a string `s` consisting of words and spaces, return the length of the last word.

A word contains only non-space characters.

---

## Solution (Code)

```js
var lengthOfLastWord = function (s) {
  // Start from the last character
  let n = s.length - 1;
  let count = 0;

  // Traverse the string from right to left
  while (n >= 0) {
    // If we already started counting and found a space,
    // the last word is complete.
    if (s[n] == " " && count > 0) {
      break;
    }

    // Count only non-space characters.
    if (s[n] != " ") {
      count++;
    }

    // Move to the previous character.
    n--;
  }

  return count;
};
```

## Idea

We only care about the **last word**, so there is no need to split the string or check every word.

We'll start from the **end of the string** and move backwards.

The trick is:

1. Ignore all trailing spaces.
2. Start counting once we find the first character.
3. Keep counting until we hit another space.
4. Return the count.

---

## Step-by-Step Algorithm

1. Start from the last index of the string.
2. Keep moving left.
3. Ignore spaces until the last word starts.
4. Once a letter is found, increase the count.
5. If another space comes after counting has started, stop.
6. Return the count.

---

## Dry Run

### Input

```text
s = " fly me to the moon "
```

Last word = `"moon"`

| Step | `n` | `s[n]` | `count` | Action                |
| ---- | --- | ------ | ------- | --------------------- |
| Init | 19  | `" "`  | 0       | Start from end        |
| 1    | 19  | `" "`  | 0       | Ignore trailing space |
| 2    | 18  | `"n"`  | 1       | Start counting        |
| 3    | 17  | `"o"`  | 2       | Count                 |
| 4    | 16  | `"o"`  | 3       | Count                 |
| 5    | 15  | `"m"`  | 4       | Count                 |
| 6    | 14  | `" "`  | 4       | Word finished, break  |
| Done | —   | —      | 4       | Return `4`            |

---

## Visual Dry Run

```text
Input

" fly me to the moon "
                  ^
                  n

Step 1
Current = ' '
count = 0

Trailing space
Move left

" fly me to the moon "
                 ^
                 n

Current = 'n'
count = 1

" fly me to the moon "
                ^
                n

Current = 'o'
count = 2

" fly me to the moon "
               ^
               n

Current = 'o'
count = 3

" fly me to the moon "
              ^
              n

Current = 'm'
count = 4

" fly me to the moon "
             ^
             n

Current = ' '
count > 0

Stop here.

Answer = 4
```

---

## Another Example

### Input

```text
s = "Hello World"
```

| Step | `n` | `s[n]` | `count` | Action     |
| ---- | --- | ------ | ------- | ---------- |
| Init | 10  | `"d"`  | 0       | Start      |
| 1    | 10  | `"d"`  | 1       | Count      |
| 2    | 9   | `"l"`  | 2       | Count      |
| 3    | 8   | `"r"`  | 3       | Count      |
| 4    | 7   | `"o"`  | 4       | Count      |
| 5    | 6   | `"W"`  | 5       | Count      |
| 6    | 5   | `" "`  | 5       | Break      |
| Done | —   | —      | 5       | Return `5` |

---

## Why We Skip Trailing Spaces

Consider this input:

```text
"hello world     "
```

If we start counting immediately, we'll count spaces instead of the last word.

So we first skip all ending spaces.

```text
hello world_____
               ^
           Ignore these

hello world
          ^
      Start counting here
```

This is why the condition

```js
if (s[n] == " " && count > 0)
```

is important.

- If `count == 0`, we're still skipping trailing spaces.
- If `count > 0`, we've already counted the last word, so reaching another space means we're done.

---

## Code Walkthrough

### Initialize

```js
let n = s.length - 1;
let count = 0;
```

- `n` starts from the last character.
- `count` stores the length of the last word.

---

### Traverse from the end

```js
while (n >= 0)
```

Keep moving left until the string ends.

---

### Stop after the last word

```js
if (s[n] == " " && count > 0) {
    break;
}
```

Once we've started counting and reach a space, the last word is complete.

---

### Count only letters

```js
if (s[n] != " ") {
  count++;
}
```

Increase the answer only for non-space characters.

---

### Move left

```js
n--;
```

Check the previous character.

---

## Why This Works

From the end of the string:

- Ignore extra spaces.
- Count characters of the last word.
- Stop as soon as that word ends.

Since we never look at earlier words, the solution stays simple and efficient.

---

## Time Complexity

```text
O(n)
```

In the worst case, we may scan the whole string once.

---

## Space Complexity

```text
O(1)
```

Only two variables are used.

---

# Revision Notes

- Start from the end of the string.
- Skip trailing spaces automatically because `count` is still `0`.
- Start counting when the first letter is found.
- Stop when another space appears after counting has started.
- No `split()`, no extra array, just one backward traversal.

---

# Pattern to Remember

```text
Need something from the end of a string?

→ Start from the last index.
→ Skip unwanted characters.
→ Count/process until a stopping condition.
→ Return the answer.
```
