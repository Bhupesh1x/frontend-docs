## Guess Number Higher or Lower

```md
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

- -1: Your guess is higher than the number I picked (i.e. num > pick).
- 1: Your guess is lower than the number I picked (i.e. num < pick).
- 0: your guess is equal to the number I picked (i.e. num == pick).
  Return the number that I picked.

Examples:

Input: n = 10, pick = 6
Output: 6

---

Input: n = 1, pick = 1
Output: 1

---

Input: n = 2, pick = 1
Output: 1
```

**Pattern:** Binary Search (classic template)

### 💡 Idea in simple words

You are guessing a number between 1 and n. Instead of guessing one by one, you guess the middle number every time. The `guess()` function tells you if you need to go higher or lower. Keep shrinking the range till you find it. This is just plain binary search, only difference is the "check" is done through an API call instead of a normal comparison.

### 🧠 Why Binary Search works here

The numbers 1 to n are sorted in a simple increasing order. Every guess splits the range into two halves, and we throw away the half we don't need. This is the exact condition needed for binary search — a sorted range where we can decide "go left or go right" at every step.

### 🪜 Steps

1. Take two pointers, `l = 1` and `r = n`.
2. While `l <= r`:
   - Find `mid`.
   - Call `guess(mid)`.
   - If result is `0` → mid is the answer, return it.
   - If result is `1` → our guess is too low, move `l = mid + 1`.
   - If result is `-1` → our guess is too high, move `r = mid - 1`.
3. Loop keeps shrinking till we land on the exact number.

### 🧾 Code

```js
/**
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */
var guessNumber = function (n) {
  let l = 1;
  let r = n;

  while (l <= r) {
    const mid = l + Math.floor((r - l) / 2);

    const guessRes = guess(mid);

    if (guessRes === 0) return mid;

    if (guessRes === 1) {
      l = mid + 1;
    } else {
      r = mid - 1;
    }
  }
};
```

### 🔍 Dry Run

Input: `n = 10`, `pick = 6`

| Step | `l` | `r` | `mid` | `guess(mid)` | Meaning              | Action        |
| ---- | --- | --- | ----- | ------------ | -------------------- | ------------- |
| Init | 1   | 10  | —     | —            | —                     | start         |
| 1    | 1   | 10  | 5     | 1            | 5 is lower than pick  | `l = 6`       |
| 2    | 6   | 10  | 8     | -1           | 8 is higher than pick | `r = 7`       |
| 3    | 6   | 7   | 6     | 0            | 6 is the pick!        | return `6`    |

So in just 3 guesses we found the number, instead of checking 1,2,3,4,5,6 one by one (which would take 6 tries).

### ⏱️ Time & Space

- **Time:** `O(log n)` → range gets cut in half every time
- **Space:** `O(1)` → only using pointers, no extra memory

### 🎯 Key Takeaway (for revision)

- Whenever you see "sorted range" + "tells you higher/lower" → binary search
- The `guess()` API is just replacing the normal `if (arr[mid] > target)` check
- Template to remember: `l <= r`, calculate `mid`, decide left/right, shrink range
- This is basically the same skeleton as normal binary search, just wrapped around an API call instead of an array