## Next Greater Element II

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

**Pattern:** Monotonic Stack + Circular Array

### 🧠 The Idea (in plain words)

For every number, we need to find the next bigger number that comes after it — but the array is circular, so after the last element we go back to the start and keep looking.

Normal "next greater element" is a classic monotonic stack problem. Here the only twist is the circular part. The trick people use is: just pretend the array is written twice, one after another. So `[1,2,3,4,3]` becomes `[1,2,3,4,3,1,2,3,4,3]`. Now it's a normal next-greater problem on this doubled array, and we only keep answers for the first half.

We go from right to left and keep a stack of "candidates" that could be the next greater element for something on the left. The stack always keeps numbers in decreasing order from bottom to top. If the number on top of the stack is smaller or equal to the current number, it can never be the answer for anyone else on the left (because current number is bigger and closer), so we throw it away.

### 🔑 Why doubling the array works

Since answer for any index can only come from the next `n-1` positions at most (circular), looking at the array twice covers every possible circular jump. We just ignore the answers computed for the second half at the end.

### 💻 Code

```js
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function (nums) {
  let stack = [];
  let arr = [...nums, ...nums];

  let n = arr.length;
  let ans = new Array(n);

  stack.push(arr[n - 1]);
  ans[n - 1] = -1;

  for (let i = n - 2; i >= 0; i--) {
    const top = stack[stack.length - 1];
    const curr = arr[i];

    if (top > curr) {
      ans[i] = top;
    } else {
      while (stack.length && stack[stack.length - 1] <= curr) {
        stack.pop();
      }

      if (stack.length) {
        ans[i] = stack[stack.length - 1];
      } else {
        ans[i] = -1;
      }
    }

    stack.push(curr);
  }

  return ans.slice(0, nums.length);
};
```

### ⚙️ Steps (in simple words)

1. Make a doubled array by joining `nums` with itself.
2. Start from the last index of this doubled array and go backwards.
3. Keep a stack. It stores numbers that are still "waiting" to be someone's next greater element.
4. For each number, first check the top of the stack:
   - If top is already bigger than current number, that's the answer for current — done, no popping needed.
   - If top is smaller or equal, it's useless now, so pop it out. Keep popping till you find something bigger, or the stack becomes empty.
5. If stack becomes empty, there's no next greater number, so answer is `-1`.
6. Whatever the current number is, push it into the stack at the end (it might be the answer for someone further left).
7. At the end, just return the first half of the answers (since second half was only there to help with the circular part).

### 🔍 Dry Run

Input: `nums = [1,2,3,4,3]`
Doubled array: `[1,2,3,4,3, 1,2,3,4,3]` (indexes 0 to 9)

We move from index 9 to index 0.

**Init:** push `arr[9] = 3` → stack = `[3]`, `ans[9] = -1`

| i | curr (`arr[i]`) | stack (before) | top vs curr | what happens | stack (after) | ans[i] |
|---|---|---|---|---|---|---|
| 8 | 4 | `[3]` | 3 > 4 ❌ | pop 3 (3≤4), stack empty → no greater found | `[4]` | -1 |
| 7 | 3 | `[4]` | 4 > 3 ✅ | top itself is the answer | `[4,3]` | 4 |
| 6 | 2 | `[4,3]` | 3 > 2 ✅ | top itself is the answer | `[4,3,2]` | 3 |
| 5 | 1 | `[4,3,2]` | 2 > 1 ✅ | top itself is the answer | `[4,3,2,1]` | 2 |
| 4 | 3 | `[4,3,2,1]` | 1 > 3 ❌ | pop 1, pop 2, pop 3 (all ≤3), top now 4 | `[4,3]` | 4 |
| 3 | 4 | `[4,3]` | 3 > 4 ❌ | pop 3, pop 4 (both ≤4), stack empty | `[4]` | -1 |
| 2 | 3 | `[4]` | 4 > 3 ✅ | top itself is the answer | `[4,3]` | 4 |
| 1 | 2 | `[4,3]` | 3 > 2 ✅ | top itself is the answer | `[4,3,2]` | 3 |
| 0 | 1 | `[4,3,2]` | 2 > 1 ✅ | top itself is the answer | `[4,3,2,1]` | 2 |

Final `ans` (index 0 to 9): `[2, 3, 4, -1, 4, 2, 3, 4, -1, -1]`

We only take the first 5 (original length): `[2, 3, 4, -1, 4]` ✅ matches expected output.

### ⏱️ Time & Space

- **Time:** `O(n)` — even though there's a while loop inside the for loop, each element is pushed and popped from the stack at most once overall.
- **Space:** `O(n)` — for the doubled array and the stack.

### 🎯 What to remember for revision

- Circular array + "next greater/smaller" → double the array trick.
- Monotonic stack always keeps things in a sorted order (here decreasing top to bottom) so we can throw away useless smaller elements fast.
- Going right to left, the stack tells you "what's still bigger than me on my right side."
- Don't forget to cut the answer array back to original length at the end — that's the most common silly mistake here.