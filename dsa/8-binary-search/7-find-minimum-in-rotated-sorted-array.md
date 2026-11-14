## Find Minimum in Rotated Sorted Array

```md
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.
  Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Examples

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

---

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

---

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

### The Problem (in short)

A sorted array got rotated some number of times. Find the smallest number in it — but you're not allowed to just loop through everything, it has to run in `O(log n)`.

Example:
`[4,5,6,7,0,1,2]` → answer is `0`
`[11,13,15,17]` → answer is `11` (not rotated at all, still valid)

---

### How I think about it

Since the array is rotated, it's basically made of two sorted chunks stuck together. Somewhere in there, there's a "break point" — the spot where a bigger number is followed by a smaller one. That smaller number is our answer.

So instead of scanning everything, I do binary search and keep asking: *"is my left half already sorted?"*

- If `arr[l] <= arr[r]`, that means this part of the array isn't rotated anymore — it's just a normal sorted piece. So the smallest value here is simply `arr[l]`. Done.
- If not, the rotation point is still hiding somewhere inside, so I pick the middle and check it against the element right before it. If `arr[m] < arr[m-1]`, I got lucky — `arr[m]` itself is the minimum.
- Otherwise, I check which side is sorted (`arr[l] <= arr[m]` means left side is sorted), and move toward the side that's NOT sorted, because that's where the rotation point must be hiding.

Basically: keep throwing away the sorted half, chase the unsorted half.

---

### Code

```js
/**
 * @param {number[]} arr
 * @return {number}
 */
var findMin = function (arr) {
  let l = 0;
  let r = arr.length - 1;

  while (l <= r) {
    // if this part of array is already sorted, leftmost is the smallest
    if (arr[l] <= arr[r]) {
      return arr[l];
    }

    const m = l + Math.floor((r - l) / 2);

    // if mid is smaller than the guy before it, mid IS the minimum
    if (arr[m] < arr[m - 1]) {
      return arr[m];
    }

    // check which half is sorted, move towards the unsorted half
    if (arr[l] <= arr[m]) {
      l = m + 1;
    } else {
      r = m - 1;
    }
  }
};
```

---

### 🔍 Dry Run — Example 1

Input: `[4, 5, 6, 7, 0, 1, 2]`

| Step | `l` | `r` | `m` | `arr[l]` | `arr[r]` | `arr[m]` | `arr[m-1]` | Check                       | Action              |
| ---- | --- | --- | --- | -------- | -------- | -------- | ---------- | --------------------------- | ------------------- |
| 1    | 0   | 6   | 3   | 4        | 2        | 7        | 6          | `arr[l]<=arr[r]`? No. `arr[m]<arr[m-1]`? No. Left sorted (`4<=7`)? Yes | move right → `l = 4` |
| 2    | 4   | 6   | —   | 0        | 2        | —        | —          | `arr[l]<=arr[r]`? Yes (`0<=2`) | this part is sorted, return `arr[l]` |

**Answer: `0`**

Only took 2 rounds even for a 7-element array — that's the whole point of doing this in log(n) instead of scanning one by one.

---

### 🔍 Dry Run — Example 2 (mid itself is the answer)

Input: `[5, 6, 7, 1, 2, 3, 4]`

| Step | `l` | `r` | `m` | `arr[l]` | `arr[r]` | `arr[m]` | `arr[m-1]` | Check                                   | Action              |
| ---- | --- | --- | --- | -------- | -------- | -------- | ---------- | ---------------------------------------- | ------------------- |
| 1    | 0   | 6   | 3   | 5        | 4        | 1        | 7          | `arr[l]<=arr[r]`? No. `arr[m]<arr[m-1]`? Yes (`1<7`) | found it, return `arr[m]` |

**Answer: `1`**

This is the case where we get lucky right in the first check — the middle element itself turns out to be the drop point.

---

### Edge Cases to remember

- Array not rotated at all → `arr[l] <= arr[r]` is true right away, returns `arr[l]` immediately.
- Only 1 element → loop runs once, `arr[l] <= arr[r]` is trivially true, returns that element.
- Minimum sitting at index 0 → still works, because eventually the search space shrinks down to just that sorted piece.

---

### Why this is `O(log n)`

Every round we're throwing away one whole half of the array (the sorted half), so the search space keeps cutting in half — classic binary search behavior, just with a slightly trickier condition to decide which half to drop.

---

### One-line takeaway

> Find the sorted half, trust it, ignore it. Keep chasing the messy half — that's where the minimum is hiding.