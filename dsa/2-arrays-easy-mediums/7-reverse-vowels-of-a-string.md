**Question Description: Reverse Vowels of a String**

```js

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

```

**code**

```js
const vowels = ["a", "e", "i", "o", "u"];

function isVowel(char) {
  return vowels?.includes(char?.toLowerCase());
}

var reverseVowels = function (str) {
  let i = 0;
  let x = str.length - 1;

  let s = str.split("");
  while (i < x) {
    if (!isVowel(s[i])) {
      i = i + 1;
      continue;
    }

    if (!isVowel(s[x])) {
      x = x - 1;
      continue;
    }

    let temp = s[i];
    s[i] = s[x];
    s[x] = temp;

    i = i + 1;
    x = x - 1;
  }

  return s.join("");
};
```

## 🧠 Logic Summary

We only need to reverse the vowels, not the whole string.

So we use **two pointers**:

- `i` → starts from left
- `x` → starts from right

### Steps

- Move `i` forward until we find a vowel
- Move `x` backward until we find a vowel
- Swap both vowels
- Continue until pointers meet

---

# 🔍 Dry Run

## Input

```js
"IceCreAm";
```

Converted array:

```js
["I", "c", "e", "C", "r", "e", "A", "m"];
```

---

## 🔍 Dry Run With Animation

![reverse_vowels_explained](./assets/reverse_vowels_explained.gif)

## Step by Step

| Step | i   | x   | s[i] | s[x] | Action            | Array State       |
| ---- | --- | --- | ---- | ---- | ----------------- | ----------------- |
| Init | 0   | 7   | I    | m    | start             | [I,c,e,C,r,e,A,m] |
| 1    | 0   | 7   | I    | m    | x-- (m not vowel) | [I,c,e,C,r,e,A,m] |
| 2    | 0   | 6   | I    | A    | swap(I,A)         | [A,c,e,C,r,e,I,m] |
| 3    | 1   | 5   | c    | e    | i++ (c not vowel) | [A,c,e,C,r,e,I,m] |
| 4    | 2   | 5   | e    | e    | swap(e,e)         | [A,c,e,C,r,e,I,m] |
| 5    | 3   | 4   | C    | r    | i++ (C not vowel) | [A,c,e,C,r,e,I,m] |
| 6    | 4   | 4   | r    | r    | stop (i >= x)     | [A,c,e,C,r,e,I,m] |

---

## Final Output

```js
"AceCreIm";
```

---

# 💡 Why Two Pointers Works Well Here

Two pointers help us:

- scan from both sides
- swap only vowels
- avoid extra loops

Efficient and clean solution.

---

# ⏱ Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(n)  |
| Space      | O(n)  |

### Why space is O(n)?

Because:

```js
str.split("");
```

creates a new array.

---

# 📌 Important Things to Remember

### 1. Use `length - 1`

```js
let x = str.length - 1;
```

### 2. `continue` makes code cleaner

```js
if (...) {
  continue;
}
```

### 3. Strings are immutable in JavaScript

So we convert string into array first:

```js
let s = str.split("");
```

---
