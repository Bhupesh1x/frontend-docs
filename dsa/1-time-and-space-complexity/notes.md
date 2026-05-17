## Time Complexity

**What is Time Complexity?**

Time complexity measures how fast an algorithm runs as the input size increases. It helps us understand the efficiency of our code.

**Important Points to Remember:**

- Time complexity is NOT the same as the actual time taken by the code to run

- It tells us how the algorithm's speed changes when we give it more data

- The actual execution time can vary based on:
  , Programming language used (Python vs JavaScript vs Java)
  , Computer specifications (fast laptop vs slow laptop)
  , Other programs running at the same time

- We measure time complexity using "Big O" notation

**What is Big O Notation?**

Big O notation shows the worst case scenario. We always consider the maximum time an algorithm might take because:
, It helps us prepare for the worst situation
, For most cases, optimized and unoptimized code perform similarly in best cases
, The worst case tells us the true performance limit

**Common Time Complexities (from fastest to slowest):**

O(1) > O(log n) > O(n) > O(n log n) > O(n²) > O(n³) > O(n!)

**Detailed Explanation with Examples:**

**O(1) → Constant Time**

Meaning: The algorithm takes the same time no matter how big the input is
, Real life example: Taking out a specific book from a bookshelf when you know its exact position
, Code example:

```javascript
console.log(arr[4]); // Always takes same time
let x = 5 + 3; // Always takes same time
```

**O(log n) → Logarithmic Time**

, Meaning: Each step cuts the problem size in half
, The algorithm gets only slightly slower even with much larger inputs
, Real life example: Finding a word in a dictionary by opening it in the middle, then halving again
, Code example: Binary Search

Comparison table:

| Input Size | Steps Needed |
| ---------- | ------------ |
| 10         | 3            |
| 100        | 7            |
| 1000       | 10           |
| 10000      | 13           |

Notice: Even when input grows 10x, steps increase by only 3!

**O(n) → Linear Time**

, Meaning: Time grows directly with input size
, If input doubles, time doubles
, Real life example: Reading every name in a phone book to find someone
, Code example: Linear Search, single loop through array

Comparison table:

| Input Size | Steps Needed |
| ---------- | ------------ |
| 10         | 10           |
| 100        | 100          |
| 1000       | 1000         |
| 10000      | 10000        |

Code example:

```javascript
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]); // Visits each element once
}
```

**O(n log n) → Linearithmic Time**

, Meaning: Combination of linear and logarithmic
, One loop that runs n times, and inside it something that takes log n time
, Real life example: Efficient sorting methods like organizing cards
, Code example: Merge Sort, Quick Sort

**O(n²) → Quadratic Time**

, Meaning: Time grows as the square of input size
, Happens when you have a loop inside another loop
, If input doubles, time becomes 4 times longer
, Real life example: Comparing every person in a room with every other person
, Code example: Bubble Sort, nested loops

Code example:

```javascript
for (let i = 0; i < arr.length; i++) {
  for (let j = 0; j < arr.length; j++) {
    // Compare arr[i] with arr[j]
  }
}
```

Comparison table:

| Input Size | Steps Needed |
| ---------- | ------------ |
| 10         | 100          |
| 100        | 10,000       |
| 1000       | 1,000,000    |

**O(n³) → Cubic Time**

, Three nested loops
, Very slow for large inputs
, Example: Three nested loops comparing elements

**O(n!) → Factorial Time**

, Extremely slow, even for small inputs
, Example: Finding all possible arrangements of items

---

### Space Complexity

**What is Space Complexity?**

Space complexity measures how much extra memory an algorithm needs to solve a problem.

**Important Points:**

- We only count EXTRA space, not the input itself
- Think of it as "How much additional memory do I need?"

**What Counts as Space:**

**Constant Space O(1):**
, Simple variables like i, j, k, count, sum
, A few numbers or strings that don't grow with input
, Example:

```javascript
let sum = 0; // Just one number
let temp = arr[0]; // Just storing one value
for (let i = 0; i < arr.length; i++) {
  // i is just one variable
  sum = sum + arr[i];
}
```

**Linear Space O(n):**
, Creating new arrays based on input size
, Making copies of data
, Example:

```javascript
// Input array
let arr = [1, 4, 8, 6];

// Creating NEW array (takes extra space)
let doubled = [];
for (let i = 0; i < arr.length; i++) {
  doubled.push(arr[i] * 2);
}
// Output: doubled = [2, 8, 16, 12]
```

Here, the `doubled` array takes O(n) space because its size depends on input size.

**Another Example:**

```javascript
// O(1) space (just modifying existing array)
function doubleInPlace(arr) {
  for (let i = 0; i < arr.length; i++) {
    arr[i] = arr[i] * 2;
  }
}

// O(n) space (creating new array)
function doubleNewArray(arr) {
  let result = []; // NEW array
  for (let i = 0; i < arr.length; i++) {
    result.push(arr[i] * 2);
  }
  return result;
}
```
