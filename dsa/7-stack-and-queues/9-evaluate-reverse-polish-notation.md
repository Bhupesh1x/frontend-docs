## Evaluate Reverse Polish Notation

```md
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

- The valid operators are '+', '-', '\*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

Examples:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) \* 3) = 9

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

### What's the problem asking

We get a list of tokens that form a math expression, but written in Reverse Polish Notation (postfix). That means the operator comes *after* the two numbers, not between them.

Example: `["2","1","+","3","*"]` means `(2 + 1) * 3 = 9`

We just need to solve this expression and return the final number.

### The main idea

Use a **stack**.

- If the token is a number, push it on the stack.
- If the token is an operator (`+ - * /`), pop the top two numbers, do the operation, push the result back.

Keep doing this till the end. Whatever is left in the stack is your answer.

The only tricky part is the **order** — when you pop two numbers, the one you popped first is actually the second operand, not the first. So for `5 - 3`, you push 3 first then 5 (top of stack), you pop `a = 3` then `b = 5`, and the real operation is `b - a` not `a - b`.

Also division should truncate toward zero, not just floor it (matters for negative numbers). That's why we use `Math.trunc` instead of `Math.floor`.

### Code

```js
const operations = {
  "+": (a, b) => a + b,
  "-": (a, b) => a - b,
  "*": (a, b) => a * b,
  "/": (a, b) => Math.trunc(a / b),
};

/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
  let stack = [];

  for (let i = 0; i < tokens.length; i++) {
    const curr = tokens[i];

    if (!operations[curr]) {
      stack.push(parseInt(curr));
    } else {
      const a = stack.pop();
      const b = stack.pop();

      const operationFn = operations[curr];
      const res = operationFn(b, a);
      stack.push(res);
    }
  }

  return stack[0];
};
```

### 🔍 Dry Run

Input: `tokens = ["4","13","5","/","+"]`

| Step | `i` | Token | Is Operator? | Stack Before | Action                          | Stack After |
| ---- | --- | ----- | ------------- | ------------- | -------------------------------- | ------------ |
| 1    | 0   | `4`   | ❌            | `[]`          | push 4                          | `[4]`        |
| 2    | 1   | `13`  | ❌            | `[4]`         | push 13                         | `[4,13]`     |
| 3    | 2   | `5`   | ❌            | `[4,13]`      | push 5                          | `[4,13,5]`   |
| 4    | 3   | `/`   | ✅            | `[4,13,5]`    | pop a=5, pop b=13 → trunc(13/5)=2 | `[4,2]`      |
| 5    | 4   | `+`   | ✅            | `[4,2]`       | pop a=2, pop b=4 → 4+2=6         | `[6]`        |
| Done | —   | —     | —             | `[6]`         | return stack[0]                 | `6`          |

**Output:** `6` ✅ matches `(4 + (13/5)) = 6`

### Things to remember for revision

- Numbers go on stack. Operators pop 2, calculate, push back.
- Order matters: first pop = `a` (right side), second pop = `b` (left side). Do `b (operator) a`, not `a (operator) b`.
- Use `Math.trunc` for division, not `Math.floor` — handles negative division correctly.
- At the end, only one number will remain in stack — that's your answer.

### Complexity

- **Time:** O(n) — one pass through tokens
- **Space:** O(n) — worst case, stack holds all numbers before any operator shows up