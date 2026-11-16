## Find First and Last Position of Element in Sorted Array

```md
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Examples

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

---

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

---

Input: nums = [], target = 0
Output: [-1,-1]
```

## 🔎 Find First and Last Position of Element in Sorted Array

**Tags:** Binary Search, Array

### 🧠 Problem in short

We get a sorted array and a target number. We need to find where this target starts and where it ends in the array (its first index and last index).

If the target is not there at all, just return `[-1, -1]`.

The tricky part is we can't just loop through the array (that's O(n)). We have to do it in O(log n), which means binary search is the way to go.

### 💡 Core idea

Normal binary search stops the moment it finds the target. But here we don't just want "does it exist", we want "where does it start and where does it end".

So the trick is: run binary search **twice**.

- **First pass** → when we find the target, don't stop. Save the index, then keep searching on the **left side** (`r = m - 1`) to see if there's an even earlier occurrence.
- **Second pass** → same idea, but keep searching on the **right side** (`l = m + 1`) to find the last occurrence.

Basically we are not settling for the first match we get, we keep pushing the boundary until binary search can't find target anymore, and whatever we saved last is our answer.

### 🖊️ My code

```js
/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function (arr, target) {
  let l = 0;
  let r = arr.length - 1;

  let res = [-1, -1];

  // First binary search -> find the first occurrence of target
  while (l <= r) {
    const m = l + Math.floor((r - l) / 2);

    if (arr[m] == target) {
      res[0] = m;
      r = m - 1; // don't stop, go left to check for an earlier one
    } else if (arr[m] < target) {
      l = m + 1;
    } else {
      r = m - 1;
    }
  }

  l = 0;
  r = arr.length - 1;

  // Second binary search -> find the last occurrence of target
  while (l <= r) {
    const m = l + Math.floor((r - l) / 2);

    if (arr[m] == target) {
      res[1] = m;
      l = m + 1; // don't stop, go right to check for a later one
    } else if (arr[m] < target) {
      l = m + 1;
    } else {
      r = m - 1;
    }
  }

  return res;
};
```

### 🔍 Dry Run

**Input:** `nums = [5, 7, 7, 8, 8, 10]`, `target = 8`

Index map for reference:

| index | 0   | 1   | 2   | 3   | 4   | 5   |
| ----- | --- | --- | --- | --- | --- | --- |
| value | 5   | 7   | 7   | 8   | 8   | 10  |

#### Pass 1 — finding the first occurrence

| Step | `l` | `r` | `m` | `arr[m]` | Compare with target | Action                |
| ---- | --- | --- | --- | -------- | -------------------- | --------------------- |
| Init | 0   | 5   | —   | —        | —                     | start                 |
| 1    | 0   | 5   | 2   | 7        | 7 < 8                 | `l = 3`               |
| 2    | 3   | 5   | 4   | 8        | match ✅              | `res[0] = 4`, `r = 3` |
| 3    | 3   | 3   | 3   | 8        | match ✅              | `res[0] = 3`, `r = 2` |
| End  | 3   | 2   | —   | —        | `l > r`, stop         | first index = `3`     |

#### Pass 2 — finding the last occurrence

| Step | `l` | `r` | `m` | `arr[m]` | Compare with target | Action                |
| ---- | --- | --- | --- | -------- | -------------------- | --------------------- |
| Init | 0   | 5   | —   | —        | —                     | start                 |
| 1    | 0   | 5   | 2   | 7        | 7 < 8                 | `l = 3`               |
| 2    | 3   | 5   | 4   | 8        | match ✅              | `res[1] = 4`, `l = 5` |
| 3    | 5   | 5   | 5   | 10       | 10 > 8                | `r = 4`               |
| End  | 5   | 4   | —   | —        | `l > r`, stop         | last index = `4`      |

**Final answer:** `[3, 4]` ✅

### ⚠️ Edge case worth remembering

**Input:** `nums = [5, 7, 7, 8, 8, 10]`, `target = 6`

Since `6` is not in the array, both passes will end without ever hitting the `arr[m] == target` condition. So `res` stays `[-1, -1]` the whole time and that's what gets returned.

Also for an empty array (`nums = []`), `l = 0` and `r = -1` right at the start, so the while loop `l <= r` never runs even once, and we directly return `[-1, -1]`. Good to keep in mind, this case gets handled automatically, no extra `if` needed.

### 📌 Things to remember for revision

- One binary search finds *a* match. Two binary searches (one biased left, one biased right) find the *range*.
- Never `break` when you find the target here — that's the whole point, you keep shrinking the search space in one direction.
- `m = l + Math.floor((r - l) / 2)` is used instead of `(l + r) / 2` to avoid overflow issues (habit worth keeping even in JS).
- Time complexity: `O(log n)` because we still just do two separate binary searches, not a linear scan.
- Space complexity: `O(1)`, only using a few variables.