## Min Stack

### 🧠 What's the problem asking

We need to build a stack, but with one extra power — it should tell us the **minimum value** in the stack at any point, and that too in **O(1)** time. Normal stack operations (push, pop, top) also need to stay O(1).

The tricky part is `getMin()`. If we just kept a normal stack, finding the min would mean looping through everything — that's O(n), not allowed here.

### 💡 The idea (logic)

Instead of storing just the value in the stack, we store a **pair**: `[value, minSoFar]`.

- `value` → the actual number we pushed
- `minSoFar` → the minimum value in the stack **up to and including this point**

So every time we push something new, we check: is this new value smaller than the current min? If yes, this becomes the new min. If no, the old min still holds.

Because we store the min **along with** every element, we never have to search for it — the top of the stack always knows the current min. That's the whole trick.

### 🚶 Dry Run

Input operations:

push(-2) | push(0) | push(-3) | getMin() | pop() | top() | getMin()


| Step | Operation | value | prevMin | newMin | Stack State (`[val, min]`) | Output |
|------|-----------|-------|---------|--------|------------------------------|--------|
| 1 | push(-2) | -2 | — (empty) | -2 | `[[-2,-2]]` | — |
| 2 | push(0)  | 0  | -2 | -2 | `[[-2,-2], [0,-2]]` | — |
| 3 | push(-3) | -3 | -2 | -3 | `[[-2,-2], [0,-2], [-3,-3]]` | — |
| 4 | getMin() | — | — | — | `[[-2,-2], [0,-2], [-3,-3]]` | **-3** |
| 5 | pop()    | — | — | — | `[[-2,-2], [0,-2]]` | — |
| 6 | top()    | — | — | — | `[[-2,-2], [0,-2]]` | **0** |
| 7 | getMin() | — | — | — | `[[-2,-2], [0,-2]]` | **-2** |

Notice: after `pop()`, the min automatically "goes back" to `-2` — we didn't have to recalculate anything. That's the beauty of storing min alongside each value.

### ✅ Code

```js
var MinStack = function () {
  this.s = [];
};

/**
 * @param {number} value
 * @return {void}
 */
MinStack.prototype.push = function (value) {
  if (this.s.length === 0) {
    this.s.push([value, value]);
  } else {
    let prevMinVal = this.getMin();
    let minValue = Math.min(prevMinVal, value);

    this.s.push([value, minValue]);
  }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
  this.s.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
  const lastVal = this.s[this.s.length - 1];
  const [val, _minVal] = lastVal;

  return val;
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
  const lastVal = this.s[this.s.length - 1];
  const [_val, minVal] = lastVal;

  return minVal;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(value)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
```

### ⏱️ Time & Space

- **Time:** O(1) for push, pop, top, getMin — no loops anywhere
- **Space:** O(n) — because every element stores 2 numbers instead of 1 (val + min)

### 🎯 Things to remember for revision

- Trick = store `[value, minSoFar]` together, not just `value`
- `getMin()` never searches — it just peeks at top and picks second item
- When you `pop()`, the previous min is already sitting right there in the next top element, so nothing breaks
- This is a classic **"carry extra info with each stack element"** pattern — same idea shows up in problems like max stack, stock span, etc.

---