## Sqrt(x) (Using binary search)

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

### 🧠 Problem in simple words

Same problem as before — find floor value of square root of `x` without using any built-in power/sqrt function.

- x = 4 → answer 2
- x = 8 → answer 2 (since 2.828 floored is 2)

This time we solve it smartly using binary search instead of checking every number one by one.

---

### 💡 Logic / Idea

- If `x` is 0 or 1, just return `x` directly.
- We know the answer (square root) will lie somewhere between `2` and `x/2`, so we set:
  - `left = 2`
  - `right = floor(x/2)`
- Now we do normal binary search:
  - Find `mid` and check `mid * mid`
  - If it's exactly equal to `x` → mid is the answer, return it
  - If `mid * mid` is smaller than `x` → our answer might be bigger, so move `left = mid + 1`
  - If `mid * mid` is bigger than `x` → our answer might be smaller, so move `right = mid - 1`
- When the loop ends (`left > right`), the answer is not found exactly, so we return `right`. This works because at the point loop breaks, `right` is the last value where `mid*mid` was still less than or equal to `x` — basically the floor value we want.

**Simple way to remember:** we're searching for the largest number whose square doesn't cross `x`. Whenever square is too big, we shrink from right side, whenever it's too small, we push from left side.

---

### 📝 Code

```js
/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  if (x < 2) return x;

  let left = 2;
  let right = Math.floor(x / 2);

  while (left <= right) {
    let mid = left + Math.floor((right - left) / 2);
    const square = mid * mid;

    if (square === x) {
      return mid;
    }

    if (square < x) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return right;
};
```

---

### 🔍 Dry Run

Input: `x = 8`

`left = 2`, `right = floor(8/2) = 4`

| Step | `left` | `right` | `mid`         | `mid*mid` | Compare with `x=8` | Action                |
| ---- | ------ | ------- | ------------- | --------- | -------------------- | ---------------------- |
| 1    | 2      | 4       | 2+(4-2)/2 = 3 | 9         | 9 > 8                 | `right = mid-1` → 2    |
| 2    | 2      | 2       | 2+(2-2)/2 = 2 | 4         | 4 < 8                 | `left = mid+1` → 3     |
| End  | 3      | 2       | —             | —         | `left > right`, stop  | return `right` → `2`   |

**Output: `2`** ✅ (matches expected)

---

### 🔍 Dry Run 2 (exact match case)

Input: `x = 4`

`left = 2`, `right = floor(4/2) = 2`

| Step | `left` | `right` | `mid` | `mid*mid` | Compare with `x=4` | Action                  |
| ---- | ------ | ------- | ----- | --------- | -------------------- | ------------------------ |
| 1    | 2      | 2       | 2     | 4         | 4 === 4               | return `mid` → `2`       |

**Output: `2`** ✅ (exact match found directly, no need to check `right` at end)

---

### ⏱ Time & Space Complexity

- **Time:** O(log x) → because we cut search space in half every time, way faster than linear version
- **Space:** O(1) → no extra space used

---

### 🎯 Key takeaway for revision

- Same problem, but instead of checking every number (linear search), we cut the search range in half every time — this is the whole point of binary search.
- Pattern to remember: "find the largest value satisfying a condition (`mid*mid <= x`)" — this pattern repeats in a LOT of binary search problems (not just sqrt).
- When exact match doesn't happen, `right` ends up holding our floor answer — this is a common trick in these kind of binary search problems, good to remember by heart.
- Compare this with the linear search version — same problem, same core idea (checking squares), but time complexity drops from O(x) to O(log x). This comparison is a good revision point to actually feel *why* binary search matters.