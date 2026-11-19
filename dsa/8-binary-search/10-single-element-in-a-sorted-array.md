## Single Element in a Sorted Array

```md
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Examples:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Input: nums = [3,3,7,7,10,11,11]
Output: 10
```
---

### The Main Idea

Think about a normal sorted array where every number appears twice, no single element.
In that case, pairs always start at an **even index**:

index: 0 1 2 3 4 5
value: 1 1 2 2 3 3

So first of every pair is at even index, second is at odd index.

Now if we insert one extra single element somewhere, everything **after** that single element gets shifted by one position. So the "pairs start at even index" pattern breaks after the single element.

So the whole trick is: **check whether the pattern is still following even-odd rule around the middle, and shrink the search side accordingly.**

We don't even need to check even/odd of index directly (though that's another common way to solve it). This code instead checks the **length of the left/right block** between the middle and the boundary to decide which side to search.

---

### Approach used in this code

At every step, take mid `m`.

- If `arr[m] == arr[m-1]` → mid is the second element of a pair, so the pair is `(m-1, m)`.
  - Now look at how many elements are between `l` and `m-1` (that's `leftDist`).
  - If `leftDist` is **odd**, it means the left side has a broken pattern → single element is on the left → move `r = m - 2`.
  - If `leftDist` is **even**, left side pattern is fine → single element is on the right → move `l = m + 1`.

- If `arr[m] == arr[m+1]` → mid is the first element of a pair, so pair is `(m, m+1)`.
  - Check `rightDist` (elements between `m+1` and `r`).
  - If `rightDist` is **odd** → single element is on the right → move `l = m + 2`.
  - If `rightDist` is **even** → single element is on the left → move `r = m - 1`.

- If `arr[m]` matches **neither** neighbour → `arr[m]` is the single element itself. Return it.

---

### 🔍 Dry Run

Input: `[1, 1, 2, 3, 3, 4, 4, 8, 8]` (indexes 0 to 8)
Answer should be `2` (at index 2)

| Step | `l` | `r` | `m` | `arr[m]` | Compare with neighbours | Distance check | Action |
|------|-----|-----|-----|----------|--------------------------|-----------------|--------|
| Init | 0 | 8 | — | — | — | — | start |
| 1 | 0 | 8 | 4 | `3` | `arr[3]=3` → matches left neighbour | leftDist = `m-1-l` = `3-0` = 3 → **odd** | pattern broken on left → `r = m-2 = 2` |
| 2 | 0 | 2 | 1 | `1` | `arr[0]=1` → matches left neighbour | leftDist = `0-0` = 0 → **even** | left side fine → `l = m+1 = 2` |
| 3 | 2 | 2 | 2 | `2` | `arr[1]=1`, `arr[3]=3` → matches neither | — | found it! return `arr[2] = 2` |

**Done → Answer = 2**

---

### Another Quick Dry Run (single element at the start)

Input: `[3, 3, 7, 7, 10, 11, 11]`
Answer should be `10` (at index 4)

| Step | `l` | `r` | `m` | `arr[m]` | Compare with neighbours | Distance check | Action |
|------|-----|-----|-----|----------|--------------------------|-----------------|--------|
| Init | 0 | 6 | — | — | — | — | start |
| 1 | 0 | 6 | 3 | `7` | `arr[2]=7` → matches left neighbour | leftDist = `2-0` = 2 → **even** | left fine → `l = m+1 = 4` |
| 2 | 4 | 6 | 5 | `11` | `arr[4]=10` no match, `arr[6]=11` → matches right neighbour | rightDist = `r-(m+1)` = `6-6` = 0 → **even** | right side fine → `r = m-1 = 4` |
| 3 | 4 | 4 | 4 | `10` | `arr[3]=7`, `arr[5]=11` → matches neither | — | found it! return `arr[4] = 10` |

**Done → Answer = 10**

---

### Code

```js
function isOdd(num) {
  return num % 2 !== 0;
}

/**
 * @param {number[]} arr
 * @return {number}
 */
var singleNonDuplicate = function (arr) {
  let l = 0;
  let r = arr.length - 1;

  while (l <= r) {
    const m = l + Math.floor((r - l) / 2);

    if (arr[m] == arr[m - 1]) {
      let leftDist = m - 1 - l;

      if (isOdd(leftDist)) {
        r = m - 1 - 1;
      } else {
        l = m + 1;
      }
    } else if (arr[m] == arr[m + 1]) {
      let rightDist = r - (m + 1);

      if (isOdd(rightDist)) {
        l = m + 1 + 1;
      } else {
        r = m - 1;
      }
    } else {
      return arr[m];
    }
  }
};
```

---

### Things to remember before interview / revision

- Array size is always **odd** (since one element is alone, rest are pairs).
- Don't do a plain binary search — check the **pair pattern**, not just value comparison.
- The core check is: after mid, is the "even index starts pair" rule still holding or broken?
- Whichever side has the broken pattern (odd distance) — the single element is hiding there.
- When `arr[m]` doesn't match `arr[m-1]` or `arr[m+1]` — that's your answer, stop right there.
- Time: `O(log n)`, Space: `O(1)` — matches the constraint asked in the problem.

---

### Related Pattern

This falls under **"Binary Search on Answer / Property"** style problems — where we're not searching for a value directly, but searching based on a condition/pattern holding true or false on each half.