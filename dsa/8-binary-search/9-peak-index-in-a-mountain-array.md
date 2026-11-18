## Peak Index in a Mountain Array

```md
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

Examples

Input: arr = [0,1,0]

Output: 1

---

Input: arr = [0,2,1,0]

Output: 1

---

Input: arr = [0,10,5,2]

Output: 1
```


### 💡 Logic (in simple words)
Since the array first goes up then goes down, at any middle point `m` we just check one thing:

- If `arr[m] < arr[m+1]` → we are still climbing up, so the peak must be somewhere on the right. Move `l` to `m+1`.
- Else (`arr[m] >= arr[m+1]`) → we are coming down (or standing on the peak itself), so the peak is at `m` or on the left side. Move `r` to `m`.

Keep shrinking `l` and `r` like this until both meet at the same index — that index is the peak.

We don't move `r` to `m-1` because `m` itself could be the answer, so we can't throw it away.

### 🧑‍💻 Code
```js
/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function (arr) {
  let l = 0;
  let r = arr.length - 1;

  // Keep going till l == r, that leftover index is the peak
  while (l < r) {
    const m = l + Math.floor((r - l) / 2);

    // still going up, peak is on the right
    if (arr[m] < arr[m + 1]) {
      l = m + 1;
    }
    // going down or on peak, peak is here or on the left
    else {
      r = m;
    }
  }

  return l;
};
```

### 🔍 Dry Run

Input: `arr = [0, 10, 5, 2]`

| Step | `l` | `r` | `m` | `arr[m]` | `arr[m+1]` | Going up? | Action                  |
| ---- | --- | --- | --- | -------- | ---------- | --------- | ----------------------- |
| Init | 0   | 3   | —   | —        | —          | —         | start                   |
| 1    | 0   | 3   | 1   | 10       | 5          | ❌ No     | `10 >= 5`, so `r = 1`   |
| 2    | 0   | 1   | 0   | 0        | 10         | ✅ Yes    | `0 < 10`, so `l = 1`    |
| Done | 1   | 1   | —   | —        | —          | —         | `l == r`, return `1`    |

Answer: **1** ✅ (matches expected output)

### ⏱️ Complexity
- **Time:** `O(log n)` — we cut the search space in half every time, just like normal binary search.
- **Space:** `O(1)` — no extra array or structure used.

### 🎯 Things to remember for revision
- This is basically binary search, just the "condition to move" is different — here we check slope (going up or down) instead of checking a target value.
- Never do `r = m - 1`. Since `m` might be the actual peak, cutting it out can make us miss the answer.
- Loop condition is `l < r`, not `l <= r`, because we want to stop exactly when both point to the same index (the peak), not cross over.
- Works only because array strictly goes up then strictly goes down — no flat parts, no duplicates at the top.