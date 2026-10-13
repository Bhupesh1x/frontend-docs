## Next Greater Element II (Without double array)

```md
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Examples:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
```

**Pattern:** Monotonic Stack + Circular Array (space optimized)

### 🧠 The Idea (in plain words)

This is the same problem as before, but instead of actually creating a new array of double size, we just **pretend** it's double by using `i % n` to wrap around. This saves us the extra space of creating a doubled array.

The core logic is exactly the same as the double array version — monotonic stack, decreasing from bottom to top, go right to left, throw away useless smaller numbers. Only difference is how we access elements.

### 🔑 The `i % n` Trick

Instead of looping `i` from `0` to `n-1` on a real doubled array, we loop `i` from `0` to `2n-1` (here written as going from `2n-2` down to `0`, i.e. reverse direction) and every time we access the array, we use `arr[i % n]` instead of `arr[i]`.

So when `i` goes beyond `n-1`, `i % n` just wraps back to the start of the original array — giving the same effect as duplicating the array, but without actually using extra memory for it.

Think of it like a clock. The array is like clock numbers 0 to n-1, and `i % n` just keeps going around the clock instead of drawing a bigger clock face.

### 💻 Code

```js
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function (arr) {
  let stack = [];

  let n = arr.length;
  let ans = new Array(n);

  stack.push(arr[n - 1]);
  ans[n - 1] = -1;

  for (let i = 2 * n - 2; i >= 0; i--) {
    const top = stack[stack.length - 1];
    const curr = arr[i % n];

    if (top > curr) {
      ans[i % n] = top;
    } else {
      while (stack.length && stack[stack.length - 1] <= curr) {
        stack.pop();
      }

      if (stack.length) {
        ans[i % n] = stack[stack.length - 1];
      } else {
        ans[i % n] = -1;
      }
    }

    stack.push(curr);
  }

  return ans;
};
```

### ⚙️ Steps (in simple words)

1. Don't create a new doubled array. Just decide the loop should run from `2n-2` down to `0` (this covers two full passes over the array, same as before).
2. Every time you need to read an element, use `arr[i % n]` — this wraps the index back to start once it crosses `n-1`.
3. Same as before: keep a stack, compare with top, pop useless smaller elements, find next greater or `-1`.
4. Store answer at `ans[i % n]` (not `ans[i]`, since `ans` is only of original size `n`).
5. First pass (i from `2n-2` to `n-1`, roughly) mostly builds up the stack. Second pass (i from `n-2` to `0`) is where most real answers settle. Some answers get overwritten during the second pass — that's normal and expected, the final overwrite is the correct one.
6. Return `ans` directly — no slicing needed this time since we never made it bigger than `n`.

### 🔍 Dry Run

Input: `nums = [1, 2, 3, 4, 3]` → `n = 5`

**Init:** push `arr[4] = 3` → stack = `[3]`, `ans[4] = -1`

Loop `i` goes from `8` down to `0`. Note `idx = i % n`.

| i | idx (`i % n`) | curr | stack (before) | top vs curr | action | stack (after) | ans[idx] |
|---|---|---|---|---|---|---|---|
| 8 | 3 | 4 | `[3]` | 3 > 4 ❌ | pop 3, stack empty | `[4]` | -1 |
| 7 | 2 | 3 | `[4]` | 4 > 3 ✅ | top is answer | `[4,3]` | 4 |
| 6 | 1 | 2 | `[4,3]` | 3 > 2 ✅ | top is answer | `[4,3,2]` | 3 |
| 5 | 0 | 1 | `[4,3,2]` | 2 > 1 ✅ | top is answer | `[4,3,2,1]` | 2 |
| 4 | 4 | 3 | `[4,3,2,1]` | 1 > 3 ❌ | pop 1, pop 2, pop 3, top now 4 | `[4,3]` | 4 *(overwrites -1)* |
| 3 | 3 | 4 | `[4,3]` | 3 > 4 ❌ | pop 3, pop 4, stack empty | `[4]` | -1 *(stays -1)* |
| 2 | 2 | 3 | `[4]` | 4 > 3 ✅ | top is answer | `[4,3]` | 4 *(stays 4)* |
| 1 | 1 | 2 | `[4,3]` | 3 > 2 ✅ | top is answer | `[4,3,2]` | 3 *(stays 3)* |
| 0 | 0 | 1 | `[4,3,2]` | 2 > 1 ✅ | top is answer | `[4,3,2,1]` | 2 *(stays 2)* |

Final `ans`: `[2, 3, 4, -1, 4]` ✅ matches expected output.

Notice `ans[4]` got a temporary wrong-ish value `-1` in the first pass, then got corrected to `4` in the second pass. This is exactly why we need two passes — the first pass alone isn't reliable since the stack hasn't seen everything yet.

### ⏱️ Time & Space

- **Time:** `O(n)` — total iterations are `2n`, and every element is still pushed/popped from stack at most once.
- **Space:** `O(n)` — only for `ans` and `stack`. This is the improvement over the double-array version, which used `O(n)` extra just to store the doubled array too.

### 🎯 What to remember for revision

- `i % n` is a clean way to simulate a circular / doubled array without actually building one.
- Loop range becomes `2n-2` to `0` (or `0` to `2n-1` if going forward) to simulate two full passes.
- Answers can get overwritten during the second pass — don't panic seeing a value change, the last write (from the second pass) is the correct final answer.
- Same stack logic as normal next-greater-element, the circular part is purely handled by the index math, not the stack logic.
- This version is preferred in interviews since it shows you can optimize space without changing the core idea.