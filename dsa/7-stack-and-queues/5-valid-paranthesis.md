## Valid Parentheses

### 🧠 Problem in Simple Words

You get a string made of brackets only — `(`, `)`, `{`, `}`, `[`, `]`.

You need to check if the brackets are "balanced" properly. That means:
- Every opening bracket should have a matching closing bracket of the same type.
- The order matters — you can't close a bracket before closing the one that came after it.

Basically, if you open something, you must close it in the right order before moving on.

---

### 💡 Core Idea

Whenever we see an **opening bracket**, we just push it onto a stack and move on — we'll deal with it later.

Whenever we see a **closing bracket**, we check the top of the stack. The top of the stack should be the matching opening bracket. If it is, pop it and continue. If it's not, the string is invalid.

At the end, if the stack is empty, it means everything got closed properly.

**Why a stack?** Because the last bracket we opened is the first one that needs to be closed (LIFO order). That's exactly how a stack works.

---

### 🔑 Extra Trick Used

Before even starting the loop, if the length of the string is odd, it can never be valid (an odd number of brackets can never fully pair up). So we return `false` immediately — this saves some unnecessary looping.

---

### 🖥️ Code

```js
function isOdd(x) {
  return x % 2 != 0;
}

const map = new Map([
  ["(", ")"],
  ["{", "}"],
  ["[", "]"],
]);

var isValid = function (s) {
  let stack = [];

  if (isOdd(s?.length)) {
    return false;
  }

  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i])) {
      stack.push(s[i]);
    } else {
      let val = map.get(stack.pop());
      if (!val || val !== s[i]) {
        return false;
      }
    }
  }

  return stack.length === 0;
};
```

---

### 🔍 Dry Run (Valid Case)

Input: `"([])"`

| Step | `i` | `s[i]` | Is Opening? | Stack Before | Action                          | Stack After |
| ---- | --- | ------ | ----------- | ------------ | -------------------------------- | ----------- |
| 1    | 0   | `(`    | ✅          | `[]`         | push `(`                         | `[(]`       |
| 2    | 1   | `[`    | ✅          | `[(]`        | push `[`                         | `[(, []`    |
| 3    | 2   | `]`    | ❌          | `[(, []`     | pop `[`, map gives `]`, matches ✅ | `[(]`       |
| 4    | 3   | `)`    | ❌          | `[(]`        | pop `(`, map gives `)`, matches ✅ | `[]`        |
| Done | —   | —      | —           | `[]`         | stack empty → return `true`      | `[]`        |

**Result:** `true` ✅

---

### 🔍 Dry Run (Invalid Case)

Input: `"([)]"`

| Step | `i` | `s[i]` | Is Opening? | Stack Before | Action                                  | Stack After |
| ---- | --- | ------ | ----------- | ------------ | ---------------------------------------- | ----------- |
| 1    | 0   | `(`    | ✅          | `[]`         | push `(`                                 | `[(]`       |
| 2    | 1   | `[`    | ✅          | `[(]`        | push `[`                                 | `[(, []`    |
| 3    | 2   | `)`    | ❌          | `[(, []`     | pop `[`, map gives `]`, but we got `)` ❌ | mismatch    |
| Done | —   | —      | —           | —            | return `false` immediately               | —           |

**Result:** `false` ❌

See the difference? In the valid case, brackets close in the exact reverse order they opened. In the invalid case, `[` was opened after `(`, but we tried to close `)` before closing `[` — that breaks the order rule.

---

### ⏱️ Time & Space Complexity

- **Time:** `O(n)` — we go through the string once.
- **Space:** `O(n)` — worst case, all characters are opening brackets and go into the stack.

---

### 🎯 Things to Remember for Revision

- Stack is the go-to structure whenever order of "opening → closing" matters.
- Odd length check is a nice early-exit trick, not compulsory but saves time.
- Always check `!val` (empty stack pop case) before comparing — otherwise popping from an empty stack silently gives `undefined` and can break your logic.
- Map is used here instead of if-else for clean and fast lookup of matching pairs.