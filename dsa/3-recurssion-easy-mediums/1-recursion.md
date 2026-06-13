# Recursion

## What is Recursion?

- Recursion is when a function calls itself to solve a smaller version of the same problem.
- Instead of using loops, the function keeps calling itself until some condition stops it.

---

## Real Life Idea

Think about climbing stairs.

- To reach the top, you first reach one step before the top.
- To reach that step, you first reach one step before that.

Problem becomes smaller and smaller.

That is the basic idea of recursion.

---

## Two Parts of Recursion

### 1. Base Case

- Stop condition.
- Without base case, recursion will run forever.

```js
if (count > n) return;
```

---

### 2. Recursive Case

- Part where function calls itself again. To solve a small problem

```js
printCount(n, count + 1);
```

---

## Basic Example

```js
function printCount(n, count = 1) {
  // base case
  if (count > n) return;

  // work
  console.log(count);

  // recursive case
  printCount(n, count + 1);
}

printCount(5);
```

---

## Output

```js
1;
2;
3;
4;
5;
```

---

## How Recursion Works Internally

Every function call gets stored in memory stack.

Flow:

```txt
printCount(5,1)
printCount(5,2)
printCount(5,3)
printCount(5,4)
printCount(5,5)
printCount(5,6) -> stop
```

Then functions start finishing one by one.

---

## 🔍 Dry Run

Input:

```js
printCount(3);
```

| Step | Function Call     | Condition `count > n` | Output | Next Call         |
| ---- | ----------------- | --------------------- | ------ | ----------------- |
| 1    | `printCount(3,1)` | `1 > 3` ❌            | `1`    | `printCount(3,2)` |
| 2    | `printCount(3,2)` | `2 > 3` ❌            | `2`    | `printCount(3,3)` |
| 3    | `printCount(3,3)` | `3 > 3` ❌            | `3`    | `printCount(3,4)` |
| 4    | `printCount(3,4)` | `4 > 3` ✅            | —      | stop              |

---

## Important Things to Remember

### 1. Every recursion needs a base case

Without base case:

```js
function test() {
  test();
}
```

This causes:

```txt
Maximum call stack size exceeded
```

---

### 2. Problem should become smaller

Good recursion:

```js
n - 1;
```

Bad recursion:

```js
n + 1;
```

---

### 3. Recursive calls use stack memory

Because every function call waits for the next function to finish.

---

## Basic Pattern of Recursion

```js
function solve(problem) {
  // base case
  if (problem is finished) return;

  // work

  // recursive call
  solve(smaller problem);
}
```

---

## Time Complexity

Depends on:

- How many recursive calls are happening
- How much work each call is doing

---

## Space Complexity

Recursion uses extra stack space.

If function runs `n` times recursively:

```txt
Space Complexity = O(n)
```

---

## Small Revision Notes

- Function calling itself = recursion
- Base case = stopping condition
- Recursive case = function calls itself
- Problem should become smaller
- Recursion uses call stack
- Missing base case causes stack overflow
