## First Bad Version

```md
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Examples:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

---

Input: n = 1, bad = 1
Output: 1
```

## 🧠 What's the problem asking

You have versions from 1 to n. One version is bad, and once a version is bad, every version after it is also bad. So the versions look something like:

`good, good, good, bad, bad, bad`

You get a function `isBadVersion(version)` that tells you true or false. You need to find the FIRST bad one, and you should call the api as less times as possible (so no linear checking one by one).

## 💡 The idea

Since the array is basically sorted like `false false false true true true`, this becomes a binary search problem. We are searching for the first `true` in this pattern.

Normal binary search finds an exact value. Here we are finding a **boundary point** - the point where it switches from false to true. So the logic changes a bit.

## 🔑 Key logic to remember

- `l = 0`, `r = n` (not n-1, we take full range till n)
- Loop condition is `l < r`, not `l <= r`
- Why not `l <= r`? Because once l and r become equal, that itself is our answer. We don't need to compare anymore at that point.
- If `isBadVersion(m)` is **false** → bad version is somewhere after m, so `l = m + 1`
- If `isBadVersion(m)` is **true** → m could itself be the first bad version, so we can't throw it away. That's why `r = m` and NOT `r = m - 1`
- When loop ends, `l === r`, and that value is your answer

Basically the rule of thumb here is: whenever mid could be a valid answer, don't eliminate it, keep it in range by setting `r = m`.

## 📝 Code

```js
var solution = function (isBadVersion) {
  return function (n) {
    let l = 0;
    let r = n;

    while (l < r) {
      const m = l + Math.floor((r - l) / 2);

      if (!isBadVersion(m)) {
        l = m + 1;
      } else {
        r = m;
      }
    }

    return r;
  };
};
```

## 🔍 Dry Run

Input: `n = 5`, bad version = `4`

(meaning versions 1,2,3 are good, versions 4,5 are bad)

| Step | `l` | `r` | `m` | `isBadVersion(m)` | Action        |
| ---- | --- | --- | --- | ------------------ | ------------- |
| Init | 0   | 5   | —   | —                   | start         |
| 1    | 0   | 5   | 2   | false               | `l → 3`       |
| 2    | 3   | 5   | 4   | true                | `r → 4`       |
| 3    | 3   | 4   | 3   | false               | `l → 4`       |
| Done | 4   | 4   | —   | —                   | loop ends, `l == r == 4` |

**Answer: 4** ✅ matches expected output

### Why this dry run matters

Notice in Step 2, `m = 4` came out `true`, but we still kept 4 in the search space by doing `r = m` instead of throwing it away with `r = m - 1`. If we had done `m - 1` there, we would have lost 4 completely from our search range and might have jumped to a wrong answer. This is the whole trick of this pattern.

## ⏱️ Time & Space

- Time: `O(log n)` — because we're halving the search space every time
- Space: `O(1)` — no extra space used

## 🎯 Pattern to remember for revision

This is basically the **"find first true in a false...false true...true array"** pattern. Any time you see a problem like:

- Find first bad version
- Find first element greater than X
- Find boundary/point where condition flips

...think of this same template:

```
l = 0, r = n
while l < r:
    m = l + (r - l) / 2
    if condition_false(m): l = m + 1
    else: r = m
return l  // or r, both same at the end
```