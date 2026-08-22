# Valid Palindrome (Using Extra Space)

## Problem

A string is considered a palindrome if:

- Convert all uppercase letters to lowercase.
- Remove all non-alphanumeric characters.
- The remaining string reads the same from left to right and right to left.

Return `true` if it is a palindrome, otherwise return `false`.

---

## Solution (Using Extra Space)

```js
var isPalindrome = function (s) {
  s = s.toLowerCase();
  let str = "";

  // Build a new string containing only letters and numbers
  for (let i = 0; i < s.length; i++) {
    if (s[i].match(/[a-z0-9]/i)) {
      str = str + s[i];
    }
  }

  // Check whether the cleaned string is a palindrome
  let i = 0;
  let j = str.length - 1;

  while (i < j) {
    if (str[i] !== str[j]) {
      return false;
    }

    i++;
    j--;
  }

  return true;
};
```

---

## Idea

The original string contains:

- Spaces
- Commas
- Colons
- Special characters
- Uppercase letters

These should **not** affect whether the string is a palindrome.

So we'll do it in **two steps**:

1. Create a new cleaned string containing only lowercase letters and numbers.
2. Use two pointers to compare characters from both ends.

---

## Step-by-Step Algorithm

1. Convert the string to lowercase.
2. Create an empty string.
3. Traverse the original string.
4. Add only letters and digits to the new string.
5. Use two pointers:
   - One from the beginning.
   - One from the end.
6. If characters don't match, return `false`.
7. Otherwise continue until both pointers meet.
8. Return `true`.

---

## Dry Run

### Input

```text
s = "A man, a plan, a canal: Panama"
```

### Step 1: Convert to Lowercase

```text
"a man, a plan, a canal: panama"
```

---

### Step 2: Remove Special Characters

```text
amanaplanacanalpanama
```

---

### Step 3: Compare Using Two Pointers

| Step | `i` | `j` | Left | Right | Match?        |
| ---- | --- | --- | ---- | ----- | ------------- |
| 1    | 0   | 20  | a    | a     | ✅            |
| 2    | 1   | 19  | m    | m     | ✅            |
| 3    | 2   | 18  | a    | a     | ✅            |
| 4    | 3   | 17  | n    | n     | ✅            |
| ...  | ... | ... | ...  | ...   | ✅            |
| Done | —   | —   | —    | —     | Return `true` |

---

## Visual Dry Run

```text
Original

A man, a plan, a canal: Panama

↓

Lowercase

a man, a plan, a canal: panama

↓

Remove spaces & symbols

amanaplanacanalpanama

↓

a m a n a p l a n a c a n a l p a n a m a
↑                                         ↑

Match ✅

Move both pointers

  ↑                                     ↑

Match ✅

Move

    ↑                                 ↑

Match ✅

...

Pointers meet

Answer = true
```

---

## Another Example

### Input

```text
s = "race a car"
```

Cleaned string:

```text
raceacar
```

| Step | Left | Right | Match? |
| ---- | ---- | ----- | ------ |
| 1    | r    | r     | ✅     |
| 2    | a    | a     | ✅     |
| 3    | c    | c     | ✅     |
| 4    | e    | a     | ❌     |

Return

```text
false
```

---

## Example with Empty String

### Input

```text
s = " "
```

After removing spaces:

```text
""
```

Since an empty string reads the same forwards and backwards,

Answer =

```text
true
```

---

## Why Do We Create a New String?

Original string:

```text
A man, a plan, a canal: Panama
```

Comparing directly would fail because of:

- Spaces
- Commas
- Colon
- Uppercase letters

Instead we convert it into:

```text
amanaplanacanalpanama
```

Now palindrome checking becomes very easy.

---

## What Does This Regex Mean?

```js
/[a-z0-9]/i;
```

It matches:

- `a-z` → lowercase letters
- `0-9` → digits
- `i` → ignore case

Examples:

```js
"A".match(/[a-z0-9]/i); // true

"7".match(/[a-z0-9]/i); // true

"$".match(/[a-z0-9]/i); // false

" ".match(/[a-z0-9]/i); // false
```

So only letters and numbers are added to the cleaned string.

---

## Why Two Pointers?

After cleaning the string:

```text
racecar
```

Compare from both ends.

```text
r a c e c a r
↑           ↑

Match

Move inward

  ↑       ↑

Match

Move inward

    ↑   ↑

Match

Done
```

If any pair is different,

the string cannot be a palindrome.

---

## Code Walkthrough

### Convert to lowercase

```js
s = s.toLowerCase();
```

Makes comparison case-insensitive.

---

### Create cleaned string

```js
let str = "";
```

Stores only valid characters.

---

### Remove unwanted characters

```js
if (s[i].match(/[a-z0-9]/i))
```

Only letters and numbers are copied.

---

### Initialize two pointers

```js
let i = 0;
let j = str.length - 1;
```

One starts from the beginning.

The other starts from the end.

---

### Compare characters

```js
if (str[i] !== str[j]) {
  return false;
}
```

If characters differ,

it's not a palindrome.

---

### Move both pointers

```js
i++;
j--;
```

Continue checking the next pair.

---

### Return answer

```js
return true;
```

If every pair matches, the string is a palindrome.

---

## Why This Works

After removing everything except letters and numbers,

the problem becomes a simple palindrome check.

Two pointers compare the first and last character,

then move inward until the middle.

If every pair matches,

the string is a palindrome.

---

## Time Complexity

```text
O(n)
```

- Build the cleaned string → `O(n)`
- Check palindrome → `O(n)`

Overall:

```text
O(n)
```

---

## Space Complexity

```text
O(n)
```

We create a new string that may contain all characters from the original string.

---

# Revision Notes

- Convert to lowercase first.
- Remove all non-alphanumeric characters.
- Store the cleaned string.
- Use two pointers to compare both ends.
- If any pair doesn't match → `false`.
- Otherwise → `true`.

---

# Pattern to Remember

```text
Need to ignore some characters before solving?

→ First clean the input.

Then solve the simplified problem.

Cleaning the input often makes the main logic much easier.
```
