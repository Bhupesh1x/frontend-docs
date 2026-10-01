## Remove Outermost Parentheses Using Level Pointer

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

### 🧠 Problem in short
We get a valid parentheses string. It is actually made up of small valid pieces glued together (called primitive parts). Each primitive part starts with `(` and ends with its matching `)`, and nothing outside it is balanced in between.

We just need to remove the **outer** `(` and `)` of every primitive part and join everything back.

Example:
`(()())(())` → primitive parts are `(()())` and `(())` → remove outer bracket from each → `()()` + `()` = `()()()`

---

### 💡 Core Idea (Level Pointer)
Keep a counter called `level`. It tells us how deep we are inside brackets right now.

- Every time we see `(` → `level` goes up by 1
- Every time we see `)` → `level` goes down by 1

Now the trick:
- The **very first** `(` of a primitive part (when level becomes 1) is an outer bracket → skip it
- The **very last** `)` of a primitive part (when level becomes 0) is also an outer bracket → skip it
- Everything else in between → keep it as it is

So basically:
- Add `(` to answer only if `level was not 1` after increasing
- Add `)` to answer only if `level is not 0` after decreasing

---

### 🧾 Code
```js
var removeOuterParentheses = function (s) {
  let level = 0;
  let ans = "";

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      level = level + 1;
      if (level !== 1) {
        ans = ans + s[i];
      }
    } else {
      level = level - 1;
      if (level !== 0) {
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

| Step | i | char | level (after) | Outer bracket? | Action | ans so far |
|------|---|------|----------------|-----------------|--------|------------|
| 1 | 0 | `(` | 1 | ✅ yes (opening of 1st part) | skip | `""` |
| 2 | 1 | `(` | 2 | ❌ no | add | `"("` |
| 3 | 2 | `)` | 1 | ❌ no | add | `"()"` |
| 4 | 3 | `(` | 2 | ❌ no | add | `"()("` |
| 5 | 4 | `)` | 1 | ❌ no | add | `"()()"` |
| 6 | 5 | `)` | 0 | ✅ yes (closing of 1st part) | skip | `"()()"` |
| 7 | 6 | `(` | 1 | ✅ yes (opening of 2nd part) | skip | `"()()"` |
| 8 | 7 | `(` | 2 | ❌ no | add | `"()()("` |
| 9 | 8 | `)` | 1 | ❌ no | add | `"()()()"` |
| 10 | 9 | `)` | 0 | ✅ yes (closing of 2nd part) | skip | `"()()()"` |

**Final Output:** `"()()()"` ✅ matches the expected answer.

Notice how every time `level` hits `1` (going up) or `0` (going down), that bracket is an outer one and gets skipped. That's the whole trick.

---

### ⏱️ Time & Space Complexity
- **Time:** `O(n)` — we go through the string once
- **Space:** `O(n)` — for the answer string (not counting output)

---

### 📝 Things to remember for revision
- `level` tells you how deep you are — think of it like floors of a building
- Ground floor entry/exit (level 0 ↔ 1) = outer bracket = always skip
- Anything above ground floor = inner bracket = always keep
- No need for a stack here, a simple counter does the job
- This pattern (counting depth with a variable instead of a stack) is useful in many bracket-related problems, so remember it well