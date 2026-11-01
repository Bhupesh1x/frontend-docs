## Search in Rotated Sorted Array

```md
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Examples:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

---

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

---

Input: nums = [1], target = 0
Output: -1
```

## 🧠 Problem (in simple words)

You have a sorted array, but someone rotated it from some point. Like `[4,5,6,7,0,1,2]` — this was originally `[0,1,2,4,5,6,7]` but rotated so it starts from the middle.

You need to find a target number in this rotated array and return its index. If not found, return `-1`.

Catch: you have to do it in `O(log n)` time — so normal loop search won't work, has to be binary search.

## 🔑 Core Idea

Even after rotation, **one half of the array is always properly sorted**. So at every step:

1. Find `mid`
2. Check which half (left or right) is sorted
3. Check if target lies inside that sorted half
4. If yes → search that half
5. If no → search the other half

This way you keep cutting the array in half, so it stays `O(log n)`.

## 💻 Code

```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (arr, target) {
  let l = 0;
  let r = arr.length - 1;

  while (l <= r) {
    const mid = l + Math.floor((r - l) / 2);

    if (arr[mid] === target) {
      return mid;
    }

    // left sorted: Left is less or equal to mid
    if (arr[l] <= arr[mid]) {
      // Check if target is in range of the sorted array search in left: (target < mid && target >= l)
      if (target < arr[mid] && target >= arr[l]) {
        r = mid - 1;
      }
      // If it's not in range of sorted array search in other side (right in this case)
      else {
        l = mid + 1;
      }
    }
    // right sorted: Left is greater than mid
    else {
      // Check if target is in range of the sorted array search in right: (target > mid && target <= r)
      if (target > arr[mid] && target <= arr[r]) {
        l = mid + 1;
      } else {
        r = mid - 1;
      }
    }
  }

  return -1;
};
```

## 🔍 Dry Run

Input: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`

| Step | `l` | `r` | `mid` | `arr[mid]` | Left half sorted? (`arr[l] <= arr[mid]`) | Is target in that sorted half? | Action                  |
| ---- | --- | --- | ----- | ---------- | ----------------------------------------- | ------------------------------- | ------------------------ |
| 1    | 0   | 6   | 3     | 7          | ✅ (4 <= 7)                                | ❌ (0 not between 4 and 7)      | search right → `l = 4`   |
| 2    | 4   | 6   | 5     | 1          | ✅ (0 <= 1)                                | ✅ (0 is between 0 and 1)       | search left → `r = 4`    |
| 3    | 4   | 4   | 4     | 0          | —                                          | 🎯 match found                  | return `4`               |

**Output:** `4`

### Why this works (in plain words)

- At step 1, mid value is `7`. Left side (`4 to 7`) is sorted. But `0` is not between `4` and `7`, so target must be hiding in the right part. Move `l` forward.
- At step 2, mid value is `1`. Left side (`0 to 1`) is sorted, and `0` fits between `0` and `1`. So go left. Move `r` back.
- At step 3, `l` and `r` meet at same index, mid value is `0` itself — found it.

## ⚠️ Things to remember (for revision)

- Always compare `arr[l] <= arr[mid]` first to know **which half is sorted**. Don't try to guess based on `mid` and `r`.
- Once you know the sorted half, just do a normal "is target inside this range" check.
- If target is not inside the sorted half, it has to be in the other half — no need to check that half separately.
- Use `<=` in `arr[l] <= arr[mid]` because when there's only one element left (`l == mid`), it should still count as sorted.
- This same pattern (find sorted half → check range → move pointer) is reused in a lot of "rotated array" style problems, so remember the pattern, not just this code.

## ⏱️ Complexity

- **Time:** `O(log n)` — binary search, cutting array in half every time
- **Space:** `O(1)` — no extra space used