## Rotting Oranges

```md
You are given an m x n grid where each cell can have one of three values:

- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Examples

![rotting-oranges](./assets/rotting-oranges.png)

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

---

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

---

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
```

**Type:** Grid + BFS (multi-source)

### What's the problem asking

We have a grid of oranges. `0` = empty cell, `1` = fresh orange, `2` = rotten orange.
Every minute, a fresh orange next to a rotten one (up/down/left/right, not diagonal) also becomes rotten.

We need to find how many minutes it takes for **all** fresh oranges to rot. If some orange can never be reached, return `-1`.

### How to think about it

This is a classic **multi-source BFS** problem. Normally in BFS we start from one point, but here we can have many rotten oranges at the same time, and they all spread together minute by minute.

So the trick is:

1. First pass — scan the whole grid and push **every rotten orange** into the queue with time `0`.
2. Then do BFS from all of them at once. Each level of BFS = 1 minute passing.
3. Whenever a fresh orange gets rotten, push it into the queue with `level + 1`.
4. Keep track of the max level reached — that's your answer.
5. At the end, do one more scan — if any `1` (fresh orange) is still left, it means it was unreachable, so return `-1`.

Why multi-source works: since all rotten oranges start rotting things at the same time, doing BFS from all of them together naturally gives the correct minute count, no need to run BFS separately for each one.

### Code

```js
/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function (grid) {
  let queue = [];
  let m = grid?.length;
  let n = grid[0]?.length;

  // push all rotten oranges first, these are our starting points
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 2) {
        queue.push([i, j, 0]);
      }
    }
  }

  let maxMinutes = 0;
  while (queue.length) {
    let [x, y, level] = queue.shift();

    // right
    if (y < n - 1 && grid?.[x][y + 1] === 1) {
      grid[x][y + 1] = 2;
      queue.push([x, y + 1, level + 1]);
    }

    // left
    if (y > 0 && grid?.[x][y - 1] === 1) {
      grid[x][y - 1] = 2;
      queue.push([x, y - 1, level + 1]);
    }

    // up
    if (x > 0 && grid?.[x - 1][y] === 1) {
      grid[x - 1][y] = 2;
      queue.push([x - 1, y, level + 1]);
    }

    // down
    if (x < m - 1 && grid?.[x + 1][y] === 1) {
      grid[x + 1][y] = 2;
      queue.push([x + 1, y, level + 1]);
    }

    maxMinutes = Math.max(maxMinutes, level);
  }

  // check if any fresh orange is left untouched
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 1) {
        return -1;
      }
    }
  }

  return maxMinutes;
};
```

> Note: the comments in the code say "top/bottom" but they're actually checking right/left/up/down — just a naming slip, logic is correct. Fixed the labels above for clarity while revising.

### Dry Run

Input:

2 1 1
1 1 0
0 1 1


Grid positions are `(row, col)`. Queue starts with all `2`s.

| Step | Popped (x,y,level) | Right check | Left check | Up check | Down check | Grid after this step | maxMinutes |
|------|--------------------|-------------|------------|----------|------------|------------------------|------------|
| Init | — | — | — | — | — | `211 / 110 / 010` | 0 |
| 1 | (0,0,0) | (0,1)=1 → rot, push(0,1,1) | y=0, skip | x=0, skip | (1,0)=1 → rot, push(1,0,1) | `221 / 210 / 010` | 0 |
| 2 | (0,1,1) | (0,2)=1 → rot, push(0,2,2) | (0,0)=2, skip | x=0, skip | (1,1)=1 → rot, push(1,1,2) | `222 / 220 / 010` | 1 |
| 3 | (1,0,1) | (1,1)=2, skip | y=0, skip | (0,0)=2, skip | (2,0)=0, skip | `222 / 220 / 010` | 1 |
| 4 | (0,2,2) | y at edge, skip | (0,1)=2, skip | x=0, skip | (1,2)=0, skip | `222 / 220 / 010` | 2 |
| 5 | (1,1,2) | (1,2)=0, skip | (1,0)=2, skip | (0,1)=2, skip | (2,1)=1 → rot, push(2,1,3) | `222 / 220 / 020` → `222/220/021`* | 2 |
| 6 | (2,1,3) | (2,2)=1 → rot, push(2,2,4) | (2,0)=0, skip | (1,1)=2, skip | x at edge, skip | `222 / 220 / 022` | 3 |
| 7 | (2,2,4) | edge, skip | (2,1)=2, skip | (1,2)=0, skip | edge, skip | `222 / 220 / 022` | 4 |

*(small typo self-correction while tracing — final grid after step 5 is `222/220/021` meaning row2 = `0,2,1` since only col1 rotted, col2 still fresh, which then rots in step 6)*

Queue empty now. Final scan → no `1` left → return `maxMinutes = 4` ✅ matches expected output.

### Complexity

- **Time:** `O(m * n)` — every cell is visited at most once during BFS, plus the two scans (finding initial rotten oranges, checking leftover fresh ones).
- **Space:** `O(m * n)` — worst case, queue can hold almost all cells.

### Things to remember for revision

- This is **multi-source BFS**, not single-source. Push all rotten oranges together at the start, not one at a time.
- The `level` value in the queue is basically "time elapsed" — track the max of it, don't just count BFS depth blindly.
- Don't forget the final leftover check for `1`s — that's the only way to catch the `-1` case.
- Directions check order doesn't matter for correctness, just don't miss any of the 4.
- If you're doing this in an interview, mention why multi-source BFS is better than running BFS from each rotten orange separately (it would give wrong/overlapping minute counts).