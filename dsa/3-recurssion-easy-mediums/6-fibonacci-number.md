# Fibonacci Number

## Problem Statement

Given an integer `n`, return the `nth` Fibonacci number.

The Fibonacci sequence is defined as:

- `F(0) = 0`
- `F(1) = 1`
- `F(n) = F(n - 1) + F(n - 2)`

### Examples

```js
Input: n = 0;
Output: 0;

Input: n = 4;
Output: 3;

Input: n = 7;
Output: 13;
```

Explanation:

```txt
Fibonacci sequence:

0, 1, 1, 2, 3, 5, 8, 13
```

---

# Code

```js
// 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610

function fib(n) {
  // base cases
  if (n === 0) return 0;
  if (n === 1) return 1;

  // recursive case
  return fib(n - 1) + fib(n - 2);
}

console.log(fib(8));
```

---

# Simple Idea

Every Fibonacci number is made using previous two numbers.

Formula:

```txt
fib(n) = fib(n - 1) + fib(n - 2)
```

Example:

```txt
fib(5)

= fib(4) + fib(3)

= 3 + 2

= 5
```

So recursion keeps breaking the problem into smaller Fibonacci problems.

---

# Base Cases

```js
if (n === 0) return 0;
if (n === 1) return 1;
```

Why?

Because first two Fibonacci numbers are already known.

```txt
fib(0) = 0
fib(1) = 1
```

These stop the recursion.

---

# Recursive Case

```js
return fib(n - 1) + fib(n - 2);
```

Meaning:

```txt
current fibonacci number
=
previous fibonacci number
+
one more previous fibonacci number
```

Example:

```js
fib(4) = fib(3) + fib(2)
```

---

# 🔍 Dry Run

## Input

```js
n = 4;
```

## Function Call

```js
fib(4);
```

| Step | Function Call | Breaks Into       | Returned Value |
| ---- | ------------- | ----------------- | -------------- |
| 1    | `fib(4)`      | `fib(3) + fib(2)` | `2 + 1 = 3`    |
| 2    | `fib(3)`      | `fib(2) + fib(1)` | `1 + 1 = 2`    |
| 3    | `fib(2)`      | `fib(1) + fib(0)` | `1 + 0 = 1`    |
| 4    | `fib(1)`      | Base Case         | `1`            |
| 5    | `fib(0)`      | Base Case         | `0`            |

Final Answer:

```js
3;
```

---

# Recursive Flow

## Example: `fib(5)`

```txt
fib(5)

= fib(4) + fib(3)

= (fib(3) + fib(2)) + (fib(2) + fib(1))

= ((fib(2) + fib(1)) + (fib(1) + fib(0)))
  +
  ((fib(1) + fib(0)) + 1)

= ((1 + 1) + (1 + 0))
  +
  ((1 + 0) + 1)

= (2 + 1) + (1 + 1)

= 3 + 2

= 5
```

---

# 🌳 Recursion Tree

## Example: `fib(5)`

```txt
                fib(5)
              /        \
          fib(4)      fib(3)
         /     \      /     \
     fib(3) fib(2) fib(2) fib(1)
      /  \    / \    / \
 fib(2) fib(1)1  0   1   0
  / \
 1   0
```

Notice:

- same calls happen many times
- `fib(2)` repeats
- `fib(3)` repeats

That is why normal recursion becomes slow for Fibonacci.

---

## 🔍 Dry Run With Animation

![factorial_recursion_explained](./assets/fibonacci_recursion.gif)

---

![fibonacci_recursion_tree](./assets/fibonacci_recursion_tree.gif)

---

# Important Thing To Notice

This line is the main idea:

```js
return fib(n - 1) + fib(n - 2);
```

One recursive call becomes TWO recursive calls.

That is why recursion grows very fast here.

For example:

```txt
fib(5)
```

creates:

```txt
fib(4) and fib(3)
```

Then both create more recursive calls again.

---

# Time Complexity

```txt
O(2^n)
```

Because function calls keep increasing exponentially.

---

# Space Complexity

```txt
O(n)
```

Because recursive calls are stored in call stack.
