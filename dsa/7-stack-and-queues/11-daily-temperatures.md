## Daily Temperatures

```md
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Examples:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

---

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

---

Input: temperatures = [30,60,90]
Output: [1,1,0]
```

**Pattern:** Monotonic Stack (keep a decreasing stack of indices)

---

### Problem in short

For every day, find out how many days you need to wait to get a warmer temperature. If no warmer day comes after, put `0`.

Input: [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]


---

### Core Idea

Go from the **end of array to start**.

Keep a stack of indices. This stack always has indices whose temperature is in **decreasing order** (top to bottom... well top has smallest going up).

For every new day (from right to left):
- If the day at top of stack has a **higher temp** than current day → answer is just 1 day wait (next day itself is warmer).
- If not, keep **popping** the stack until you find a day with higher temp than current, or stack becomes empty.
  - If found → answer = (index of that day - current index)
  - If stack empty → no warmer day ahead → answer = 0
- Push current index into stack (so next days behind it can check against it)

Basically the stack always stores "days that are still waiting for a warmer day".

---

### Code

```js
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var dailyTemperatures = function (arr) {
  let stack = [];

  let n = arr.length;
  let res = new Array(n);

  stack.push(n - 1);
  res[n - 1] = 0;

  for (let i = n - 2; i >= 0; i--) {
    const topVal = arr[stack[stack.length - 1]];
    const curr = arr[i];

    if (topVal > curr) {
      res[i] = 1;
    } else {
      while (stack.length && arr[stack[stack.length - 1]] <= curr) {
        stack.pop();
      }
      if (stack.length) {
        res[i] = stack[stack.length - 1] - i;
      } else {
        res[i] = 0;
      }
    }

    stack.push(i);
  }

  return res;
};
```

---

### 🔍 Dry Run

Input: `[73, 74, 75, 71, 69, 72, 76, 73]` (indices 0 to 7)

We start from the last index and move left.

| Step | `i` | `arr[i]` | Top of Stack (idx → val) | Compare (top > curr?) | What Happens | Stack After | `res[i]` |
|------|-----|----------|---------------------------|------------------------|--------------|--------------|----------|
| Init | 7   | 73       | —                         | —                      | first day, nothing ahead | `[7]` | `res[7]=0` |
| 1    | 6   | 76       | 7 → 73                    | ❌ 73 > 76 false        | pop 7 (73 ≤ 76), stack empty now, so no warmer day | `[6]` | `res[6]=0` |
| 2    | 5   | 72       | 6 → 76                    | ✅ 76 > 72 true         | top is already warmer, answer = 1 | `[6,5]` | `res[5]=1` |
| 3    | 4   | 69       | 5 → 72                    | ✅ 72 > 69 true         | top is already warmer, answer = 1 | `[6,5,4]` | `res[4]=1` |
| 4    | 3   | 71       | 4 → 69                    | ❌ 69 > 71 false        | pop 4 (69≤71), now top is 5→72, 72>71 stop popping. answer = 5-3 = 2 | `[6,5,3]` | `res[3]=2` |
| 5    | 2   | 75       | 3 → 71                    | ❌ 71 > 75 false        | pop 3 (71≤75), pop 5 (72≤75), now top is 6→76, 76>75 stop. answer = 6-2 = 4 | `[6,2]` | `res[2]=4` |
| 6    | 1   | 74       | 2 → 75                    | ✅ 75 > 74 true         | top already warmer, answer = 1 | `[6,2,1]` | `res[1]=1` |
| 7    | 0   | 73       | 1 → 74                    | ✅ 74 > 73 true         | top already warmer, answer = 1 | `[6,2,1,0]` | `res[0]=1` |

**Final Answer:** `[1,1,4,2,1,1,0,0]` ✅ matches expected output

---

### Why stack and not brute force?

Brute force = for every day, check every future day one by one → O(n²).

Here, every index gets pushed once and popped at most once from the stack → each index touched max 2 times → **O(n)** overall.

---

### Things to remember for revision

- We move **right to left**, not left to right.
- Stack holds **indices**, not values (we need to calculate distance later, so index is more useful).
- Stack is kept in a way that values go **decreasing from bottom to top**... wait actually think of it as: we only keep days which are still "waiting" for a warmer day. So whenever we find a bigger value while moving left, we throw away (pop) all smaller waiting days because current bigger day will answer for them too if needed later, but they already got their answer as soon as current day appeared? No — actually popping happens because those popped days already found their warmer day = the current day itself. So don't confuse — popped ones already got answered mentally, we just don't need them in stack anymore.
- Last index always gets `0` because nothing is ahead of it.
- Time: `O(n)`, Space: `O(n)` (for stack + result array)

---

### Quick Recap Line (for fast revision)

> Traverse from back, maintain a stack of "still waiting" indices, pop until you find someone warmer, distance between indices is your answer, push current index back in.