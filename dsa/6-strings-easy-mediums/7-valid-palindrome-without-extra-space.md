# Valid Palindrome (Without Extra Space)

## Problem

A string is considered a palindrome if:

- Convert all uppercase letters to lowercase.
- Ignore all non-alphanumeric characters.
- The remaining characters read the same forward and backward.

Return `true` if the string is a palindrome, otherwise return `false`.

---

## Solution (Without Extra Space)

```js
var isPalindrome = function (s) {
  s = s.toLowerCase();

  let i = 0;
  let j = s.length - 1;

  while (i < j) {
    // Skip invalid characters from the left
    if (!s[i].match(/[a-z0-9]/i)) {
      i++;
      continue;
    }

    // Skip invalid characters from the right
    if (!s[j].match(/[a-z0-9]/i)) {
      j--;
      continue;
    }

    // Compare valid characters
    if (s[i] !== s[j]) {
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

Unlike the previous solution, we **do not create a new cleaned string**.

Instead,

- One pointer starts from the left.
- Another pointer starts from the right.
- Whenever a pointer reaches a special character, skip it.
- Compare only valid letters and numbers.

This saves extra memory.

---

## Step-by-Step Algorithm

1. Convert the string to lowercase.
2. Place one pointer at the beginning.
3. Place another pointer at the end.
4. If the left character isn't alphanumeric, move the left pointer.
5. If the right character isn't alphanumeric, move the right pointer.
6. Compare the valid characters.
7. If they don't match, return `false`.
8. Continue until the pointers meet.
9. Return `true`.

---

## Dry Run

### Input

```text
s = "A man, a plan, a canal: Panama"
```

After lowercase:

```text
a man, a plan, a canal: panama
```

| Step | `i` | `j` | Left | Right | Action        |
| ---- | --- | --- | ---- | ----- | ------------- |
| 1    | 0   | 29  | a    | a     | Match         |
| 2    | 1   | 28  | " "  | m     | Skip left     |
| 3    | 2   | 28  | m    | m     | Match         |
| 4    | 3   | 27  | a    | a     | Match         |
| 5    | 4   | 26  | n    | n     | Match         |
| ...  | ... | ... | ...  | ...   | Continue      |
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

a   m a n ,   a   p l a n ,   a   c a n a l :   p a n a m a
↑                                                           ↑

Compare

a == a ✅

Move

  ↑                                                       ↑

Space ❌

Skip it

    ↑                                                   ↑

m == m ✅

Move

      ↑                                               ↑

a == a ✅

...

Eventually both pointers meet

Answer = true
```

---

## Another Example

### Input

```text
s = "race a car"
```

After lowercase:

```text
race a car
```

| Step | Left | Right | Action       |
| ---- | ---- | ----- | ------------ |
| 1    | r    | r     | Match        |
| 2    | a    | a     | Match        |
| 3    | c    | c     | Match        |
| 4    | e    | a     | Not Equal ❌ |

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

Both pointers point to an invalid character.

The space is skipped.

Pointers cross each other.

No mismatch is found.

Answer:

```text
true
```

---

## Why Do We Skip Characters?

Consider:

```text
A man, a plan
```

The space and comma should not affect the answer.

Instead of creating:

```text
amanaplan
```

we simply skip them while moving the pointers.

Example:

```text
a   m a n
 ↑

Space?

Skip

Now compare the next valid character.
```

---

## What Does This Regex Mean?

```js
/[a-z0-9]/i;
```

It matches:

- Letters (`a-z`)
- Numbers (`0-9`)
- `i` means ignore uppercase/lowercase differences.

Examples:

```js
"A".match(/[a-z0-9]/i); // true

"8".match(/[a-z0-9]/i); // true

"!".match(/[a-z0-9]/i); // false

" ".match(/[a-z0-9]/i); // false
```

Only valid characters are compared.

---

## Why Do We Use `continue`?

When an invalid character is found:

```js
if (!s[i].match(/[a-z0-9]/i)) {
    i++;
    continue;
}
```

We move the pointer and immediately start the next iteration.

This prevents us from comparing invalid characters.

Example:

```text
a , b

^

Comma

Skip

Continue

Now compare b
```

---

## Code Walkthrough

### Convert to lowercase

```js
s = s.toLowerCase();
```

Makes comparison case-insensitive.

---

### Initialize two pointers

```js
let i = 0;
let j = s.length - 1;
```

- `i` starts from the left.
- `j` starts from the right.

---

### Skip invalid character from the left

```js
if (!s[i].match(/[a-z0-9]/i)) {
    i++;
    continue;
}
```

Ignore spaces and symbols.

---

### Skip invalid character from the right

```js
if (!s[j].match(/[a-z0-9]/i)) {
    j--;
    continue;
}
```

Do the same from the other side.

---

### Compare characters

```js
if (s[i] !== s[j]) {
  return false;
}
```

If they differ,

the string cannot be a palindrome.

---

### Move both pointers

```js
i++;
j--;
```

Continue comparing the next pair.

---

### Return answer

```js
return true;
```

If no mismatch is found,

the string is a palindrome.

---

## Why This Works

Both pointers always point to valid characters.

Special characters are ignored automatically.

Each valid pair is compared exactly once.

If every pair matches,

the string is a palindrome.

---

## Extra Space vs No Extra Space

| Using Extra Space            | Without Extra Space                     |
| ---------------------------- | --------------------------------------- |
| Build a cleaned string first | Compare directly in the original string |
| Easier to understand         | Slightly more optimized                 |
| Extra memory required        | No extra string needed                  |
| Space: `O(n)`                | Space: `O(1)`                           |

---

## Time Complexity

```text
O(n)
```

Every character is visited at most once.

---

## Space Complexity

```text
O(1)
```

No extra string or array is created.

Only two pointers are used.

---

# Revision Notes

- Convert to lowercase.
- Use two pointers.
- Skip spaces and special characters.
- Compare only letters and numbers.
- If any valid pair doesn't match → `false`.
- Otherwise → `true`.
- More space-efficient than creating a cleaned string.

---

# Pattern to Remember

```text
Need to ignore unwanted characters?

Instead of creating a new string,

move the pointers until they reach valid characters.

Then compare only the useful characters.

This is a common two-pointer optimization.
```
