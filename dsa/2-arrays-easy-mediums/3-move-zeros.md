**Question Description: Move Zeroes**

```js

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

```

**code**

```js
var moveZeroes = function (nums) {
  let x = 0;
  let val = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== val) {
      // Switch them so that zero are at the end
      let temp = nums[x];
      nums[x] = nums[i];
      nums[i] = temp;
      x = x + 1;
    }
  }

  return nums;
};

moveZeroes([0, 1, 0, 3, 12]);
moveZeroes([0]);
```
