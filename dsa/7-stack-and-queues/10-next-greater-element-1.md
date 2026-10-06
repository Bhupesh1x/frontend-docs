## Next Greater Element I

```md
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above

Examples:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:

- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

---

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:

- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
```

### 🧠 What's it asking
You get two arrays, `nums1` and `nums2`. Every number in `nums1` also exists somewhere in `nums2`.

For every number in `nums1`, go find it inside `nums2`, then look to its **right** and find the first number that's bigger than it. That's its "next greater element". If nothing bigger is found on the right, answer is `-1`.

`nums1` is basically just asking "give me answers for these specific numbers", but all the real work happens on `nums2`.

### 💡 The idea (Monotonic Stack)
This is a classic **monotonic decreasing stack** problem.

Trick: go through `nums2` from **right to left**, and keep a stack where numbers are always in decreasing order (top to bottom... well top is smallest here, read below).

Why right to left? Because "next greater on the right" — if we walk backwards, whatever is already in the stack IS "stuff to the right" of current number. So we just check the stack.

Steps:
1. Push the last element first, its answer is always `-1` (nothing to its right).
2. Walk backwards from second-last to first.
3. For current number `curr`, look at stack's top:
   - if top is bigger than `curr` → that's the answer, done.
   - if top is smaller or equal → keep popping until you find something bigger, or stack becomes empty.
4. Whatever you land on (or `-1` if stack empty) is the answer for `curr`.
5. Push `curr` onto stack before moving to next number.
6. Store every answer in a map (number → its next greater), so at the end you just look up answers for `nums1`.

Basically the stack is holding "candidates that could still be someone's next greater element", and we throw away numbers that are too small because they'll never be anyone's answer once a bigger number shows up.

### 🔍 Dry Run

Input: `nums2 = [1, 3, 4, 2]`, `nums1 = [4, 1, 2]`

**Setup:** push last element first → `stack = [2]`, `map = {2: -1}`

| Step | `i` | `curr` | Stack (before) | Top | Compare | Action | Stack (after) | Map so far |
|------|-----|--------|-----------------|-----|---------|--------|-----------------|------------|
| 1 | 2 | 4 | `[2]` | 2 | 2 > 4? ❌ | pop 2 (too small), stack empty → answer is `-1` | `[4]` | `{2:-1, 4:-1}` |
| 2 | 1 | 3 | `[4]` | 4 | 4 > 3? ✅ | top is the answer → `map[3] = 4` | `[4, 3]` | `{2:-1, 4:-1, 3:4}` |
| 3 | 0 | 1 | `[4, 3]` | 3 | 3 > 1? ✅ | top is the answer → `map[1] = 3` | `[4, 3, 1]` | `{2:-1, 4:-1, 3:4, 1:3}` |

**Now build result for `nums1 = [4, 1, 2]`** using the map:
- `4 → -1`
- `1 → 3`
- `2 → -1`

**Output:** `[-1, 3, -1]` ✅ matches expected

### ⏱ Time & Space
- **Time:** `O(n)` — every number gets pushed and popped from the stack at most once.
- **Space:** `O(n)` — for the stack and the map.

### 🧵 Code
```js
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function (nums1, nums2) {
  let stack = [];
  let map = new Map();

  let n = nums2.length;

  stack.push(nums2[n - 1]);
  map.set(nums2[n - 1], -1);

  for (let i = n - 2; i >= 0; i--) {
    const top = stack[stack.length - 1];
    const curr = nums2[i];

    if (top > curr) {
      map.set(curr, top);
    } else {
      while (stack.length && stack[stack.length - 1] <= curr) {
        stack.pop();
      }

      if (stack.length) {
        map.set(curr, stack[stack.length - 1]);
      } else {
        map.set(curr, -1);
      }
    }

    stack.push(curr);
  }

  let res = [];
  for (let i = 0; i < nums1.length; i++) {
    res.push(map.get(nums1[i]));
  }

  return res;
};
```

### 📝 Things to remember
- Whenever you see "next greater / next smaller" → think **monotonic stack**.
- Going **right to left** makes "next on the right" checks easy, since stack already holds right-side elements.
- Stack should stay **decreasing** — pop anything smaller or equal, because it can never be the answer for future numbers once a bigger one shows up.
- Use a **map** to store answers by value since `nums1` values need to be looked up separately, not by index of `nums2`.
- If stack becomes empty while popping → answer is `-1`, nothing bigger exists to the right.