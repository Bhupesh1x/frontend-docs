## Sqrt(x) (Using linear search)

```md
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x \*\* 0.5 in python.

Examples:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

---

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```

**Topic:** Binary Search Series (Basic version using linear search first)

### 🧠 Problem in simple words

We are given a number `x`. We need to find its square root, but rounded down (floor value). We can't use any built-in power/sqrt function — we have to figure it out ourselves.

So basically, we need to find the largest number `i` such that `i * i <= x`.

**Examples:**
- x = 4 → answer is 2 (since 2*2 = 4)
- x = 8 → answer is 2 (since 2*2=4 is fine, but 3*3=9 is too big, so we stay at 2)

---

### 💡 Logic / Idea

- If `x` is 0 or 1, just return `x` directly (sqrt of 0 is 0, sqrt of 1 is 1).
- The square root of `x` can never be more than `x/2` (except for very small numbers), so we only loop till `n = x/2`. This saves us from looping all the way to `x`.
- We go one by one from `i = 0` and check `i * i`:
  - If it becomes exactly equal to `x`, that `i` is our answer.
  - If `i * i` becomes bigger than `x`, that means the previous `i` (i.e. `i - 1`) was our answer, because current `i` already overshoots.
- If loop finishes without any of these, return `n` (this handles edge cases).

Basically this is just **checking numbers one by one until we cross the limit**, that's why it's called linear search here (later this same problem is solved smartly using binary search).

---

### 📝 Code

```js
/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  if (x < 2) return x;

  const n = Math.floor(x / 2);
  for (let i = 0; i <= n; i++) {
    const square = i * i;

    if (square === x) {
      return i;
    }

    if (square > x) {
      return i - 1;
    }
  }

  return n;
};
```

---

### 🔍 Dry Run

Input: `x = 8`

`n = floor(8/2) = 4` → so we loop `i` from 0 to 4

| Step | `i` | `i*i` | Compare with `x=8`  | Action              |
| ---- | --- | ----- | -------------------- | -------------------- |
| 1    | 0   | 0     | 0 < 8                | continue              |
| 2    | 1   | 1     | 1 < 8                | continue              |
| 3    | 2   | 4     | 4 < 8                | continue              |
| 4    | 3   | 9     | 9 > 8                | return `i - 1` → `2` |

**Output: `2`** ✅ (matches expected, since √8 ≈ 2.828 → floor is 2)

---

### ⏱ Time & Space Complexity

- **Time:** O(x/2) → basically O(x), since we loop till half of x in worst case
- **Space:** O(1) → no extra space used

---

### 🎯 Key takeaway for revision

- The moment `i*i` crosses `x`, the answer is always one step behind (`i - 1`) — this trick is reused a lot in binary search versions of this same problem.
- Looping only till `x/2` instead of `x` is a small optimization, doesn't change complexity class but reduces iterations.
- This is the "brute force" way — good to remember before jumping to the binary search version of the same problem, so you can compare and see why binary search is better (O(log x) instead of O(x)).