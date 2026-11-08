## Find Peak Element

```md
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Examples:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

---

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```
---

### 🧠 The Idea (in simple words)

A peak is just an element which is bigger than both its neighbours. Think of the array as a mountain range with ups and downs. We don't need to check every element — we can use binary search because at any point, we can tell which side has a peak just by looking at the slope.

Here's the trick:
- Pick the middle element `m`.
- Compare it with the element right next to it `m+1`.
- If `arr[m] < arr[m+1]` → we are going **uphill**. That means somewhere on the right side there has to be a peak (because the array is bounded by `-∞` on both ends, it can't keep going up forever). So move `l = m + 1`.
- If `arr[m] > arr[m+1]` → we are going **downhill** (or `m` itself is the peak). So the peak is at `m` or somewhere to its left. Move `r = m`.

Keep shrinking the search space like this until `l === r`. That point is your peak.

No need to check both neighbours (`m-1` and `m+1`) — comparing with just `m+1` is enough to know which direction to go.

---

### 💻 Code

```js
/**
 * @param {number[]} arr
 * @return {number}
 */
var findPeakElement = function (arr) {
  let l = 0;
  let r = arr.length - 1;

  while (l < r) {
    const m = l + Math.floor((r - l) / 2);

    // If next element is bigger, we're on the "up" slope.
    // Peak must be somewhere to the right, so move l forward.
    if (arr[m] < arr[m + 1]) {
      l = m + 1;
    }
    // Otherwise we're on the "down" slope (or m itself is the peak).
    // Peak is at m or to its left, so shrink r to m.
    else {
      r = m;
    }
  }

  // l === r here, this is our peak index.
  return l;
};
```

---