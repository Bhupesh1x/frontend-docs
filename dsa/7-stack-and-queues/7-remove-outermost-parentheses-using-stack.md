## Remove Outermost Parentheses Using Stack

```md
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Examples:

Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
```

### Problem (in short)

A "primitive" string is a valid parentheses string that can't be split into two smaller valid parentheses strings. Basically it's one full `(...)` block that closes completely only at the very end.

Any valid parentheses string is just a bunch of these primitive blocks joined together.

We need to remove the outer `(` and `)` from **each** primitive block and return whatever is left joined together.

**Example:**

Input: "(()())(())"
Output: "()()()"

Here the string breaks into two primitive blocks: `(()())` and `(())`.
Remove the outer bracket from each → `()()` and `()` → join → `()()()`.

---

### My Logic

Think of it like counting how "deep" you are inside brackets using a stack (or just a counter, stack is easier to picture).

- Every time you see `(`, push it.
- Every time you see `)`, pop it.

Now the trick: the **very first `(` of a primitive block** and the **very last `)` of that block** are the "outer" ones we want to skip. Every other bracket in between is safe to keep.

So:
- When we push and the stack size becomes **1** → this is an outer opening bracket → skip it, don't add to answer.
- When we pop and the stack size becomes **0** → this is an outer closing bracket → skip it, don't add to answer.
- In all other cases → this bracket is "inside" something → keep it.

That's literally the whole problem. No complex data structure needed, just track depth.

---

### Code

```js
var removeOuterParentheses = function (s) {
  let stack = [];
  let ans = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] == "(") {
      stack.push(s[i]);
      if (stack.length !== 1) {
        ans = ans + s[i];
      }
    } else {
      stack.pop(s[i]);

      if (stack.length !== 0) {
        ans = ans + s[i];
      }
    }
  }

  return ans;
};
```

---

### 🔍 Dry Run

Input: `"(()())(())"`

| Step | `i` | `s[i]` | Action     | Stack size (before → after) | Add to `ans`? | `ans` so far |
| ---- | --- | ------ | ---------- | ---------------------------- | -------------- | ------------ |
| 1    | 0   | `(`    | push       | 0 → 1                        | ❌ (outer open) | `""`         |
| 2    | 1   | `(`    | push       | 1 → 2                        | ✅              | `"("`        |
| 3    | 2   | `)`    | pop        | 2 → 1                        | ✅              | `"()"`       |
| 4    | 3   | `(`    | push       | 1 → 2                        | ✅              | `"()("`      |
| 5    | 4   | `)`    | pop        | 2 → 1                        | ✅              | `"()()"`     |
| 6    | 5   | `)`    | pop        | 1 → 0                        | ❌ (outer close)| `"()()"`     |
| 7    | 6   | `(`    | push       | 0 → 1                        | ❌ (outer open) | `"()()"`     |
| 8    | 7   | `(`    | push       | 1 → 2                        | ✅              | `"()()("`    |
| 9    | 8   | `)`    | pop        | 2 → 1                        | ✅              | `"()()()"`   |
| 10   | 9   | `)`    | pop        | 1 → 0                        | ❌ (outer close)| `"()()()"`   |

**Final Output:** `"()()()"` ✅ matches expected.

**What to notice while revising:**
- Steps 1, 6, 7, 10 are the ones getting skipped — these are exactly the outer brackets of the two primitive blocks `(()())` and `(())`.
- Every time stack size touches `0`, that means one primitive block just fully closed. That's your cue a new block starts next.

---

### Complexity

- **Time:** `O(n)` — one pass through the string.
- **Space:** `O(n)` — for the stack in worst case (all opening brackets before any closing, like `"((((...))))"`).

---

### Quick Revision Point

> Skip a bracket only when it's making the stack go from `0 → 1` (opening) or `1 → 0` (closing). Everything else, keep it.