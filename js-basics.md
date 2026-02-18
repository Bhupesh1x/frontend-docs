## How JavaScript works

- JavaScript is a single-threaded language and executes code synchronously by default.

- This means it can execute only one line of code at a time, in a specific order.

- Everything in JavaScript happens inside an Execution Context.

- An Execution Context has two parts:
  1. Memory Component (Variable Environment)
     - Stores variables and their values
     - Stores function declarations with their complete code

  2. Code Component (Thread of Execution)
     - Executes the code line by line

---

## How JavaScript Code Is Executed

Everything in JavaScript is executed inside an **execution context**.

**Global Execution Context (GEC)**

- When a JavaScript program starts, a **Global Execution Context (GEC)** is created.
- The GEC is pushed onto the **call stack**.
- All JavaScript code runs inside an execution context.

**Phases of Execution Context**

Each execution context goes through **two phases**:

1. **Memory Creation Phase**
2. **Code Execution Phase**

**Memory Creation Phase**

- JavaScript scans the entire code before execution.
- Memory is allocated for variables and functions.
- During this phase:
  - Variables are assigned a placeholder value of `undefined`.
  - Functions are stored in memory with their complete code.
- No code is executed in this phase.

**Code Execution Phase**

- JavaScript executes the code **line by line**.
- Values are assigned to variables.
- Calculations and operations are performed.
- The actual execution of the program happens in this phase.

**Function Execution**

- When JavaScript encounters a **function call**, it creates a new execution context for that function.
- This new execution context is pushed onto the **call stack**.
- The function execution context also goes through:
  - Memory Creation Phase
  - Code Execution Phase
- If JavaScript encounters a `return` statement:
  - The function’s execution context is removed (popped) from the call stack.
  - Control returns to the place where the function was called, along with the returned value.

**Call Stack**

- The **call stack** manages the order of execution of execution contexts.
- It follows the **Last In, First Out (LIFO)** principle.
- When a function finishes execution, its execution context is popped from the stack.
- After the entire program finishes execution:
  - The Global Execution Context is popped off the call stack.
- This marks the end of JavaScript program execution.

---

## Hoisting in JavaScript

**What is Hoisting?**  
Hoisting refers to JavaScript’s ability to access variables and functions **even before they are declared**.  
This happens because JavaScript allocates memory for them before execution starts.

**How JavaScript Executes Code**  
JavaScript runs code in two phases inside an Execution Context:

- **Memory Creation Phase:**
  - The entire file is scanned.
  - Memory is reserved for variables and functions.
  - Variables are initialized with `undefined`.
  - Function declarations are stored with their full function body.

- **Execution Phase:**
  - Code runs line by line.
  - Variables get assigned with actual values.
  - Functions are invoked.

Because memory is set up in advance, identifiers can be accessed earlier — that behavior is known as **hoisting**.

**Variables vs Functions**

- Function declarations are fully hoisted — you can call them before defining them.
- Variables are hoisted but set to `undefined`.
- Arrow functions and function expressions behave like variables, so they also start off as `undefined`.

**Example**

```js
console.log(x); // undefined
printHelloWorld(); // Hello world

function printHelloWorld() {
  console.log("Hello world");
}

console.log(myFunc); // undefined
myFunc(); // TypeError: myFunc is not a function

var myFunc = function () {
  console.log("Hi there");
};
```

---

## How Functions Work in JavaScript

Functions are the heart of JavaScript. We can think of them as **mini programs** that run inside the main program and have their own execution flow.

**Execution Context and Call Stack**  
When a JavaScript program starts running, a **Global Execution Context (GEC)** is created and pushed onto the **call stack**.  
Just like any execution context, it goes through two phases:

- Memory Creation Phase
- Code Execution Phase

**What Happens When a Function Is Called**  
During the code execution phase, when JavaScript encounters a function call:

- A **new execution context** is created for that function.
- This execution context is pushed on top of the call stack.
- Execution control moves to the **first line of the function body**.

Inside this function execution context:

- Memory is allocated for the function’s variables and parameters.
- The function has access to its **own memory** and also to its **parent (outer) scope**.

**Function Completion**  
Once the function finishes executing:

- Its execution context is removed (popped) from the call stack.
- Control returns back to the execution context below it.

This push-and-pop behavior of execution contexts is what allows JavaScript to manage multiple function calls efficiently.

---

## Shortest Program in JavaScript

**What is the Shortest Program?**  
In JavaScript, the shortest program is an **empty file**. Even when there is nothing to execute, JavaScript still performs its internal setup.

**What JavaScript Does Internally**  
When an empty file runs:

- A **Global Execution Context (GEC)** is created.
- It is pushed into the **call stack**.
- The **global object (`window` in browsers)** is created.
- The `this` keyword is set to refer to the global object.

**Execution Completion**  
Since there is no code to execute:

- The execution phase completes immediately.
- The global execution context is popped out of the call stack.

**Global Scope**

- Any variables or functions declared in the global scope are attached to the global object.
- The global scope includes everything that is **not inside any function**.
- The variables and functions can be accessed using window.a or directly as a as it is in global scope.

**Example**

```js
var x = 10;
console.log(x); // 10
console.log(window.x); // 10
console.log(this.x); // 10
```

---

## Undefined vs Not Defined in JavaScript

**What does `undefined` mean?**  
In JavaScript, `undefined` is a **special value**. It acts as a placeholder for variables that have been **declared but not yet assigned a value**.

When JavaScript allocates memory during the memory creation phase, variables are initialized with `undefined` until a value is assigned during execution.

**What does `not defined` mean?**  
`not defined` means that a variable or function **does not exist in the program at all**.  
It was never declared, so no memory was allocated for it.

**Key Difference**

- `undefined` → variable is declared and has memory, but no value yet
- `not defined` → variable is not declared and has no memory

Although you _can_ manually assign `undefined` as a value, its main purpose is to indicate that a variable exists but hasn’t been assigned yet.

**Example**

```js
console.log(a); // undefined
var a = 10;
console.log(a); // 10

console.log(x); // ReferenceError: x is not defined
```

---

## The Scope Chain in JavaScript

**What is Scope?**  
Scope defines what variables and functions can be accessed at a particular place in the code.

**Execution Context and Lexical Environment**  
Whenever an execution context is created in JavaScript, it contains:

- Its own **local memory**
- A **lexical environment**

The lexical environment is a reference to the local memory + lexical environment of it's **parent scope** — the place where the function is physically available in the code.

**What is the Scope Chain?**  
The whole chain of:

- Execution context local memory + lexical environment forms a scope chain
  forms the **scope chain**.

This chain determines what variables and functions are accessible in the current scope.

**How JavaScript Resolves Variables**  
When JavaScript tries to access a variable or function:

1. It first looks in the current local scope.
2. If not found, it looks in it's lexical environment.
3. This process continues up the chain until the **global scope** is reached.
4. If JavaScript cannot find the variable or function anywhere in the scope chain, it throws a `ReferenceError` saying the identifier is not defined.

The global execution context’s lexical environment points to `null`, which marks the end of the scope chain.

**Example**

```js
function a() {
  function b() {
    console.log(b); // 10
  }
  b();
}
let b = 10;
a();
```

- ![the-scope-chain](./js-basics-assets/the-scope-chain.png)

---

## let, const vs var in JavaScript

**Overview**  
`let`, `const`, and `var` differ mainly in three areas:

- Hoisting
- Strictness (redeclaration & initialization)
- Scope

**Hoisting Behavior**  
All three keywords are hoisted, meaning memory is allocated before code execution starts.

- Variables declared with `var` are initialized with `undefined` and attached to the global object.
- `let` and `const` are also hoisted and initialized with `undefined`, but they are stored in a separate memory space (script scope).
- Accessing `let` or `const` before initialization results in a `ReferenceError`. As they are in `Temporal dead zone` till they are initialized. They can be accessed only after initialized some value in it.

**Temporal Dead Zone (TDZ)**  
The time between hoisting and initialization of `let` and `const` variables is called the **Temporal Dead Zone**.

During this period:

- Variables exist in memory
- But cannot be accessed

Moving variable declarations to the top of the scope helps reduce the TDZ.

**Example**

```js
console.log(b); // Reference error

console.log(a); // undefined

var a = 10;

let b = 10;

console.log(a); // 10
console.log(b); // 10
```

**Strictness Rules**

- `var` allows redeclaration in the same scope.
- `let` and `const` do not allow redeclaration in the same scope and will throw an error.

`const` is stricter than `let`:

- It must be declared and initialized in the same statement.
- Reassignment is not allowed.
- `let` allows declaration first and initialization later.

**Example**

```js
var a = 10;

var a = "Hello world"; // allowed

let x;

x = 10; // allowed: Can be declared first and initialized letter.

let x = "Hello world"; // Error: cannot redeclare the let variables

const b = 20; // allowed

const b;

b = 10; // Syntax error: variable declared with const should be declared and initialized in the same statement.
```

**Scope Differences**

- `var` is **function-scoped**.
- `let` and `const` are **block-scoped**.

This means:

- `let` and `const` variables are accessible only within the block `{}` they are declared in.
- `var` variables can be accessed outside blocks (if not inside a function).

**Example**

```js
if (true) {
  var a = 10;
  let b = 20;
  const c = 30;

  console.log(a); // 10
  console.log(b); // 20
  console.log(c); // 30
}

console.log(a); // 10
console.log(b); // Error: Cannot access variables with let keyword outside of the block as they are block scope
console.log(c); // Error: Cannot access variables with const keyword outside of the block as they are block scope
```

---

## Block Scope & Shadowing in JavaScript

**What is a Block?**  
A block is defined using curly braces `{}` and is also known as a **compound statement**.

JavaScript uses blocks to group multiple statements in places where it expects a single statement, for example in `if`, `else`, `for`, etc.

**Why Blocks Are Needed**  
Statements like `if` do not require `{}` by syntax, but blocks are used when we want to execute **multiple statements** instead of just one.

**Block Scope vs Function Scope**

- Variables declared with `let` and `const` inside `{}` are **block-scoped**.
- They cannot be accessed outside the block.
- `var` is **function-scoped**, not block-scoped.

This means:

- `var` declared inside a block still belongs to the enclosing function or global scope.
- `let` and `const` declared in the global scope are stored in the **script scope**, not on the global object.

**Shadowing**  
Shadowing occurs when a variable declared in an inner scope has the same name as a variable in an outer scope.

In such cases:

- The inner variable **shadows** the outer one inside that block.
- Outside the block, the original variable remains unchanged for let and const in block scope.

**Illegal Shadowing**  
Shadowing must respect scope rules.

For example:

- A `let` variable declared in an outer scope **cannot** be shadowed by a `var` in an inner scope.
- This is called **illegal shadowing** and results in an error.

**Scope Rules Still Apply**  
Blocks follow the same rules of:

- Scope
- Lexical environment
- Scope chain

Arrow functions follow the same scoping rules as regular functions.

**Example**

```js
// Block example
if (true) console.log("Hello world"); // Hello world

if (true) {
  // Compound statement
  let a = 10;
  console.log(a); // 10
}

// Shadowing
var a = 10;
let b = 20;
const c = 30;

{
  var a = 40;
  let b = 50;
  const c = 60;

  console.log(a); // 40
  console.log(b); // 50
  console.log(c); // 60
}

console.log(a); // 40 (var is function/global scoped)
console.log(b); // 20
console.log(c); // 30
```

---

## Closures in JavaScript

**What is a Closure?**  
A function bundled together with its **surrounding state (lexical environment)** forms a closure.

**How Closures Work**  
In JavaScript, every function has access to its **lexical environment** (outer scope).  
Even if a function is returned and executed in a different scope, it still remembers the variables and functions from the scope where it was originally created.

A function along with the reference to its outer scope forms a **closure**.

**Why Closures Are Powerful**  
Closures become more interesting when a function is returned or passed around and executed elsewhere.  
Even then, the function continues to hold references to variables in its lexical environment.

These referenced values are **not garbage collected**, because they may be needed later.

**Common Use Cases of Closures**  
Closures are commonly used in:

- Functions like `once`
- Memoization
- Data hiding and encapsulation
- Asynchronous code (callbacks, timers, promises)

**Examples**

```js
// Basic example
function x() {
  var a = 10;
  function y() {
    console.log(a);
  }
  y();
}
x(); // 10

// Return example
function x() {
  var a = 10;
  function y() {
    console.log(a);
  }
  return y;
}

const z = x();
console.log(z); // function y() {...}
z(); // 10
```

---

## setTimeout + Closures in JavaScript

A common interview question that tricks up a lot of developers. Let's understand why and how to fix it.

**The Problem**

**Question:** Print numbers 1 to 5, where each number appears 1 second after the previous one.

So we want:

- 1 (after 1 second)
- 2 (after 2 seconds)
- 3 (after 3 seconds)
- 4 (after 4 seconds)
- 5 (after 5 seconds)

**First Attempt (This Won't Work!)**

```js
function printNumber() {
  for (var i = 1; i <= 5; i++) {
    setTimeout(() => {
      console.log(i);
    }, i * 1000);
  }
}

printNumber();
```

**What we expect:** 1, 2, 3, 4, 5

**What we actually get:** 6, 6, 6, 6, 6

But, Why is it printing 6 five times?

**Understanding Why This Happens**

Let's break it down:

**Step 1: The loop runs really fast**

- JavaScript doesn't wait for setTimeout to finish
- It just registers the callback and moves on to the next iteration
- So the loop completes almost instantly

**Step 2: Loop finishes, i becomes 6**

- The loop runs from i=1 to i=5
- When i becomes 6, the condition `i <= 5` fails and loop stops
- So now i = 6

**Step 3: Callbacks start executing**

- After 1 second, first callback runs and logs `i`
- But i is now 6 (from step 2)
- After 2 seconds, second callback runs and logs `i`
- Still 6!
- Same thing happens for all callbacks

**The real problem:**

- `var` is function-scoped, not block-scoped
- There's only ONE variable `i` in the entire function
- All 5 callbacks are looking at the same `i`
- By the time they run, that `i` has the value 6

Think of it like this: You write down the address of a house (variable i), not the value inside the house. When you go back to check the house later, someone has changed what's inside to 6.

** Solution 1: Just Use `let` (Easiest Fix)**

```js
function printNumber() {
  for (let i = 1; i <= 5; i++) {
    setTimeout(() => {
      console.log(i);
    }, i * 1000);
  }
}

printNumber();
// Output: 1, 2, 3, 4, 5 ✓
```

**Why does this work?**

`let` is block-scoped. This means:

- Each loop iteration gets its own separate `i`
- It's like having 5 different variables: i1, i2, i3, i4, i5
- Each callback remembers its own `i`

This is the simplest solution. If you're writing new code, just use `let`.

**Solution 2: Using Closures (The Old Way with `var`)**

But what if the interviewer specifically asks you to solve it with `var`?

```js
function printNumber() {
  for (var i = 1; i <= 5; i++) {
    function enclosed(x) {
      setTimeout(() => {
        console.log(x);
      }, x * 1000);
    }
    enclosed(i);
  }
}

printNumber();
// Output: 1, 2, 3, 4, 5 ✓
```

**How does this work?**

- We create a new function `enclosed` that takes a parameter `x`
- Each time we call `enclosed(i)`, we pass the current value of i
- This creates a new scope for each iteration
- Each setTimeout callback now remembers its own `x` value

We can think of it like taking a snapshot of `i` and storing it in `x` before moving to the next iteration.

**Here's what happens:**

- Loop iteration 1: enclosed(1) creates a scope with x=1
- Loop iteration 2: enclosed(2) creates a scope with x=2
- And so on...

Each callback now has its own separate x to look at.

---

## Closures: Examples, Advantages & Disadvantages

Understanding closures through practical examples:

**Example 1: Nested Closures**

```javascript
function outest() {
  var b = 20;

  function outer(c) {
    return function inner() {
      console.log(a, b, c);
    };
  }

  let a = 10;

  return outer;
}

outest()("Hello world")(); // 10 20 Hello world
```

**What's happening here?**

**Key point:** The `inner` function has access to variables from THREE different scopes:

- Its own scope (none in this case)
- The `outer` function's scope (variable `c`)
- The `outest` function's scope (variables `a` and `b`)

This is closure in action - the function remembers where it came from.

**Example 2: Data Hiding & Encapsulation**

This is one of the most practical uses of closures.

```javascript
function Counter() {
  let count = 0;

  this.increment = function () {
    count++;
    console.log(count);
  };

  this.decrement = function () {
    count--;
    console.log(count);
  };
}

let counter1 = new Counter();
counter1.increment(); // 1
counter1.increment(); // 2
counter1.increment(); // 3
counter1.decrement(); // 2

let counter2 = new Counter();
counter2.increment(); // 1
counter2.increment(); // 2
counter2.decrement(); // 1
```

**Why is this useful?**

The `count` variable is private. You can't do this:

```javascript
console.log(counter1.count); // undefined
counter1.count = 100; // doesn't work!
```

The only way to change `count` is through the `increment` and `decrement` methods. This is called **data encapsulation** or **data hiding**.

**Important observations:**

1. Each counter instance has its own separate `count`
2. `counter1` and `counter2` don't interfere with each other
3. The `count` variable is completely protected from outside access
4. Only the methods we provide can modify `count`

This pattern is super useful when you want to protect data from being accidentally changed.

**Advantages of Closures**

Closures are powerful because they let us access variables from outer scopes even when those outer functions have finished executing. Here's where we use them:

**1. Maintaining State in Async Operations**

```javascript
function fetchUserData(userId) {
  const timestamp = Date.now();

  setTimeout(() => {
    console.log(`User ${userId} fetched at ${timestamp}`);
    // closure remembers both userId and timestamp
  }, 1000);
}

fetchUserData(123);
```

**2. Creating Functions Like `once`**

```javascript
function once(func) {
  let ran = false;
  let result;

  return function () {
    if (!ran) {
      result = func.apply(this, arguments);
      ran = true;
    }
    return result;
  };
}

const initialize = once(() => console.log("Initialized!"));
initialize(); // Initialized!
initialize(); // (nothing happens)
```

**3. Data Hiding & Encapsulation**

As we saw in the Counter example - keeping variables private.

**4. Module Pattern**

```javascript
const calculator = (function () {
  let result = 0;

  return {
    add: (x) => (result += x),
    subtract: (x) => (result -= x),
    getResult: () => result,
  };
})();

calculator.add(5);
calculator.add(3);
console.log(calculator.getResult()); // 8
```

**Disadvantages of Closures**

Everything has a cost. Here's what you need to watch out for:

**Memory Issues**

When you create a closure, JavaScript can't clean up (garbage collect) the variables that closure is holding onto. They stay in memory because they might be used later.

**Example of potential memory leak:**

```javascript
function heavyOperation() {
  const bigArray = new Array(1000000).fill("data");

  return function () {
    console.log("I still hold reference to bigArray!");
    // bigArray can't be garbage collected
  };
}

const func = heavyOperation();
// bigArray is stuck in memory even if we never use it
```

**What's garbage collection?**

The garbage collector is like a cleanup crew in JavaScript. It removes variables and functions that are no longer needed to free up memory. But with closures, it can't clean up because those variables might be used later.

**Good News: Modern JavaScript Engines Are Smart**

Modern browsers have smart garbage collectors. They can figure out which variables in a closure are actually being used.

**Example:**

```javascript
function outer() {
  let a = 10;
  let b = 20; // This won't stay in memory!
  let c = 30; // This won't stay in memory either!

  return function inner() {
    console.log(a);
    // Only using 'a', not 'b' or 'c'
  };
}

const myFunc = outer();
myFunc(); // 10
```

**When to Be Careful**

Even though modern engines are smart, you should still be careful when:

1. Creating lots of closures in loops
2. Holding references to large objects or arrays
3. Creating closures that will live for a long time (like event listeners)

---

## First Class Functions in JavaScript

Functions in JavaScript are beautiful and flexible. Let's explore the different ways to declare and use them.

**Function Statement (aka Function Declaration)**

```javascript
function a() {
  console.log("a called");
}

a(); // a called
```

This is the most straightforward way to create a function. You give it a name and define what it does.

**Function Expression**

Function expression is when you use a function as a value and assign it to a variable.

```javascript
var b = function () {
  console.log("b called");
};

b(); // b called
```

**Difference between Function Statement and Function Expression:**

The main difference shows up during hoisting:

```javascript
// Function Statement - This works!
a(); // a called
function a() {
  console.log("a called");
}

// Function Expression - This breaks!
b(); // Error: b is not a function
var b = function () {
  console.log("b called");
};
```

**Why does this happen?**

- Function declarations get fully hoisted - you can call them before they're declared
- Function expressions act like variables - they get `undefined` during hoisting
- So when you try calling `b()` before its line, JavaScript sees `undefined()` which gives an error

**Anonymous Function**

Anonymous functions are functions without a name. They don't have their own identity.

```javascript
function() {
  console.log("Anonymous function called");
}
```

**But wait, if you try this directly, you'll get an error!**

```javascript
function() {
  console.log("Anonymous function called");
}
// SyntaxError: Function statements require a function name
```

This happens because the syntax looks like a function statement without a name. And according to ECMAScript specification, function statements require a name.

**So where do we use anonymous functions?**

We use anonymous functions where we want to use functions as values:

```javascript
// As a callback in setTimeout
setTimeout(function () {
  console.log("This runs after 1 second");
}, 1000);
```

Basically, anywhere you're passing a function as a value, you can use an anonymous function.

**Named Function Expression**

Named function expression is a function expression, but instead of an anonymous function, it's a named function.

```javascript
var c = function xyz() {
  console.log("c called");
};

c(); // c called
```

**Important thing to note:**

The name `xyz` is local to the function and not globally accessible. You can only access it within the function itself.

```javascript
var c = function xyz() {
  console.log("c called");
  console.log(xyz); // This works - accessible inside
};

c(); // c called
xyz(); // Error: xyz is not defined - not accessible outside
```

This is useful for recursion or when you want the function to reference itself:

```javascript
var factorial = function fact(n) {
  if (n <= 1) return 1;
  return n * fact(n - 1); // Can call itself using 'fact'
};

console.log(factorial(5)); // 120
```

**First Class Functions**

The ability to use functions as values is known as **first class functions** (or first class citizens) in JavaScript.

This means you can:

- Use functions as values in variables
- Pass functions as arguments to other functions
- Return functions from other functions

This ability is what makes functions "first class" in JavaScript.

**Example 1: Passing a function as an argument**

```javascript
function outer(param) {
  console.log(param); // logs the function
  param(); // calls the function
}

outer(function () {
  console.log("I'm being passed as an argument!");
});
```

**Example 2: Returning a function from another function**

```javascript
function outer() {
  return function () {
    console.log("I'm being returned!");
  };
}

const returnedFunc = outer();
returnedFunc(); // I'm being returned!
```

**Example 3: Storing functions in variables**

```javascript
var greet = function () {
  console.log("Hello!");
};

var sayHi = greet; // assigning function to another variable
sayHi(); // Hello!
```

**Why is this powerful?**

First class functions enable:

- Callbacks (like in setTimeout, event handlers)
- Higher-order functions (functions that take or return functions)
- Functional programming patterns
- Closures and much more

**Real example combining everything:**

```javascript
function createMultiplier(multiplier) {
  return function (number) {
    return number * multiplier;
  };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(double(5)); // 10
console.log(triple(5)); // 15
```

Here we're:

- Returning a function from `createMultiplier`
- Storing that returned function in variables (`double`, `triple`)
- Using those functions as values

**Arrow Functions**

Arrow functions are a shorter syntax for writing functions, introduced in ES6.

```javascript
var sum = (a, b) => a + b;

console.log(sum(2, 3)); // 5
```

---

## Callback Functions in JS ft. Event Listeners

- As function acts as first class functions javascript means it can be used like a value. It can be assigned to the variables and passed down as a argument to the functions and can be also return from another function. This makes function in js really powerful.

- And with this ability the function we pass to the other function or event listeners known as the callback function. And the function which takes the function as argument is known as higher order function in javascript.

- And with this callback functions we can access the whole async world in synchronous single threaded language.

- The callback functions will be passed to another function and now the responsibility of calling this function is on the other function. And this function will be called sometime else in the program.

- So with callback functions we can do things in async way means so javascript can be register the function and execute sometime else in the code, So we don't block the main thread. And js starts executing the next line of code. And once the condition satisfy the function is bring back to the call stack and then executed quickly.

- So if there is some code which takes sometime so instead of blocking our main thread for that time. We can use callbacks.

**Examples of callbacks**

```js
// Here with power of web apis (setTimeout) and callback function. We can execute the code in async way
setTimeout(() => {
  console.log("Set timeout called");
}, 1000);

console.log("Hello");
console.log("World");

// Hello | world | Set timeout called
```

```js
// Example with event listener

// How this executed is when the code executed the code first register the event listener callback and executes the next lines defined in the code.
//  So the Hello and world will be printed in the console and when user clicks the button the callback function will get in the call stack and gets executed
// With this behavior we don't get blocked and the code can be executed as expected.

document.getElementIdById("btn-click").addEventListener("click", () => {
  console.log("btn clicked");
});

console.log("Hello");
console.log("World");
```

## Async JavaScript and Event Loop

Understanding how JavaScript handles asynchronous operations behind the scenes.

**What is Event Loop?**

Event loop is like a gatekeeper that constantly monitors two things:

1. The callback queue (where async callbacks wait)
2. The call stack (where code executes)

Its job is simple: when the call stack is empty, pick callbacks from the queue and put them in the call stack so they can be executed.

**JavaScript is Synchronous and Single-Threaded**

Let's start with the basics:

JavaScript executes whatever comes into the call stack quickly. It doesn't wait for anything.

**The Problem: What About Timers?**

```javascript
console.log("Start");
// Wait for 2 seconds somehow?
console.log("End");
```

How do we make JavaScript wait? The call stack and JavaScript engine don't have access to timers!

**The answer:** JavaScript gets help from the browser.

**Browser Superpowers (Web APIs)**

Browsers provide superpowers to JavaScript through **Web APIs**:

- `setTimeout` and `setInterval` (timers)
- `fetch` (network requests)
- `console` (logging)
- DOM APIs (document, getElementById, etc.)
- `localStorage` (storage)
- And many more...

The browser attaches these to the global `window` object, so we can access them:

```javascript
window.setTimeout(() => {}, 1000);
window.console.log("Hello");

// Or just use them directly (they're global)
setTimeout(() => {}, 1000);
console.log("Hello");
```

**How Async Operations Work: Step by Step**

Let's walk through an example to understand the complete flow:

```javascript
console.log("Start");

setTimeout(() => {
  console.log("Timer callback");
}, 2000);

console.log("End");
```

**Step 1: Code starts executing**

- `console.log("Start")` goes to call stack → executes → "Start" is printed
- Call stack is now empty

**Step 2: setTimeout is encountered**

- JavaScript sees `setTimeout` (a Web API)
- It passes the callback function to the Web API environment
- The browser starts a 2-second timer
- JavaScript doesn't wait! It moves to the next line immediately

**Step 3: Continue execution**

- `console.log("End")` goes to call stack → executes → "End" is printed
- Call stack is empty
- Main code execution is complete

**Step 4: Timer expires (after 2 seconds)**

- Browser timer completes
- The callback function is pushed to the **callback queue**
- It waits there until the call stack is empty

**Step 5: Event loop does its job**

- Event loop constantly checks: "Is call stack empty?"
- Call stack is empty (main code finished)
- Event loop picks the callback from the queue
- Puts it in the call stack

**Step 6: Callback executes**

- `console.log("Timer callback")` executes → "Timer callback" is printed

**Final Output:**

```
Start
End
Timer callback
```

**Visual Flow**

```
Code Execution:
┌─────────────────────────────────────────────────────────┐
│ 1. console.log("Start") → Call Stack → Execute         │
│ 2. setTimeout → Web API (timer starts)                 │
│ 3. console.log("End") → Call Stack → Execute           │
│ 4. Main code done, Call Stack empty                    │
│ 5. Timer expires → Callback → Callback Queue           │
│ 6. Event Loop → Move callback to Call Stack            │
│ 7. console.log("Timer callback") → Execute             │
└─────────────────────────────────────────────────────────┘
```

**Another Example: fetch**

```javascript
console.log("Start");

fetch("https://api.example.com/data").then((response) =>
  console.log("Got response"),
);

console.log("End");
```

**What happens:**

1. "Start" prints immediately
2. `fetch` is called → request goes to Web API environment
3. "End" prints immediately (JavaScript doesn't wait)
4. When response arrives → callback goes to micro task queue as it is a callback from promises
5. Event loop moves it to call stack when empty
6. "Got response" prints

**Output:**

```
Start
End
Got response
```

**Two Types of Queues**

JavaScript actually has TWO queues for callbacks:

**1. Microtask Queue (High Priority)**

Callbacks from:

- Promises (`.then`, `.catch`, `.finally`)
- Mutation Observer
- `queueMicrotask()`

**2. Callback Queue / Task Queue (Normal Priority)**

Callbacks from:

- `setTimeout`
- `setInterval`
- `setImmediate`
- DOM events (click, scroll, etc.)
- Other async operations

**Important:** Microtask queue has higher priority! Event loop always checks microtask queue first.

**Priority Example**

```javascript
console.log("Start");

setTimeout(() => {
  console.log("setTimeout callback");
}, 0);

Promise.resolve().then(() => {
  console.log("Promise callback");
});

console.log("End");
```

**What's the output?**

```
Start
End
Promise callback
setTimeout callback
```

**Why this order?**

1. "Start" → synchronous, executes immediately
2. `setTimeout` → callback goes to **Callback Queue**
3. Promise → callback goes to **Microtask Queue**
4. "End" → synchronous, executes immediately
5. Call stack empty, event loop checks queues
6. **Microtask Queue has priority** → "Promise callback" executes first
7. Then Callback Queue → "setTimeout callback" executes

**"Starvation of the Callback Queue"** - when microtasks keep creating more microtasks, callbacks in the callback queue never get executed.

**Real-world scenario:**

```javascript
setTimeout(() => {
  console.log("Timeout");
}, 0);

function recursivePromise(count) {
  if (count > 0) {
    Promise.resolve().then(() => {
      console.log(`Promise ${count}`);
      recursivePromise(count - 1);
    });
  }
}

recursivePromise(1000); // Creates 1000 microtasks!
// "Timeout" will only print after ALL 1000 promises complete
```

**Complete Flow Diagram**

```
JavaScript Code
     ↓
Call Stack (executes synchronously)
     ↓
Encounters async operation (setTimeout, fetch, etc.)
     ↓
Web API Environment (browser handles it)
     ↓
Operation completes
     ↓
  ┌─────────────────────────────┐
  │                             │
  ↓                             ↓
Microtask Queue          Callback Queue
(Promises)               (setTimeout, events)
  │                             │
  └──────────┬──────────────────┘
             ↓
       Event Loop
    (checks if call stack empty)
             ↓
       Call Stack
     (callback executes)
```

**Web Apis**

- ![web-apis png](/js-basics-assets/web-apis.png)

**Async SetTimeout example with event loop**

- ![async-settimeout png](/js-basics-assets/async-settimeout.png)

**Async DOM API's example with event loop**

- ![async-dom-eventlistner](/js-basics-assets/async-dom-eventlistner.png)

**Async Promise Event Loop example with event loop**

- ![async-promise-event-loop](/js-basics-assets/async-promise-event-loop.png)

---

## JS Engine Architecture

Understanding how JavaScript code gets executed under the hood.

**What is a JS Engine?**

JS engine is the heart of the JavaScript Runtime Environment (JRE). This is where your entire JavaScript code gets executed.

**Where Can JavaScript Run?**

JavaScript can run in different places nowadays. To run JavaScript code, you need a JRE (JavaScript Runtime Environment). A JRE consists of:

- JS Engine (the core)
- Web APIs
- Callback Queue
- Microtask Queue
- Event Loop
- And more...

**Examples of JRE:**

**Browsers** - Browsers can run JavaScript because they have a JRE built in. Different browsers have different JS engines:

- Chrome uses V8
- Firefox uses SpiderMonkey
- Safari uses JavaScriptCore

**Node.js** - Also has a JRE which allows JavaScript to run on servers. It uses the V8 engine (same as Chrome).

**Hypothetical Example:**

If we wanted to run JavaScript in a water cooler, we would need to create a JRE for it! The Web APIs would be different - maybe something like `getWaterLevel()` or `adjustTemperature()`. But some APIs would be the same, like `console` and `setTimeout` which are present in both browser and Node.js JRE.

This shows that the JS engine can remain the same, but the environment and Web APIs can be different based on where JavaScript is running.

**Three Main Phases of JS Execution**

When the JS engine receives your high-level JavaScript code, it executes it in three main phases:

1. Parsing
2. Compilation
3. Execution

Let's understand each phase in detail.

**Phase 1: Parsing**

In the parsing phase, your JavaScript code gets converted into something the engine can understand.

**Step 1: Tokenization**

First, the code gets broken down into tokens. Think of tokens as the smallest meaningful pieces of code.

Example:

```javascript
let x = 10;
```

Gets broken into tokens:

```
'let', 'x', '=', '10', ';'
```

**Step 2: Syntax Parser & AST**

These tokens are then passed to the Syntax Parser, which checks if your code follows JavaScript's grammar rules and creates an **Abstract Syntax Tree (AST)**.

Think of AST like a tree structure that represents your code:

```javascript
function add(a, b) {
  return a + b;
}
```

This AST is then passed to the next phase.

**Phase 2: Compilation**

Now comes the interesting part - how does the code actually run?

**Two Types of Code Execution:**

**1. Interpreter**

- Runs code line by line
- Translates and executes immediately
- Produces bytecode (low-level code)
- Fast to start but slower execution

```javascript
console.log("Line 1"); // Execute immediately
console.log("Line 2"); // Then this
console.log("Line 3"); // Then this
```

**2. Compiler**

- Reads the entire code first
- Optimizes and compiles it all
- Produces highly optimized machine code
- Slower to start but faster execution

**Comparison:**

```javascript
// Large loop
for (let i = 0; i < 1000000; i++) {
  console.log(i);
}
```

- **Interpreter**: Starts immediately, but slower overall
- **Compiler**: Takes time to compile first, but runs much faster

**Interpreter is fast**, **Compiler is efficient**.

**JIT (Just In Time) Compilation - Best of Both Worlds**

Most modern JS engines (like V8 in Chrome) use **JIT compilation** which combines both interpreter and compiler!

**How JIT Works:**

1. Start with interpreter for quick execution
2. While running, identify "hot" code (code that runs frequently)
3. Send hot code to compiler for optimization
4. Replace interpreted code with optimized compiled code

```javascript
// This function gets called 10,000 times
function calculate(x) {
  return x * 2 + 5;
}

// First few calls: Interpreter handles it
// After detecting it's "hot": Compiler optimizes it
// Future calls: Use optimized version
```

**Popular Optimization Techniques:**

1. **Inlining** - Replace function calls with actual function code

```javascript
// Before optimization
function double(x) {
  return x * 2;
}
let result = double(5);

// After inlining
let result = 5 * 2; // Direct calculation
```

2. **Copy Elision** - Avoid unnecessary copying of data

3. **Inline Caching** - Remember property lookup results

```javascript
// First time: Look up obj.name
// Next times: Use cached location
obj.name;
```

**What Happens in This Phase:**

The JS engine takes the AST and:

1. Starts interpreting the code line by line
2. Works with the compiler to identify hot code
3. Compiles frequently used parts
4. Produces optimized bytecode

**Phase 3: Execution**

Now the bytecode is ready to run!

The JS engine executes the bytecode using three main components:

**1. Call Stack**

- Keeps track of function calls
- Manages execution context
- Works in LIFO (Last In First Out) manner

**2. Memory Heap**

- Stores variables and objects
- Unstructured memory storage
- Where all your data lives

**3. Garbage Collector**

- Automatically frees up unused memory
- Removes variables/objects that are no longer needed
- Prevents memory leaks

```javascript
function createUser() {
  let user = { name: "John" }; // Created in heap
  return user.name;
} // After function ends, 'user' object is garbage collected

let result = createUser();
```

**Complete Flow Summary**

```
Your JavaScript Code
       ↓
┌──────────────────┐
│   1. PARSING     │
├──────────────────┤
│ • Tokenization   │
│ • Syntax Parser  │
│ • Create AST     │
└────────┬─────────┘
         ↓
┌──────────────────┐
│  2. COMPILATION  │
├──────────────────┤
│ • JIT Compiler   │
│ • Interpreter +  │
│   Compiler       │
│ • Optimization   │
│ • Bytecode       │
└────────┬─────────┘
         ↓
┌──────────────────┐
│  3. EXECUTION    │
├──────────────────┤
│ • Call Stack     │
│ • Memory Heap    │
│ • Garbage        │
│   Collector      │
└──────────────────┘
         ↓
    Output/Result
```

**Generic JS Engine Architecture**

- ![generic-js-engine](/js-basics-assets/generic-js-engine.png)

**Google V8 Engine Architecture**

- ![v8-js-engine](/js-basics-assets/v8-js-engine.png)

## Understanding setTimeout and Async Timing Issues

Async programming in JavaScript can be confusing at first because of how JavaScript's concurrency model works and how it executes synchronous and asynchronous code differently.

The most common confusion happens when people expect async operations to work like they do in other languages. Let's understand why things don't always work as expected.

**The setTimeout Guarantee Problem**

One of the most common misconceptions about `setTimeout`:

```javascript
setTimeout(() => {
  console.log("This runs after 5 seconds... right?");
}, 5000);
```

**Important:** `setTimeout` with 5000 milliseconds doesn't GUARANTEE that it will run exactly after 5 seconds!

**Why not?**

Let's break down what actually happens when you use `setTimeout`:

**Step 1:** JavaScript encounters `setTimeout`

- The callback function is registered in the Web API environment
- A timer starts counting (5000ms in this case)
- JavaScript immediately moves to the next line (doesn't wait)

**Step 2:** Timer completes after 5 seconds

- The callback is pushed to the callback queue
- It waits there

**Step 3:** Event loop checks

- Event loop asks: "Is the call stack empty?"
- **If YES** → callback moves to call stack and executes
- **If NO** → callback has to wait in the queue

**The problem:** If the call stack is busy executing something else, the callback has to wait even if 5 seconds have already passed!

**setTimeout is a MINIMUM delay, not an exact delay.**

**Example 1: Blocking Code Delays setTimeout**

```javascript
console.log("Start");

setTimeout(() => {
  console.log("setTimeout called");
}, 5000);

const startDate = new Date().getTime();
let endDate = startDate;

// This loop blocks for 10 seconds!
while (endDate < startDate + 10000) {
  endDate = new Date().getTime();
}

console.log("While loop finished");

// Output:
// Start (immediately)
// While loop finished (after 10 seconds)
// setTimeout called (after 10 seconds, not 5!)
```

**Example 2: setTimeout with 0 Milliseconds**

This is another tricky one:

```javascript
console.log("Hello");

setTimeout(() => {
  console.log("setTimeout called");
}, 0);

console.log("World");

// Output:
// Hello
// World
// setTimeout called
```

**Important:** Even `setTimeout(fn, 0)` is asynchronous! It doesn't execute immediately in line. It goes through the whole async process.

**Key Takeaways**

- we should avoid blocking the call stack. And if there is something which can take time then we should do that task in async way. So the thread is not blocked and all the code can get to execute.

---

## Higher Order Functions

Understanding one of JavaScript's most powerful features for writing clean, reusable code.

**What are Higher Order Functions?**

Higher order functions are functions that either:

1. Take another function as a parameter, OR
2. Return a function from itself

Simple examples you already know:

- `map()`
- `filter()`
- `reduce()`
- `setTimeout()`
- `addEventListener()`

All of these take a function as a parameter!

**What is a Callback Function?**

The function that you pass as a parameter to a higher order function is called a **callback function**.

```javascript
function greet(name, callback) {
  console.log("Hello " + name);
  callback(); // This is the callback function being executed
}

greet("John", function () {
  console.log("Callback executed!");
});
```

The callback function will be executed somewhere else in the program (not immediately where it's defined).

**Why are Higher Order Functions Useful?**

They allow us to write:

- More modular code
- Reusable code
- Cleaner code
- Less repetitive code

This is the foundation of **functional programming**.

**What is Functional Programming?**

Functional programming means thinking from the function point of view. The key principles are:

1. Write modular code (small, focused functions)
2. Write reusable code (functions that can be used in different contexts)
3. Don't repeat yourself (DRY principle)
4. Use pure functions when possible

**Example: The Problem with Repetitive Code**

Let's say we have an array of radius values and we want to calculate different things:

```javascript
const radius = [3, 1, 4, 10];
```

**Approach 1: Writing separate functions (repetitive)**

```javascript
function calculateArea(radius) {
  const output = [];

  for (let i = 0; i < radius.length; i++) {
    output.push(Math.PI * radius[i] * radius[i]);
  }

  return output;
}

console.log(calculateArea(radius));

function calculateCircumference(radius) {
  const output = [];

  for (let i = 0; i < radius.length; i++) {
    output.push(2 * Math.PI * radius[i]);
  }

  return output;
}

console.log(calculateCircumference(radius));

function calculateDiameter(radius) {
  const output = [];

  for (let i = 0; i < radius.length; i++) {
    output.push(2 * radius[i]);
  }

  return output;
}

console.log(calculateDiameter(radius));
```

**What's wrong with this code?**

Look closely at all three functions. Notice the pattern?

```javascript
// Same in all three functions:
const output = []; // ✓ Creating array
for (let i = 0; i < radius.length; i++) {
  // ✓ Looping
  output.push(/* LOGIC */); // ✓ Pushing to array
}
return output; // ✓ Returning array
```

The only thing that changes is the LOGIC part:

- Area: `Math.PI * radius[i] * radius[i]`
- Circumference: `2 * Math.PI * radius[i]`
- Diameter: `2 * radius[i]`

We're repeating ourselves a lot! The structure is the same, only the calculation logic is different.

**Approach 2: Using Functional Programming (better)**

Let's separate the "what to do" (logic) from the "how to do it" (iteration):

**Step 1: Extract the logic into separate functions**

```javascript
function area(radius) {
  return Math.PI * radius * radius;
}

function circumference(radius) {
  return 2 * Math.PI * radius;
}

function diameter(radius) {
  return 2 * radius;
}
```

These functions are simple and focused. Each does ONE thing.

**Step 2: Create a reusable calculate function**

```javascript
function calculate(radiusArray, logic) {
  const output = [];

  for (let i = 0; i < radiusArray.length; i++) {
    output.push(logic(radiusArray[i]));
  }

  return output;
}
```

This function handles the iteration and array building. It doesn't care about WHAT calculation you do, it just applies whatever function (logic) you give it.

**Step 3: Use it!**

```javascript
const radius = [3, 1, 4, 10];

console.log(calculate(radius, area));
// [28.27, 3.14, 50.26, 314.15]

console.log(calculate(radius, circumference));
// [18.84, 6.28, 25.13, 62.83]

console.log(calculate(radius, diameter));
// [6, 2, 8, 20]
```

**Benefits:**

1. **Less code** - We wrote the loop logic once
2. **More reusable** - `calculate` can work with ANY logic function
3. **More readable** - Clear separation of concerns
4. **Easy to test** - Each function is small and focused

**Making it Even Better: Array.prototype**

Notice how our `calculate` function is similar to `map`? Let's make it work exactly like `map`:

```javascript
Array.prototype.calculate = function (logic) {
  const output = [];

  for (let i = 0; i < this.length; i++) {
    output.push(logic(this[i]));
  }

  return output;
};
```

Now we can use it just like `map`:

```javascript
const radius = [3, 1, 4, 10];

console.log(radius.map(area));
// [28.27, 3.14, 50.26, 314.15]

console.log(radius.calculate(area));
// [28.27, 3.14, 50.26, 314.15]
```

**More Examples of Higher Order Functions**

**Example 1: Function returning a function**

```javascript
function multiplyBy(factor) {
  return function (number) {
    return number * factor;
  };
}

const double = multiplyBy(2);
const triple = multiplyBy(3);

console.log(double(5)); // 10
console.log(triple(5)); // 15
```

`multiplyBy` is a higher order function because it returns a function.

**Example 2: Custom filter function like implementation**

```javascript
function customFilter(array, testFunction) {
  const result = [];

  for (let i = 0; i < array.length; i++) {
    if (testFunction(array[i])) {
      result.push(array[i]);
    }
  }

  return result;
}

const numbers = [1, 2, 3, 4, 5, 6];

const evenNumbers = customFilter(numbers, function (num) {
  return num % 2 === 0;
});

console.log(evenNumbers); // [2, 4, 6]
```

**Example 3: Custom forEach**

```javascript
function customForEach(array, callback) {
  for (let i = 0; i < array.length; i++) {
    callback(array[i], i, array);
  }
}

const fruits = ["apple", "banana", "orange"];

customForEach(fruits, function (fruit, index) {
  console.log(`${index}: ${fruit}`);
});
// 0: apple
// 1: banana
// 2: orange
```

---

## Map, Filter and Reduce

Understanding the three most powerful array methods in JavaScript.

**What are Map, Filter, and Reduce?**

Map, filter, and reduce are higher order functions in JavaScript that are used for array transformation. They help you loop through arrays and transform them based on the logic you provide in a callback function.

Instead of writing traditional for loops every time, these functions give you a cleaner, more readable way to work with arrays.

**Map Function**

Map is used when you want to transform each element in an array and get a new array back.

**What it does:**

- Loops through each element in the array
- Applies the transformation logic from your callback function
- Returns a NEW transformed array
- Original array stays unchanged

**Syntax:**

```javascript
array.map((element) => {
  // return transformed element
});
```

**Examples:**

```javascript
let array = [1, 2, 3, 6];

// Double each number
let double = array.map((item) => item * 2);
console.log(double); // [2, 4, 6, 12]

// Triple each number
let triple = array.map((item) => item * 3);
console.log(triple); // [3, 6, 9, 18]

console.log(array); // [1, 2, 3, 6] - original unchanged
```

**Real-world example with objects:**

```javascript
let users = [
  { name: "sachin", age: 29, place: "mumbai" },
  { name: "virat", age: 21, place: "delhi" },
  { name: "dhoni", age: 27, place: "rachi" },
];

// Get array of user names with their places
let userNames = users.map((user) => user.name + " from " + user.place);
console.log(userNames);
// ["sachin from mumbai", "virat from delhi", "dhoni from rachi"]

// Get array of just ages
let ages = users.map((user) => user.age);
console.log(ages); // [29, 21, 27]
```

**When to use map:**

- When you need to transform every element
- When you need the same number of elements in output as input
- When you want to extract specific properties from objects

**Filter Function**

Filter is used when you want to select only certain elements from an array based on a condition.

**What it does:**

- Loops through each element in the array
- Tests each element with your condition (callback function)
- If condition returns `true`, element is included in new array
- If condition returns `false`, element is skipped
- Returns a NEW filtered array

**Syntax:**

```javascript
array.filter((element) => {
  // return true to keep, false to remove
});
```

**Examples:**

```javascript
let array = [1, 2, 3, 6];

// Get only even numbers
let evenNumbers = array.filter((item) => item % 2 === 0);
console.log(evenNumbers); // [2, 6]

// Get numbers greater than 2
let greaterThanTwo = array.filter((item) => item > 2);
console.log(greaterThanTwo); // [3, 6]
```

**Real-world example with objects:**

```javascript
let users = [
  { name: "sachin", age: 29, place: "mumbai" },
  { name: "virat", age: 21, place: "delhi" },
  { name: "dhoni", age: 27, place: "rachi" },
];

// Get users older than 21
let filteredUsers = users.filter((user) => user.age > 21);
console.log(filteredUsers);
// [
//   { name: "sachin", age: 29, place: "mumbai" },
//   { name: "dhoni", age: 27, place: "rachi" }
// ]

// Get users from rachi
let filteredUsersByPlace = users.filter((user) => user.place === "rachi");
console.log(filteredUsersByPlace);
// [{ name: "dhoni", age: 27, place: "rachi" }]

// Get users whose name starts with 's'
let usersStartingWithS = users.filter((user) => user.name.startsWith("s"));
console.log(usersStartingWithS);
// [{ name: "sachin", age: 29, place: "mumbai" }]
```

**When to use filter:**

- When you need to select elements based on a condition
- When output array might have fewer elements than input
- When you want to remove unwanted elements

**Reduce Function**

Reduce is the most powerful and flexible of the three. It's used when you want to reduce an array to a single value.

**What it does:**

- Loops through each element in the array
- Maintains an accumulator (the result you're building)
- Updates the accumulator based on your logic
- Returns a SINGLE value (can be number, string, object, or even array)

**Syntax:**

```javascript
array.reduce((accumulator, currentElement) => {
  // update and return accumulator
}, initialValue);
```

**Important parameters:**

- `accumulator` (acc): The result you're building up
- `currentElement` (curr): The current array element being processed
- `initialValue`: Starting value for the accumulator

**Example 1: Sum of numbers**

```javascript
let array = [1, 2, 3, 6];

let sum = array.reduce((acc, curr) => {
  acc += curr;
  return acc;
}, 0);

console.log(sum); // 12
```

**How it works step by step:**

```
Initial: acc = 0 (the initial value we provided)

Step 1: curr = 1, acc = 0 + 1 = 1
Step 2: curr = 2, acc = 1 + 2 = 3
Step 3: curr = 3, acc = 3 + 3 = 6
Step 4: curr = 6, acc = 6 + 6 = 12

Final result: 12
```

**Shorter version:**

```javascript
let sum = array.reduce((acc, curr) => acc + curr, 0);
```

**Example 2: Find maximum number**

```javascript
let array = [1, 2, 3, 6];

let max = array.reduce((acc, curr) => {
  if (curr > acc) {
    return curr;
  }
  return acc;
}, array[0]);

console.log(max); // 6
```

**Example 3: Transform array to object**

```javascript
let users = [
  { name: "sachin", age: 29, place: "mumbai" },
  { name: "virat", age: 21, place: "delhi" },
  { name: "dhoni", age: 27, place: "rachi" },
];

// Group users by place
let usersByPlace = users.reduce((acc, curr) => {
  acc[curr.place] = curr;
  return acc;
}, {});

console.log(usersByPlace);
// {
//   mumbai: { name: 'sachin', age: 29, place: 'mumbai' },
//   delhi: { name: 'virat', age: 21, place: 'delhi' },
//   rachi: { name: 'dhoni', age: 27, place: 'rachi' }
// }
```

**How this works:**

```
Initial: acc = {} (empty object)

Step 1: curr = {name: "sachin", ...}
  acc["mumbai"] = {name: "sachin", ...}
  acc = { mumbai: {...} }

Step 2: curr = {name: "virat", ...}
  acc["delhi"] = {name: "virat", ...}
  acc = { mumbai: {...}, delhi: {...} }

Step 3: curr = {name: "dhoni", ...}
  acc["rachi"] = {name: "dhoni", ...}
  acc = { mumbai: {...}, delhi: {...}, rachi: {...} }

Final result: object with all three users grouped by place
```

**Example 4: Count occurrences**

```javascript
let fruits = ["apple", "banana", "apple", "orange", "banana", "apple"];

let count = fruits.reduce((acc, curr) => {
  if (acc[curr]) {
    acc[curr]++;
  } else {
    acc[curr] = 1;
  }
  return acc;
}, {});

console.log(count);
// { apple: 3, banana: 2, orange: 1 }
```

**When to use reduce:**

- When you need a single value from an array
- When you're calculating a sum, average, max, min
- When you're transforming an array into an object
- When you're flattening nested arrays
- When you're grouping or counting data

**Combining Map, Filter, and Reduce**

The real power comes when you chain these methods together!

```javascript
let users = [
  { name: "sachin", age: 29, place: "mumbai" },
  { name: "virat", age: 21, place: "delhi" },
  { name: "dhoni", age: 27, place: "rachi" },
  { name: "rohit", age: 19, place: "mumbai" },
];

// Get total age of users older than 20
let totalAge = users
  .filter((user) => user.age > 20) // Keep only age > 20
  .map((user) => user.age) // Extract just the ages
  .reduce((acc, age) => acc + age, 0); // Sum them up

console.log(totalAge); // 77 (29 + 21 + 27)
```

**Step by step:**

```
Step 1 (filter): Get users with age > 20
  Result: [
    { name: "sachin", age: 29, place: "mumbai" },
    { name: "virat", age: 21, place: "delhi" },
    { name: "dhoni", age: 27, place: "rachi" }
  ]

Step 2 (map): Extract just ages
  Result: [29, 21, 27]

Step 3 (reduce): Sum all ages
  Result: 77
```

---

## Callbacks and Callback Hell

Understanding the foundation of async JavaScript and its problems with callbacks.

**What are Callbacks?**

Callbacks are the most important thing in JavaScript when it comes to async programming. In fact, async programming in JavaScript exists because of callback functions.

**Why do we need callbacks?**

Remember, JavaScript is a synchronous single-threaded language. It can do one task at a time in a particular order. Whatever you give to JavaScript, it executes immediately.

But what if we need to wait for something? What if we want to execute a piece of code later, not right now?

This is where callbacks help us!

**Simple Callback Example**

```javascript
console.log("Hello world");

setTimeout(() => {
  console.log("callback called");
}, 3000);

console.log("End of the code");

// Output:
// Hello world
// End of the code
// callback called (after 3 seconds)
```

**Real-World Example: API Calls**

Let's say you're building an e-commerce site. When a user clicks "Buy Now", you need to:

1. Create an order
2. Process payment
3. Show order summary
4. Update wallet balance

Each step depends on the previous one completing. Here's how you might write it with callbacks:

```javascript
let cart = ["shirt", "pant", "kurta"];

api.createOrder(cart, function () {
  api.proceedToPayment(function () {
    api.orderSummary(function () {
      api.updateWalletBalance();
    });
  });
});
```

This works, but notice how the code keeps going deeper and deeper? This leads to two major problems.

**Problem 1: Callback Hell**

Callback hell happens when you have multiple callbacks nested inside each other. The code starts to grow horizontally instead of vertically, making it extremely hard to read and maintain.

**Example of Callback Hell:**

```javascript
let cart = ["shirt", "pant", "kurta"];

api.createOrder(cart, function (orderId) {
  api.proceedToPayment(orderId, function (paymentInfo) {
    api.orderSummary(paymentInfo, function (summary) {
      api.updateWalletBalance(summary, function (balance) {
        console.log("Order completed! New balance: " + balance);
      });
    });
  });
});
```

See how it keeps going deeper? This is called the **"Pyramid of Doom"** or **"Callback Hell"**.

**Even worse with conditions:**

This is a nightmare to:

- Read
- Understand
- Debug
- Maintain
- Modify

**Why is Callback Hell bad?**

1. **Hard to read** - Code grows horizontally, not vertically
2. **Hard to maintain** - Making changes becomes risky
3. **Hard to debug** - Finding errors is difficult
4. **Hard to understand flow** - Logic is buried in nested functions
5. **Error handling is messy** - Need to handle errors at each level

**Problem 2: Inversion of Control**

This is an even bigger problem than callback hell!

**What is Inversion of Control?**

When you pass your callback function to another function, you're giving away control of your code.

```javascript
api.createOrder(cart, function () {
  // This is YOUR code
  // But YOU don't control when it runs
  // api.createOrder controls it!
});
```

You're trusting that `api.createOrder` will:

- Call your callback exactly once
- Call it at the right time
- Pass the correct data
- Not call it if there's an error

But what if the API has bugs?

**What could go wrong:**

**Issue 1: Callback never called**

```javascript
api.createOrder(cart, function () {
  console.log("This might never run!");
});
// API has a bug and never calls the callback
// Your code just waits forever
```

**Issue 2: Callback called multiple times**

```javascript
api.proceedToPayment(orderId, function (paymentInfo) {
  chargeCustomer(paymentInfo.amount);
  // What if this API calls the callback twice?
  // Customer gets charged twice!
});
```

**Issue 3: Callback called too early**

```javascript
api.fetchUserData(userId, function (userData) {
  // API calls this before data is ready
  // userData is undefined or incomplete
});
```

**Issue 4: Callback called with wrong data**

```javascript
api.getOrderDetails(orderId, function (orderDetails) {
  // API passes null or incorrect data
  // Your code breaks
});
```

**Real-world disaster scenario:**

```javascript
let cart = ["iPhone", "MacBook"];

api.createOrder(cart, function (orderId) {
  // What if createOrder calls this twice?
  api.proceedToPayment(orderId, function (paymentInfo) {
    // Payment happens twice!
    // Customer charged $3000 instead of $1500

    api.sendConfirmationEmail(paymentInfo, function () {
      // Customer gets two emails
    });
  });
});
```

You have no control over:

- Whether the callback is called
- How many times it's called
- When it's called
- What data is passed to it

This is **Inversion of Control** - you've inverted (given away) the control of your code execution to someone else's code.

You wrote good code, but the API you're using has a bug. Your users get duplicate emails, and you have no way to prevent it without changing the API itself.

## Promises

A Promise is a JavaScript object that represents the eventual completion or failure of an asynchronous operation.

**Promise Object Structure**

A Promise is a special object in JavaScript that has two main properties:

1. **PromiseState** - The current status of the promise
2. **PromiseResult** - The data or error from the async operation

**When a Promise is created:**

```javascript
const promise = fetch("https://api.example.com/data");

// Initial state:
// PromiseState: "pending"
// PromiseResult: undefined
```

**When the async operation completes successfully:**

```javascript
// After successful completion:
// PromiseState: "fulfilled"
// PromiseResult: {the data returned}
```

**When the async operation fails:**

```javascript
// After failure:
// PromiseState: "rejected"
// PromiseResult: {error object}
```

**The Three States of a Promise**

```
                    ┌──────────┐
                    │ PENDING  │ ← Initial state
                    └─────┬────┘
                          │
                ┌─────────┴──────────┐
                │                    │
           ┌────▼────┐          ┌───▼────┐
           │FULFILLED│          │REJECTED│
           └─────────┘          └────────┘
         (success)              (failure)
```

**Using Promises**

You can attach callback functions to a promise using `.then()` for success and `.catch()` for errors:

```javascript
const promise = fetch("https://api.example.com/data");

promise
  .then((data) => {
    // This runs when promise is fulfilled
    console.log("Success!", data);
  })
  .catch((error) => {
    // This runs when promise is rejected
    console.log("Error!", error);
  });
```

The callback attached to `.then()` or `.catch()` will be executed automatically once the promise state becomes 'fulfilled' or 'rejected'.

**Important:** The callback is called automatically by JavaScript when the promise resolves - you don't control when it runs, but you're guaranteed it will run by javascript.

**Advantages of Promises**

Promises help us solve the two main problems we faced when handling async operations with just callback functions:

1. Callback Hell
2. Inversion of Control

Let's understand how promises solve each problem.

**Advantage 1: Solving Inversion of Control**

Remember the problem with callbacks? When we pass our callback function to some API, we lose control:

```javascript
// With callbacks - WE LOST CONTROL
api.createOrder(cart, function (orderId) {
  // This is OUR code
  // But the API controls when/if it runs
  // What if API never calls this?
  // What if it calls it twice?
});
```

We're trusting that the API will:

- Call our callback
- Call it only once
- Call it with correct data

But we have no guarantees!

**How Promises solve this:**

```javascript
// With promises - WE HAVE CONTROL AS THE API'S ONLY JOB IS TO RETURN THE PROMISE
const promise = api.createOrder(cart);

promise.then((orderId) => {
  // JavaScript GUARANTEES:
  // 1. This will be called definitely when data arrives
  // 2. This will be called ONLY ONCE
  // 3. Promise object is immutable
});
```

**Advantage 2: Solving Callback Hell with Promise Chaining**

Remember callback hell? The pyramid of doom?

**With Callbacks (Callback Hell):**

```javascript
let cart = ["shirt", "pants", "kurta"];

api.createOrder(cart, function (orderId) {
  api.proceedToPayment(orderId, function (paymentInfo) {
    api.orderSummary(paymentInfo, function (summary) {
      api.updateWalletBalance(summary, function () {
        console.log("Order complete!");
      });
    });
  });
});
```

Code grows horizontally → hard to read and maintain.

**With Promises (Promise Chaining):**

```javascript
let cart = ["shirt", "pants", "kurta"];

api
  .createOrder(cart)
  .then((orderId) => api.proceedToPayment(orderId))
  .then((paymentInfo) => api.orderSummary(paymentInfo))
  .then((summary) => api.updateWalletBalance(summary))
  .then(() => console.log("Order complete!"));
```

Code grows vertically → much easier to read!

**How Promise Chaining Works**

Each `.then()` can return a new promise, which allows you to chain them:

```javascript
api
  .createOrder(cart) // Returns Promise<orderId>
  .then((orderId) => {
    console.log("Order created:", orderId);
    return api.proceedToPayment(orderId); // Returns Promise<paymentInfo>
  })
  .then((paymentInfo) => {
    console.log("Payment done:", paymentInfo);
    return api.orderSummary(paymentInfo); // Returns Promise<summary>
  })
  .then((summary) => {
    console.log("Summary:", summary);
    return api.updateWalletBalance(summary); // Returns Promise<balance>
  })
  .then((balance) => {
    console.log("New balance:", balance);
  });
```

**Flow of Promise Chain:**

```
Step 1: createOrder runs
   ↓
Returns promise with orderId
   ↓
Step 2: First .then() receives orderId
   ↓
Calls proceedToPayment
   ↓
Returns promise with paymentInfo
   ↓
Step 3: Second .then() receives paymentInfo
   ↓
Calls orderSummary
   ↓
Returns promise with summary
   ↓
Step 4: Third .then() receives summary
   ↓
Calls updateWalletBalance
   ↓
Done!
```

**Advantage 3: Promise Immutability**

Once a promise is resolved (fulfilled or rejected), its value cannot be changed:

```javascript
const promise = api.getData();

promise.then((data) => {
  console.log(data); // "Hello"
});

// Later, somewhere else in code
promise.then((data) => {
  console.log(data); // Still "Hello" - same value!
});

// You cannot modify the promise result
// It's safe to pass around
```

This means you can:

- Pass promises to different parts of your code
- Attach multiple `.then()` handlers
- Be confident the value won't change

---

**Key differences/Summary:**

1. **We're not passing our code to the API** - We're attaching our callback to the promise object that the API returns

2. **JavaScript gives us guarantees:**
   - Callback will be called when promise resolves
   - Callback will be called exactly once
   - Promise state can only change once (pending → fulfilled or pending → rejected)

3. **Promise object is immutable** - Once a promise is resolved, its value cannot be changed. You can pass it around safely.

```javascript
const orderPromise = api.createOrder(cart);

// You can pass this promise around
handleOrder(orderPromise);
logOrder(orderPromise);
trackOrder(orderPromise);

// No one can change the promise result. orderResponse.data = "something" is not allowed
// Everyone gets the same data when promise resolves
```

## Promise Chaining and Creating Promises

Understanding how to create your own promises and chain them together.

**Real-World Example: E-commerce Order Flow**

Let's build a complete order processing system with promises. When a user places an order, we need to:

1. Create the order
2. Process payment
3. Generate order summary
4. Update wallet balance

Each step depends on the previous one, so we'll use promise chaining.

Now let's understand each part step by step.

**Creating a Promise**

To create a promise, use the `new Promise()` constructor:

```javascript
const myPromise = new Promise((resolve, reject) => {
  // Your async code here
});
```

The Promise constructor takes a function with two parameters:

- `resolve` - Call this when operation succeeds
- `reject` - Call this when operation fails

```javascript
const cart = ["kurta", "pants", "shoes"];
let walletBalance = 500;
```

**Example 1: Creating the Order**

```javascript
function createOrder() {
  return new Promise((resolve, reject) => {
    // Step 1: Validate the cart
    if (!validateCart(cart)) {
      const error = new Error("Cart is not valid");
      reject(error); // Reject if cart is invalid
      return;
    }

    // Step 2: Create order ID
    let orderId = "12345";

    // Step 3: Simulate async operation (like API call)
    setTimeout(() => {
      resolve(orderId); // Resolve with order ID after 3 seconds
    }, 3000);
  });
}

function validateCart(cart) {
  if (!cart?.length) return false;
  return true;
}
```

**Understanding resolve and reject:**

```javascript
new Promise((resolve, reject) => {
  // If everything is good:
  resolve(data); // Promise becomes "fulfilled"

  // If something goes wrong:
  reject(error); // Promise becomes "rejected"
});
```

**Example 2: Processing Payment**

```javascript
function proceedToPayment(orderId) {
  return new Promise((resolve, reject) => {
    // Validate order ID
    if (!orderId) {
      const error = new Error("Order ID is not valid");
      reject(error);
      return;
    }

    // Process payment
    let paymentInfo = {
      paymentStatus: "success",
      paymentAmount: 100,
    };

    // Simulate payment processing (2 seconds)
    setTimeout(() => {
      resolve(paymentInfo);
    }, 2000);
  });
}
```

**Example 3: Generating Order Summary**

```javascript
function orderSummary(paymentInfo) {
  return new Promise((resolve, reject) => {
    // Check if payment was successful
    if (paymentInfo?.paymentStatus !== "success") {
      const error = new Error("Invalid payment status");
      reject(error);
      return;
    }

    // Create summary
    let summary = { cart, paymentInfo };

    // Simulate summary generation (3 seconds)
    setTimeout(() => {
      resolve(summary);
    }, 3000);
  });
}
```

**Example 4: Updating Wallet Balance**

```javascript
function updateWalletBalance(summary) {
  return new Promise((resolve, reject) => {
    // Validate summary data
    if (!summary?.cart || !summary?.paymentInfo) {
      const error = new Error("Invalid data");
      reject(error);
      return;
    }

    // Calculate new balance
    let remainingBalance = walletBalance - summary?.paymentInfo?.paymentAmount;

    // Simulate wallet update (1 second)
    setTimeout(() => {
      resolve(remainingBalance);
    }, 1000);
  });
}
```

**Understanding the Promise Chain**

Now let's trace through the entire flow:

```javascript
createOrder() // Step 1: Start here
  .then((orderId) => {
    // Step 2: Receives orderId
    console.log("Order ID:", orderId); // Logs: "12345"
    return orderId; // Pass to next .then()
  })
  .then((orderId) => {
    // Step 3: Receives orderId
    return proceedToPayment(orderId); // Returns a promise
  })
  .then((paymentInfo) => {
    // Step 4: Receives paymentInfo
    console.log("Payment Info:", paymentInfo);
    return paymentInfo; // Pass to next .then()
  })
  .then((paymentInfo) => {
    // Step 5: Receives paymentInfo
    return orderSummary(paymentInfo); // Returns a promise
  })
  .then((summary) => {
    // Step 6: Receives summary
    console.log("Order Summary:", summary);
    return summary; // Pass to next .then()
  })
  .then((summary) => {
    // Step 7: Receives summary
    return updateWalletBalance(summary); // Returns a promise
  })
  .then((remainingBalance) => {
    // Step 8: Receives balance
    console.log("Remaining Balance:", remainingBalance);
  })
  .catch((error) => {
    // Catches ANY error above
    console.error("Error:", error?.message);
  });
```

**Important Rule: Always Return**

In promise chains, you need to return values to pass them to the next `.then()`:

```javascript
// ✓ Correct - returning the value
.then((orderId) => {
  return proceedToPayment(orderId);
})

// ✗ Wrong - not returning
.then((orderId) => {
  proceedToPayment(orderId);  // Next .then() gets undefined!
})
```

**Error Handling in Promise Chains**

What happens if the cart is empty?

```javascript
const cart = []; // Empty cart!

createOrder()
  .then((orderId) => {
    console.log("Order ID:", orderId); // Never runs
    return orderId;
  })
  .then((orderId) => {
    return proceedToPayment(orderId); // Never runs
  })
  // ... all other .then() are skipped
  .catch((error) => {
    console.error("Error:", error?.message); // Runs here!
    // Logs: "Error: Cart is not valid"
  });
```

**Important:** When any promise rejects, it skips all `.then()` blocks and jumps directly to `.catch()`! And .catch covers all the .then above it.

**Visual Flow with Error:**

```
createOrder()
   ↓
Cart invalid!
   ↓
reject(error)
   ↓
Skip all .then()
   ↓
.catch() receives error
   ↓
Log error message
```

**Handling Errors at Different Levels**

You can have multiple `.catch()` blocks:

```javascript
createOrder()
  .then((orderId) => proceedToPayment(orderId))
  .catch((error) => {
    console.log("Order creation failed:", error.message);
    throw error; // Re-throw to continue error chain
  })
  .then((paymentInfo) => orderSummary(paymentInfo))
  .catch((error) => {
    console.log("Payment failed:", error.message);
    throw error;
  })
  .then((summary) => updateWalletBalance(summary))
  .catch((error) => {
    console.log("Final error handler:", error.message);
  });
```

**Key Points About Promise Chains**

**1. Each .then() returns a new promise:**

```javascript
const promise1 = createOrder();           // Promise
const promise2 = promise1.then(...);      // New Promise
const promise3 = promise2.then(...);      // Another new Promise
```

**2. Data flows down the chain:**

```javascript
createOrder() // Returns orderId
  .then((orderId) => {
    // Receives orderId
    return "modified"; // Returns "modified"
  })
  .then((data) => {
    // Receives "modified", not orderId
    console.log(data); // "modified"
  });
```

**3. Errors propagate down until caught:**

```javascript
step1()
  .then(step2)
  .then(step3) // Error happens here
  .then(step4) // Skipped
  .then(step5) // Skipped
  .catch(handleError); // Catches error from step3
```

**Best Practices**

1. **Always return** in `.then()` if you need the value in next step
2. **Add `.catch()`** at the end to handle errors
3. **Keep chains readable** - one operation per `.then()`
4. **Validate inputs** before doing async operations
5. **Create descriptive error messages**

## Async/Await in JavaScript

Async/await is a modern way to handle promises in JavaScript. It makes async code easier to read and understand.

**The `async` Keyword**

`async` is a keyword used before a function to make it an async function.

```javascript
async function fetchData() {
  // This is an async function
}
```

**Key difference from normal functions:**

An async function ALWAYS returns a promise, even if you return a regular value.

```javascript
// Normal function
function regularFunction() {
  return "Hello";
}

console.log(regularFunction()); // "Hello"

// Async function
async function asyncFunction() {
  return "Hello";
}

console.log(asyncFunction()); // Promise {<fulfilled>: "Hello"}
```

Even though we returned a string, the async function automatically wraps it in a promise! And if we return a promise directly then that promise will be the returned value.

**Using the returned promise:**

```javascript
async function greet() {
  return "Hello World";
}

greet().then((message) => {
  console.log(message); // "Hello World"
});
```

**The `await` Keyword**

`await` is used before a promise to wait for it to resolve.

**Important rules:**

1. `await` can ONLY be used inside an `async` function
2. `await` pauses the function execution until the promise resolves
3. `await` returns the resolved value of the promise

```javascript
async function fetchData() {
  const result = await somePromise;
  console.log(result); // The resolved value
}
```

**Simple Example:**

```javascript
function getData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("Data received!");
    }, 2000);
  });
}

async function fetchData() {
  console.log("Fetching data...");

  const data = await getData(); // Wait for promise to resolve

  console.log(data); // "Data received!" (after 2 seconds)
}

fetchData();
// Output:
// Fetching data...
// (wait 2 seconds)
// Data received!
```

**Async/Await is Syntactic Sugar**

Behind the scenes, async/await is just a cleaner way to write `.then()` and `.catch()`. JavaScript still uses promises underneath.

```javascript
// Using .then()
function fetchData() {
  getData().then((data) => {
    console.log(data);
  });
}

// Using async/await (same thing, cleaner syntax)
async function fetchData() {
  const data = await getData();
  console.log(data);
}
```

Both do the same thing, but async/await is more readable!

**Key Difference: Function Suspension**

This is where async/await behaves differently from `.then()`.

**With `.then()` - code below executes immediately:**

```javascript
function fetchData() {
  p1.then((res) => {
    console.log(res); // Printed after 5s
  });

  console.log("Hello world"); // Printed IMMEDIATELY
}

// Output:
// Hello world (immediately)
// (promise result after 5s)
```

**With `await` - function gets suspended:**

```javascript
async function fetchData() {
  const res = await p1; // Function PAUSES here

  console.log(res); // Printed after 5s
  console.log("Hello world"); // Also printed after 5s
}

// Output:
// (wait 5 seconds)
// (promise result)
// Hello world
```

**What happens when function is suspended?**

1. When `await` is encountered, the function is paused
2. The function is removed from the call stack
3. Other code continues to execute
4. When promise resolves, event loop puts the function back in call stack
5. Function resumes from where it left off

**Important:** Only the FUNCTION is suspended, not the entire JavaScript execution!

```javascript
async function fetchData() {
  console.log("Start");

  const data = await getData(); // Function pauses HERE

  console.log("Data:", data);
  console.log("End");
}

fetchData();
console.log("Outside function"); // This runs while fetchData is waiting!

// Output:
// Start
// Outside function (runs while fetchData is paused!)
// Data: ... (after promise resolves)
// End
```

**Real-World Example: E-commerce Order**

Let's rewrite our order flow using async/await:

**With Promises (.then chain):**

```javascript
createOrder(cart)
  .then((orderId) => {
    console.log("Order ID:", orderId);
    return proceedToPayment(orderId);
  })
  .then((paymentInfo) => {
    console.log("Payment Info:", paymentInfo);
    return orderSummary(paymentInfo);
  })
  .then((summary) => {
    console.log("Order Summary:", summary);
    return updateWalletBalance(summary);
  })
  .then((balance) => {
    console.log("Remaining Balance:", balance);
  })
  .catch((error) => {
    console.error("Error:", error.message);
  });
```

**With Async/Await (cleaner!):**

```javascript
async function processOrder() {
  try {
    const orderId = await createOrder(cart);
    console.log("Order ID:", orderId);

    const paymentInfo = await proceedToPayment(orderId);
    console.log("Payment Info:", paymentInfo);

    const summary = await orderSummary(paymentInfo);
    console.log("Order Summary:", summary);

    const balance = await updateWalletBalance(summary);
    console.log("Remaining Balance:", balance);
  } catch (error) {
    console.error("Error:", error.message);
  }
}

processOrder();
```

Much cleaner and easier to read! It looks like synchronous code.

**Error Handling with Try/Catch**

With async/await, we use `try/catch` to handle errors instead of `.catch()`.

```javascript
async function fetchUserData() {
  try {
    const user = await getUser();
    const orders = await getOrders(user.id);
    console.log(orders);
  } catch (error) {
    console.error("Something went wrong:", error.message);
  }
}
```

If ANY await inside the `try` block rejects, it jumps to the `catch` block.

**Multiple Awaits - Sequential Execution**

When you have multiple `await` statements, they execute one after another (sequentially).

**Example 1: p1 takes longest (5 seconds)**

```javascript
// p1 - 5s, p2 - 3s, p3 - 1s

async function getData() {
  const result1 = await p1;
  console.log("P1 result", result1); // After 5 seconds

  const result2 = await p2;
  console.log("P2 result", result2); // After 5 seconds (not 8!)

  const result3 = await p3;
  console.log("P3 result", result3); // After 5 seconds (not 9!)
}
```

**Why all after 5 seconds?**

**Timeline:**

```
Time 0s:
  - await p1 encountered
  - p1 starts (5s timer)
  - p2 starts in background (3s timer)
  - p3 starts in background (1s timer)
  - Function suspended

Time 1s:
  - p3 completes (but we're not awaiting it yet)

Time 3s:
  - p2 completes (but we're not awaiting it yet)

Time 5s:
  - p1 completes
  - Function resumes
  - Logs "P1 result"
  - Encounters await p2
  - p2 ALREADY resolved! (at 3s)
  - Immediately gets p2 result
  - Logs "P2 result"
  - Encounters await p3
  - p3 ALREADY resolved! (at 1s)
  - Immediately gets p3 result
  - Logs "P3 result"
```

All three are logged at 5 seconds because p2 and p3 finished earlier while waiting for p1!

**Example 2: p3 takes longest (6 seconds)**

```javascript
// p1 - 1s, p2 - 4s, p3 - 6s

async function getData() {
  const result1 = await p1;
  console.log("P1 result", result1); // After 1 second

  const result2 = await p2;
  console.log("P2 result", result2); // After 4 seconds

  const result3 = await p3;
  console.log("P3 result", result3); // After 6 seconds
}
```

**Timeline:**

```
Time 0s:
  - await p1 encountered
  - All promises start because they are directly called
  - Function suspended

Time 1s:
  - p1 completes
  - Function resumes
  - Logs "P1 result"
  - Encounters await p2
  - p2 still running (needs 3 more seconds)
  - Function suspended again

Time 4s:
  - p2 completes
  - Function resumes
  - Logs "P2 result"
  - Encounters await p3
  - p3 still running (needs 2 more seconds)
  - Function suspended again

Time 6s:
  - p3 completes
  - Function resumes
  - Logs "P3 result"
```

**Understanding Promise Registration**

Important concept: When you create a promise or call a function that returns a promise, it starts executing IMMEDIATELY, even before you `await` it.

```javascript
async function example() {
  // These promises START executing immediately
  const p1 = slowOperation1(); // Starts now!
  const p2 = slowOperation2(); // Starts now!
  const p3 = slowOperation3(); // Starts now!

  // Now we wait for them
  const result1 = await p1;
  const result2 = await p2;
  const result3 = await p3;
}
```

All three operations run concurrently! But we wait for them sequentially.

**Parallel vs Sequential Execution**

**Sequential (slower):**

```javascript
async function sequential() {
  const result1 = await slowOperation1(); // Wait 3s
  const result2 = await slowOperation2(); // Wait 3s
  const result3 = await slowOperation3(); // Wait 3s
  // Total: 9 seconds
}
```

**Parallel (faster):**

```javascript
async function parallel() {
  // Start all at once
  const p1 = slowOperation1();
  const p2 = slowOperation2();
  const p3 = slowOperation3();

  // Wait for all
  const result1 = await p1;
  const result2 = await p2;
  const result3 = await p3;
  // Total: 3 seconds (they run together!)
}
```

**Or use Promise.all:**

```javascript
async function parallel() {
  const results = await Promise.all([
    slowOperation1(),
    slowOperation2(),
    slowOperation3(),
  ]);
  // Total: 3 seconds
}
```

**How Function Suspension Works**

Let's trace through execution step by step:

```javascript
const p1 = new Promise((resolve) => {
  setTimeout(() => resolve("P1 done"), 5000);
});

async function handleData() {
  console.log("Before await");

  const result = await p1; // Function pauses here

  console.log("After await:", result);
  console.log("Function complete");
}

console.log("Start");
handleData();
console.log("End");
```

**Execution flow:**

```
1. "Start" prints
2. handleData() called
3. "Before await" prints
4. await p1 encountered
5. Function SUSPENDED and removed from call stack
6. "End" prints (code outside continues!)
7. ... wait 5 seconds ...
8. p1 resolves
9. handleData() back to call stack via microtask queue
10. "After await: P1 done" prints
11. "Function complete" prints
```

**Output:**

```
Start
Before await
End
(wait 5 seconds)
After await: P1 done
Function complete
```

**Common Mistakes**

**Mistake 1: Forgetting `async` keyword**

```javascript
// ✗ Wrong
function getData() {
  const data = await fetchData(); // Error! await only in async
}

// ✓ Correct
async function getData() {
  const data = await fetchData();
}
```

**Mistake 2: Not using `await`**

```javascript
// ✗ Wrong
async function getData() {
  const data = fetchData(); // Returns promise, not data!
  console.log(data); // Promise object
}

// ✓ Correct
async function getData() {
  const data = await fetchData(); // Returns actual data
  console.log(data); // The data
}
```

**Mistake 3: Sequential when parallel would be better**

```javascript
// ✗ Slower (6 seconds total)
async function getUsers() {
  const user1 = await fetchUser(1); // 3s
  const user2 = await fetchUser(2); // 3s
}

// ✓ Faster (3 seconds total)
async function getUsers() {
  const [user1, user2] = await Promise.all([fetchUser(1), fetchUser(2)]);
}
```

**When to Use What?**

**Use async/await when:**

- You want cleaner, more readable code
- You have sequential operations
- You need to use values from previous operations
- You want easier debugging

**Use .then() when:**

- You need code below to execute immediately
- You're working with older codebases
- You have simple promise chains

**Key Takeaways**

1. **`async` makes function always return a promise**

2. **`await` pauses function until promise resolves**

3. **Only function is suspended**, not entire JavaScript execution

4. **Async/await is syntactic sugar** over promises

5. **Use try/catch** for error handling

6. **Multiple awaits execute sequentially** but promises can resolve in parallel

7. **Function suspension:**
   - Function removed from call stack
   - Goes to microtask queue when promise resolves
   - Event loop brings it back to call stack

8. **Code after await doesn't execute** until promise resolves (unlike .then)

## Promise APIs

JavaScript provides several built-in methods to work with multiple promises at once. Let's understand each one.

**Overview**

All these methods:

- Take an iterable (usually an array) of promises
- Make concurrent requests (all promises run together)
- Return different results based on their behavior

The four main Promise APIs are:

1. `Promise.all()`
2. `Promise.allSettled()`
3. `Promise.race()`
4. `Promise.any()`

**Promise.all()**

`Promise.all()` waits for ALL promises to succeed. If any promise fails, it immediately returns that error.

**Use case:** When you need ALL operations to succeed.

**Syntax:**

```javascript
const result = await Promise.all([p1, p2, p3]);
```

**Success Case: All promises succeed**

```javascript
const p1 = new Promise((resolve) =>
  setTimeout(() => resolve("P1 success"), 2000),
);
const p2 = new Promise((resolve) =>
  setTimeout(() => resolve("P2 success"), 3000),
);
const p3 = new Promise((resolve) =>
  setTimeout(() => resolve("P3 success"), 1000),
);

const result = await Promise.all([p1, p2, p3]);
console.log(result);
// ["P1 success", "P2 success", "P3 success"]
// After 3 seconds (waits for slowest promise)
```

**Timeline:**

```
Time 0s:  All promises start
Time 1s:  p3 completes ✓
Time 2s:  p1 completes ✓
Time 3s:  p2 completes ✓ → Promise.all resolves
Result: ["P1 success", "P2 success", "P3 success"]
```

**Error Case: Any promise fails**

```javascript
const p1 = new Promise((resolve, reject) =>
  setTimeout(() => reject("P1 error"), 2000),
);
const p2 = new Promise((resolve) =>
  setTimeout(() => resolve("P2 success"), 3000),
);
const p3 = new Promise((resolve) =>
  setTimeout(() => resolve("P3 success"), 1000),
);

try {
  const result = await Promise.all([p1, p2, p3]);
} catch (error) {
  console.log(error);
  // "P1 error"
  // After 2 seconds (fails immediately when first promise rejects)
}
```

**Timeline:**

```
Time 0s:  All promises start
Time 1s:  p3 completes ✓
Time 2s:  p1 FAILS ✗ → Promise.all immediately rejects
Time 3s:  p2 completes ✓ (but Promise.all already failed)
Result: "P1 error" (after 2 seconds)
```

**Key points about Promise.all():**

1. **Waits for ALL** promises to resolve
2. **Fails fast** - returns error as soon as ANY promise rejects
3. **Returns array** of results in same order as input
4. **Total time** = time of slowest promise
5. **Use when** you need all operations to succeed

**Real-world example:**

```javascript
async function loadUserDashboard(userId) {
  try {
    // Need ALL data before showing dashboard
    const [user, orders, notifications] = await Promise.all([
      fetchUser(userId),
      fetchOrders(userId),
      fetchNotifications(userId),
    ]);

    displayDashboard(user, orders, notifications);
  } catch (error) {
    console.error("Failed to load dashboard:", error);
  }
}
```

**Promise.allSettled()**

`Promise.allSettled()` waits for ALL promises to complete (either resolve or reject). It never fails - it always returns results for all promises.

**Use case:** When you want to know the outcome of ALL promises, regardless of success or failure.

**Syntax:**

```javascript
const result = await Promise.allSettled([p1, p2, p3]);
```

**Success Case: All promises succeed**

```javascript
const p1 = new Promise((resolve) =>
  setTimeout(() => resolve("P1 success"), 2000),
);
const p2 = new Promise((resolve) =>
  setTimeout(() => resolve("P2 success"), 3000),
);
const p3 = new Promise((resolve) =>
  setTimeout(() => resolve("P3 success"), 1000),
);

const result = await Promise.allSettled([p1, p2, p3]);
console.log(result);
// [
//   { status: "fulfilled", value: "P1 success" },
//   { status: "fulfilled", value: "P2 success" },
//   { status: "fulfilled", value: "P3 success" }
// ]
// After 3 seconds (waits for all to complete)
```

**Mixed Case: Some succeed, some fail**

```javascript
const p1 = new Promise((resolve, reject) =>
  setTimeout(() => reject("P1 error"), 2000),
);
const p2 = new Promise((resolve) =>
  setTimeout(() => resolve("P2 success"), 3000),
);
const p3 = new Promise((resolve) =>
  setTimeout(() => resolve("P3 success"), 1000),
);

const result = await Promise.allSettled([p1, p2, p3]);
console.log(result);
// [
//   { status: "rejected", reason: "P1 error" },
//   { status: "fulfilled", value: "P2 success" },
//   { status: "fulfilled", value: "P3 success" }
// ]
// After 3 seconds (waits for ALL to complete)
```

**Timeline:**

```
Time 0s:  All promises start
Time 1s:  p3 completes ✓
Time 2s:  p1 FAILS ✗ (but continues waiting)
Time 3s:  p2 completes ✓ → Promise.allSettled resolves
Result: Array with all outcomes (after 3 seconds)
```

**Key points about Promise.allSettled():**

1. **Waits for ALL** promises to complete (success or failure)
2. **Never rejects** - always returns an array of results
3. **Returns objects** with `status` and `value`/`reason`
4. **Total time** = time of slowest promise
5. **Use when** you want results from all promises regardless of failures

**Real-world example:**

```javascript
async function uploadMultipleFiles(files) {
  const uploadPromises = files.map((file) => uploadFile(file));

  const results = await Promise.allSettled(uploadPromises);

  const successful = results.filter((r) => r.status === "fulfilled");
  const failed = results.filter((r) => r.status === "rejected");

  console.log(`${successful.length} uploaded, ${failed.length} failed`);

  // Show which files failed
  failed.forEach((result, index) => {
    console.log(`File ${index} failed:`, result.reason);
  });
}
```

**Promise.race()**

`Promise.race()` returns the result of the FIRST promise that settles (either resolves or rejects).

**Use case:** When you only care about the fastest response, or want to set timeouts.

**Syntax:**

```javascript
const result = await Promise.race([p1, p2, p3]);
```

**Success Case: Fastest promise succeeds**

```javascript
const p1 = new Promise((resolve) =>
  setTimeout(() => resolve("P1 success"), 2000),
);
const p2 = new Promise((resolve) =>
  setTimeout(() => resolve("P2 success"), 3000),
);
const p3 = new Promise((resolve) =>
  setTimeout(() => resolve("P3 success"), 1000),
);

const result = await Promise.race([p1, p2, p3]);
console.log(result);
// "P3 success"
// After 1 second (first to complete)
```

**Timeline:**

```
Time 0s:  All promises start
Time 1s:  p3 completes ✓ → Promise.race resolves immediately
Time 2s:  p1 completes ✓ (ignored)
Time 3s:  p2 completes ✓ (ignored)
Result: "P3 success" (after 1 second)
```

**Error Case: Fastest promise fails**

```javascript
const p1 = new Promise((resolve) =>
  setTimeout(() => resolve("P1 success"), 2000),
);
const p2 = new Promise((resolve) =>
  setTimeout(() => resolve("P2 success"), 3000),
);
const p3 = new Promise((resolve, reject) =>
  setTimeout(() => reject("P3 error"), 1000),
);

try {
  const result = await Promise.race([p1, p2, p3]);
} catch (error) {
  console.log(error);
  // "P3 error"
  // After 1 second (first to settle, even though it failed)
}
```

**Timeline:**

```
Time 0s:  All promises start
Time 1s:  p3 FAILS ✗ → Promise.race rejects immediately
Time 2s:  p1 completes ✓ (ignored)
Time 3s:  p2 completes ✓ (ignored)
Result: "P3 error" (after 1 second)
```

**Key points about Promise.race():**

1. **Returns FIRST** settled promise (success or failure)
2. **Can succeed or fail** depending on which finishes first
3. **Ignores** all other promises after first one settles
4. **Total time** = time of fastest promise
5. **Use when** you want the fastest result or need timeouts

**Real-world example: Multiple API servers**

```javascript
async function fetchFromFastestServer(data) {
  // Try multiple servers, use whichever responds first
  const result = await Promise.race([
    fetch("https://server1.com/api", { body: data }),
    fetch("https://server2.com/api", { body: data }),
    fetch("https://server3.com/api", { body: data }),
  ]);
  return result;
}
```

**Promise.any()**

`Promise.any()` returns the FIRST promise that successfully resolves. It ignores rejections until all promises fail.

**Use case:** When you need at least one successful result, and don't care which one.

**Syntax:**

```javascript
const result = await Promise.any([p1, p2, p3]);
```

**Success Case: At least one promise succeeds**

```javascript
const p1 = new Promise((resolve) =>
  setTimeout(() => resolve("P1 success"), 2000),
);
const p2 = new Promise((resolve) =>
  setTimeout(() => resolve("P2 success"), 3000),
);
const p3 = new Promise((resolve) =>
  setTimeout(() => resolve("P3 success"), 1000),
);

const result = await Promise.any([p1, p2, p3]);
console.log(result);
// "P3 success"
// After 1 second (first successful promise)
```

**Timeline:**

```
Time 0s:  All promises start
Time 1s:  p3 succeeds ✓ → Promise.any resolves immediately
Time 2s:  p1 succeeds ✓ (ignored)
Time 3s:  p2 succeeds ✓ (ignored)
Result: "P3 success" (after 1 second)
```

**Mixed Case: Some fail, but at least one succeeds**

```javascript
const p1 = new Promise((resolve) =>
  setTimeout(() => resolve("P1 success"), 2000),
);
const p2 = new Promise((resolve) =>
  setTimeout(() => resolve("P2 success"), 3000),
);
const p3 = new Promise((resolve, reject) =>
  setTimeout(() => reject("P3 error"), 1000),
);

const result = await Promise.any([p1, p2, p3]);
console.log(result);
// "P1 success"
// After 2 seconds (first successful promise, ignores p3 failure)
```

**Timeline:**

```
Time 0s:  All promises start
Time 1s:  p3 FAILS ✗ (ignored, waiting for success)
Time 2s:  p1 succeeds ✓ → Promise.any resolves
Time 3s:  p2 succeeds ✓ (ignored)
Result: "P1 success" (after 2 seconds)
```

**All Fail Case: Every promise rejects**

```javascript
const p1 = new Promise((resolve, reject) =>
  setTimeout(() => reject("P1 error"), 2000),
);
const p2 = new Promise((resolve, reject) =>
  setTimeout(() => reject("P2 error"), 3000),
);
const p3 = new Promise((resolve, reject) =>
  setTimeout(() => reject("P3 error"), 1000),
);

try {
  const result = await Promise.any([p1, p2, p3]);
} catch (error) {
  console.log(error.errors);
  // ["P1 error", "P2 error", "P3 error"]
  // After 3 seconds (waits for all to fail)
  console.log(error.constructor.name);
  // "AggregateError"
}
```

**Timeline:**

```
Time 0s:  All promises start
Time 1s:  p3 FAILS ✗ (ignored, still hoping for success)
Time 2s:  p1 FAILS ✗ (ignored, still hoping for success)
Time 3s:  p2 FAILS ✗ → All failed, Promise.any rejects with AggregateError
Result: AggregateError with all errors (after 3 seconds)
```

**Key points about Promise.any():**

1. **Returns FIRST** successful promise
2. **Ignores failures** until all promises fail
3. **Only rejects** if ALL promises fail (AggregateError)
4. **Total time** = time of first success (or all failures)
5. **Use when** you need at least one success

**Real-world example:**

```javascript
async function loadImage(urls) {
  try {
    // Try to load image from multiple CDNs
    // Use whichever succeeds first
    const imageData = await Promise.any([
      fetch(urls.cdn1),
      fetch(urls.cdn2),
      fetch(urls.cdn3),
    ]);
    return imageData;
  } catch (error) {
    console.error("All CDNs failed:", error.errors);
  }
}
```

**Comparison Table**

| Method                 | Resolves When  | Rejects When                        | Use Case                  |
| ---------------------- | -------------- | ----------------------------------- | ------------------------- |
| `Promise.all()`        | ALL succeed    | ANY fails (immediately)             | Need all results          |
| `Promise.allSettled()` | ALL complete   | Never (always returns results)      | Want all outcomes         |
| `Promise.race()`       | FIRST settles  | FIRST settles (if it's a rejection) | Need fastest response     |
| `Promise.any()`        | FIRST succeeds | ALL fail                            | Need at least one success |

**Quick Reference with Examples**

```javascript
// Promise.all - Need ALL to succeed
const all = await Promise.all([p1, p2, p3]);
// Result: ["result1", "result2", "result3"]
// Fails: If any promise fails

// Promise.allSettled - Want ALL outcomes
const settled = await Promise.allSettled([p1, p2, p3]);
// Result: [
//   { status: "fulfilled", value: "result1" },
//   { status: "rejected", reason: "error2" },
//   { status: "fulfilled", value: "result3" }
// ]
// Never fails

// Promise.race - Need FASTEST (success or failure)
const race = await Promise.race([p1, p2, p3]);
// Result: "fastest result" or Error (whichever comes first)

// Promise.any - Need FIRST SUCCESS
const any = await Promise.any([p1, p2, p3]);
// Result: "first successful result"
// Fails: Only if ALL promises fail (AggregateError)
```

**Practical Decision Guide**

**Use `Promise.all()` when:**

- All operations are critical
- You can't proceed if any fails
- Example: Loading all required data for a page

**Use `Promise.allSettled()` when:**

- You want to attempt all operations
- Some failures are acceptable
- Example: Batch operations where you want to know which succeeded

**Use `Promise.race()` when:**

- You want the fastest result
- First response wins
- Example: Timeouts, racing multiple servers

**Use `Promise.any()` when:**

- You need at least one success
- Don't care which one succeeds
- Example: Multiple fallback options

**Key Takeaways**

1. **All methods run promises concurrently** - promises execute in parallel

2. **Promise.all()** - "All or nothing" approach

3. **Promise.allSettled()** - "I want to know everything"

4. **Promise.race()** - "First one wins (success or failure)"

5. **Promise.any()** - "First success wins, ignore failures"

6. **Timing depends on use case:**
   - Promise.all/allSettled: Wait for all
   - Promise.race: Wait for first to settle
   - Promise.any: Wait for first success (or all failures)

## The `this` Keyword in JavaScript

The `this` keyword in JavaScript refers to an object. But WHICH object it refers to depends on HOW and WHERE it's used.

Think of `this` as a special variable that points to different objects in different situations. It's context-dependent.

**The Golden Rule:**

The value of `this` is determined by **how a function is called**, not where it's defined (except for arrow functions).

**1. `this` in Global Scope**

When you use `this` in the global scope (outside any function), it refers to the global object.

```javascript
console.log(this); // window (in browser) or global (in Node.js)
```

**What's the global object?**

It depends on where JavaScript is running:

- **Browser**: `window`
- **Node.js**: `global`

```javascript
// In browser
console.log(this === window); // true

// In Node.js
console.log(this === global); // true
```

**2. `this` in Regular Functions**

This is where it gets tricky. The value depends on whether you're in strict mode or not.

**Non-Strict Mode:**

```javascript
function printThis() {
  console.log(this);
}

printThis(); // window (in browser)
```

**Why `window`?**

In non-strict mode, JavaScript does something called **"this substitution"**. When `this` would be `undefined`, JavaScript automatically replaces it with the global object.

```
Function called without reference
→ this should be undefined
→ JavaScript substitutes it with window
→ Result: this = window
```

**Strict Mode:**

```javascript
"use strict";

function printThis() {
  console.log(this);
}

printThis(); // undefined
```

In strict mode, there's no "this substitution". If `this` has no value, it remains `undefined`.

**Which is better?**

Strict mode is better because it makes errors more obvious. Use `"use strict"` at the top of your files or functions.

**3. `this` with Function Reference**

When you call a function using a reference (like `object.method()`), `this` refers to that object.

```javascript
function printThis() {
  console.log(this);
}

// Called without reference
printThis(); // undefined (strict mode) or window (non-strict)

// Called with reference
window.printThis(); // window (the reference used)
```

The reference before the dot (`.`) becomes the value of `this`.

**4. `this` in Object Methods**

When a function is a method of an object (function inside an object), `this` refers to that object.

```javascript
let student = {
  name: "Bhupesh",
  age: 24,
  printName: function () {
    console.log(this.name);
  },
};

student.printName(); // "Bhupesh"
```

**Why?**

Because we called the method using `student.printName()`. The object before the dot (`student`) becomes `this`.

```
student.printName()
   ↑
   └─ this
```

**Important:** It's about HOW you call it, not WHERE it's defined!

```javascript
let student = {
  name: "Bhupesh",
  printName: function () {
    console.log(this.name);
  },
};

let printFunc = student.printName;
printFunc(); // undefined (this is not student anymore!)
```

When we store the method in a variable and call it without the object reference, `this` loses its context.

**5. Changing `this` with call, apply, bind**

JavaScript provides three methods to explicitly set the value of `this`:

**Using `call()`:**

```javascript
let student = {
  name: "John",
  printName: function () {
    console.log(this.name);
  },
};

let student2 = {
  name: "Matt",
};

// Call printName but set this to student2
student.printName.call(student2); // "Matt"
```

**How it works:**

```
student.printName.call(student2)
                       ↑
                       └─ this will be student2
```

**Using `apply()`:**

Similar to `call()`, but arguments are passed as an array:

```javascript
function introduce(age, city) {
  console.log(`I'm ${this.name}, ${age} years old, from ${city}`);
}

let person = { name: "John" };

introduce.call(person, 25, "Mumbai");
// I'm John, 25 years old, from Mumbai

introduce.apply(person, [25, "Mumbai"]); // Same result
// apply takes arguments as array
```

**Using `bind()`:**

Creates a new function with `this` permanently set:

```javascript
let student = {
  name: "Bhupesh",
  printName: function () {
    console.log(this.name);
  },
};

let student2 = { name: "Mohit" };

// Create a new function with this bound to student2
let boundFunction = student.printName.bind(student2);
boundFunction(); // "Mohit"
```

**Difference between call/apply and bind:**

- `call()` and `apply()` - Execute the function immediately
- `bind()` - Returns a new function with `this` set

**Real-world example:**

```javascript
let user = {
  name: "Alice",
  greet: function () {
    console.log(`Hello, ${this.name}`);
  },
};

// Problem: setTimeout loses context
setTimeout(user.greet, 1000); // Hello, undefined

// Solution 1: Use bind
setTimeout(user.greet.bind(user), 1000); // Hello, Alice

// Solution 2: Use arrow function
setTimeout(() => user.greet(), 1000); // Hello, Alice
```

**6. `this` in Arrow Functions**

Arrow functions are special - they DON'T have their own `this` binding!

Instead, they inherit `this` from their surrounding (lexical) scope - where the code is physically written in your file.

```javascript
const arrowFunction = () => {
  console.log(this);
};

arrowFunction(); // window (in global scope)
```

Even if you try to change it with `call()`, it won't work:

```javascript
const arrowFunction = () => {
  console.log(this);
};

let obj = { name: "Test" };
arrowFunction.call(obj); // Still window! (can't change arrow function's this)
```

**Arrow Functions in Objects:**

```javascript
let obj = {
  name: "Bhupesh",
  print: () => {
    console.log(this); // window (NOT obj!)
  },
};

obj.print(); // window
```

**Why `window` and not `obj`?**

Because arrow functions look at where they're physically written (lexical scope). The arrow function is written in the global scope (inside the object literal, but not inside another function), so it takes `this` from the global scope.

Think of it like this:

```javascript
// The arrow function "sees" this scope
const obj = {
  // ← We're in global scope here
  name: "John",
  print: () => {
    console.log(this); // Inherits from global scope
  },
};
```

**Arrow Function Inside a Method:**

```javascript
let obj = {
  name: "John",
  print: function () {
    // Regular function - this = obj

    let innerArrow = () => {
      // Arrow function - inherits this from print method
      console.log(this.name); // "John"
    };

    innerArrow();
  },
};

obj.print(); // "John"
```

**Why does this work?**

```
obj.print() is called
  ↓
Regular function - this = obj
  ↓
Arrow function inherits this from parent scope
  ↓
this = obj (same as parent function)
```

**Visual comparison:**

```javascript
let obj = {
  a: 1,

  // Regular function - this = obj
  regularMethod: function () {
    console.log(this); // obj
  },

  // Arrow function - this = window (global scope)
  arrowMethod: () => {
    console.log(this); // window
  },

  // Regular function with arrow inside
  methodWithArrow: function () {
    // this = obj (regular function)

    let arrow = () => {
      console.log(this); // obj (inherited from parent)
    };

    arrow();
  },
};

obj.regularMethod(); // obj
obj.arrowMethod(); // window
obj.methodWithArrow(); // obj
```

**When to use arrow functions:**

✅ **Use arrow functions:**

- For callbacks where you want to preserve `this`
- Inside methods when you need to inherit parent's `this`

❌ **Don't use arrow functions:**

- As object methods (you'll lose the object reference)
- When you need `this` to be dynamic

**7. `this` in Event Listeners (DOM Elements)**

When `this` is used inside an event handler, it refers to the HTML element that triggered the event.

```html
<button id="myButton" onclick="onButtonClick(this)">Click Me</button>
```

```javascript
function onButtonClick(element) {
  console.log("Button clicked!");
  console.log(element); // <button id="myButton">...
  console.log(element.id); // "myButton"
  console.log(element.tagName); // "BUTTON"
}
```

**Or using addEventListener:**

```javascript
document.getElementById("myButton").addEventListener("click", function () {
  console.log(this); // <button id="myButton">...
  console.log(this.id); // "myButton"
  console.log(this.tagName); // "BUTTON"
});
```

**Important:** This only works with regular functions, not arrow functions!

```javascript
// Regular function - this = button element
button.addEventListener("click", function () {
  console.log(this); // <button>
});

// Arrow function - this = window (or surrounding scope)
button.addEventListener("click", () => {
  console.log(this); // window (NOT the button!)
});
```

**Summary Table**

| Context                       | Value of `this`                 | Example                                |
| ----------------------------- | ------------------------------- | -------------------------------------- |
| Global scope                  | Global object (window/global)   | `console.log(this)`                    |
| Regular function (non-strict) | Global object                   | `function f() { this }`                |
| Regular function (strict)     | undefined                       | `"use strict"; function f() { this }`  |
| Object method                 | The object                      | `obj.method()`                         |
| Arrow function                | Lexical (inherited from parent) | `() => { this }`                       |
| Event listener                | DOM element                     | `button.onclick = function() { this }` |
| call/apply/bind               | The specified object            | `func.call(obj)`                       |

**Quick Decision Guide**

**To determine `this` value, ask:**

1. **Is it an arrow function?**
   - YES → Inherited from surrounding scope
   - NO → Continue...

2. **Is it called with call/apply/bind?**
   - YES → `this` is what you specified
   - NO → Continue...

3. **Is it called as a method (obj.method())?**
   - YES → `this` is the object before the dot
   - NO → Continue...

4. **Is it a regular function call?**
   - Strict mode → `undefined`
   - Non-strict → Global object

**Common Mistakes**

**Mistake 1: Losing context when passing methods**

```javascript
let user = {
  name: "Alice",
  greet() {
    console.log(`Hello, ${this.name}`);
  },
};

let greetFunc = user.greet;
greetFunc(); // Hello, undefined (lost context!)

// Fix: Use bind
let boundGreet = user.greet.bind(user);
boundGreet(); // Hello, Alice
```

**Mistake 2: Using arrow functions as methods**

```javascript
// ✗ Wrong
let obj = {
  name: "Bob",
  greet: () => {
    console.log(this.name); // undefined (this = window)
  },
};

// ✓ Correct
let obj = {
  name: "Bob",
  greet: function () {
    console.log(this.name); // "Bob"
  },
};
```

**Mistake 3: Not understanding arrow function inheritance**

```javascript
function Timer() {
  this.seconds = 0;

  // ✗ Wrong - regular function loses context
  setInterval(function () {
    this.seconds++; // this = window, not Timer!
  }, 1000);

  // ✓ Correct - arrow function inherits context
  setInterval(() => {
    this.seconds++; // this = Timer instance
  }, 1000);
}
```

**Key Takeaways**

1. **`this` is context-dependent** - depends on how function is called

2. **Global scope** → global object (window/global)

3. **Regular function** → undefined (strict) or global object (non-strict)

4. **Object method** → the object itself

5. **Arrow function** → inherited from surrounding scope (lexical)

6. **Event listener** → DOM element (regular functions only)

7. **call/apply/bind** → manually set `this` value

8. **Arrow functions can't have `this` changed** - they always inherit from parent scope

---

## Function Currying in JavaScript

Understanding how to transform functions to make them more reusable and flexible.

**What is Function Currying?**

Function currying is a technique where you transform a function that takes multiple arguments into a series of functions that each take a single argument.

Instead of calling a function like this:

```javascript
function(a, b, c)
```

You transform it to:

```javascript
function(a)(b)(c)
```

**Simple Example:**

**Before Currying (Normal Function):**

```javascript
function sum(a, b) {
  return a + b;
}

console.log(sum(2, 3)); // 5
```

**After Currying:**

```javascript
function sum(a) {
  return function (b) {
    return a + b;
  };
}

console.log(sum(2)(3)); // 5
```

Notice the difference:

- Normal: `sum(2, 3)` - takes both arguments at once
- Curried: `sum(2)(3)` - takes arguments one at a time

**How Does It Work?**

When you call `sum(2)`, it returns a function. That returned function is waiting for the second argument `b`.

```javascript
function sum(a) {
  return function (b) {
    return a + b;
  };
}

const addTwo = sum(2); // Returns a function
console.log(addTwo); // function(b) { return 2 + b }

console.log(addTwo(3)); // 5
console.log(addTwo(5)); // 7
console.log(addTwo(10)); // 12
```

**Step by step execution:**

```
sum(2)
  ↓
Returns: function(b) { return 2 + b }
  ↓
Store in addTwo
  ↓
addTwo(3)
  ↓
Returns: 2 + 3 = 5
```

**Why Use Currying?**

The main advantage of currying is **reusability**. You can create specialized functions from generic ones.

**Advantage 1: Reusability**

Create multiple specialized functions from one generic function:

```javascript
function multiply(a) {
  return function (b) {
    return a * b;
  };
}

// Create specialized functions
let multiplyByTwo = multiply(2);
let multiplyByThree = multiply(3);
let multiplyByTen = multiply(10);

// Reuse them multiple times
console.log(multiplyByTwo(12)); // 24
console.log(multiplyByTwo(3)); // 6
console.log(multiplyByTwo(5)); // 10

console.log(multiplyByThree(3)); // 9
console.log(multiplyByThree(12)); // 36

console.log(multiplyByTen(5)); // 50
console.log(multiplyByTen(7)); // 70
```

**Benefits:**

- Create `multiplyByTwo` once, use it everywhere
- No need to remember the first argument repeatedly
- More readable code
- Easier to test and maintain

**Advantage 2: Partial Application**

Partial application means you can fix some arguments early and provide the rest later.

```javascript
function greet(greeting) {
  return function (name) {
    return `${greeting}, ${name}!`;
  };
}

// Fix the greeting early
let sayHi = greet("Hi");
let sayHello = greet("Hello");
let sayGoodMorning = greet("Good Morning");

// Use them later with different names
console.log(sayHi("Alice")); // "Hi, Alice!"
console.log(sayHi("Bob")); // "Hi, Bob!"

console.log(sayHello("John")); // "Hello, John!"
console.log(sayHello("Sarah")); // "Hello, Sarah!"

console.log(sayGoodMorning("Team")); // "Good Morning, Team!"
```

**Why is this useful?**

Instead of writing this repeatedly:

```javascript
console.log("Hi, Alice!");
console.log("Hi, Bob!");
console.log("Hi, Charlie!");
```

You create a function once and reuse it:

```javascript
let sayHi = greet("Hi");
console.log(sayHi("Alice"));
console.log(sayHi("Bob"));
console.log(sayHi("Charlie"));
```

**Real-World Example 1: Discount Calculator**

```javascript
function discount(discountPercent) {
  return function (price) {
    return price - (price * discountPercent) / 100;
  };
}

// Create discount functions for different customer types
let studentDiscount = discount(20); // 20% off
let seniorDiscount = discount(30); // 30% off
let memberDiscount = discount(10); // 10% off

// Calculate prices
console.log(studentDiscount(100)); // 80
console.log(studentDiscount(50)); // 40

console.log(seniorDiscount(100)); // 70
console.log(seniorDiscount(200)); // 140

console.log(memberDiscount(100)); // 90
```

**Real-World Example 2: Logger with Levels**

```javascript
function createLogger(level) {
  return function (module) {
    return function (message) {
      return `[${level}] [${module}] ${message}`;
    };
  };
}

// Create loggers for different levels
let errorLogger = createLogger("ERROR");
let warningLogger = createLogger("WARNING");
let infoLogger = createLogger("INFO");

// Create module-specific loggers
let authErrors = errorLogger("Auth");
let dbErrors = errorLogger("Database");
let authWarnings = warningLogger("Auth");

// Log messages
console.log(authErrors("Login failed"));
// "[ERROR] [Auth] Login failed"

console.log(dbErrors("Connection timeout"));
// "[ERROR] [Database] Connection timeout"

console.log(authWarnings("Session expiring soon"));
// "[WARNING] [Auth] Session expiring soon"
```

**Currying with Arrow Functions**

Arrow functions make currying syntax even cleaner:

```javascript
// Regular function syntax
function multiply(a) {
  return function (b) {
    return a * b;
  };
}

// Arrow function syntax (cleaner!)
const multiply = (a) => (b) => a * b;

// Usage is the same
let double = multiply(2);
console.log(double(5)); // 10
```

**Currying vs Partial Application**

People often confuse these two concepts:

**Currying:**

- Transforms a function to take arguments one at a time
- Always returns a function until all arguments are provided
- `f(a, b, c)` becomes `f(a)(b)(c)`

**Practical Currying Pattern: Configuration**

```javascript
function fetchData(config) {
  return function (endpoint) {
    return function (params) {
      return {
        url: `${config.baseURL}${endpoint}`,
        method: config.method,
        headers: config.headers,
        params: params,
      };
    };
  };
}

// Configure once
let apiConfig = {
  baseURL: "https://api.example.com",
  method: "GET",
  headers: { Authorization: "Bearer token123" },
};

let api = fetchData(apiConfig);

// Create endpoint-specific functions
let getUsers = api("/users");
let getPosts = api("/posts");

// Make requests
console.log(getUsers({ page: 1 }));
console.log(getPosts({ limit: 10 }));
```

**Advantages of Currying**

1. **Code Reusability**
   - Create specialized functions from generic ones
   - Avoid repetition

2. **Function Composition**
   - Easier to combine small functions into bigger ones
   - More modular code

3. **Delayed Execution**
   - Fix some arguments now, provide others later
   - Useful for callbacks and event handlers

4. **Better Testing**
   - Easier to test small, focused functions
   - Can mock partial functions

**When to Use Currying**

✅ **Use currying when:**

- You need to reuse a function with some fixed arguments
- Creating configuration-based functions
- Building utility libraries
- Working with higher-order functions
- Need delayed execution with partial data

❌ **Don't use currying when:**

- Function is only called once
- All arguments are always available together
- It makes code harder to understand
- Performance is critical (extra function calls add overhead)

**Common Patterns**

**Pattern 1: Event Handlers**

```javascript
const handleClick = (action) => (event) => {
  console.log(`Action: ${action}, Element: ${event.target.id}`);
};

// Create specific handlers
let saveHandler = handleClick("save");
let deleteHandler = handleClick("delete");

// Use in event listeners
button1.addEventListener("click", saveHandler);
button2.addEventListener("click", deleteHandler);
```

**Pattern 2: Form Validation**

```javascript
const validate = (rule) => (value) => {
  switch (rule) {
    case "email":
      return value.includes("@");
    case "minLength":
      return value.length >= 8;
    case "required":
      return value.length > 0;
    default:
      return true;
  }
};

let validateEmail = validate("email");
let validatePassword = validate("minLength");
let validateRequired = validate("required");

console.log(validateEmail("test@example.com")); // true
console.log(validatePassword("pass123")); // false
console.log(validateRequired("")); // false
```

**Pattern 3: Composing Functions**

```javascript
const add = (a) => (b) => a + b;
const multiply = (a) => (b) => a * b;

// Create reusable operations
let addTen = add(10);
let double = multiply(2);
let triple = multiply(3);

// Compose them
let result = triple(addTen(5)); // (5 + 10) * 3 = 45
console.log(result); // 45
```

**Key Takeaways**

1. **Currying transforms** `f(a, b, c)` into `f(a)(b)(c)`

2. **Returns a function** for each argument until all are provided

3. **Main benefit is reusability** - create specialized functions

4. **Partial application** fixes some arguments early

5. **Arrow functions** make currying syntax cleaner

6. **Use for configuration**, repeated patterns, and composition

7. **Don't overuse** - use when it actually improves code clarity

## Call, Apply & Bind in JavaScript

**What are Call, Apply, and Bind?**

Call, Apply, and Bind are methods available on every function in JavaScript. They allow us to:

1. Control what `this` refers to inside a function
2. Reuse functions with different objects
3. Borrow methods from one object and use them with another

**The Problem They Solve**

Imagine you have a method that works perfectly for one object, and you want to use it with another object. Instead of writing the same method again, you can borrow it!

```javascript
let user1 = {
  name: "John",
  greet: function () {
    console.log(`Hello, ${this.name}`);
  },
};

let user2 = {
  name: "Sarah",
  // We want to use user1's greet method here!
};

user1.greet(); // Hello, John
// How to use greet with user2? That's where call/apply/bind help!
```

**The `call()` Method**

The `call()` method lets you call a function and explicitly set what `this` should be.

**Syntax:**

```javascript
functionName.call(thisValue, arg1, arg2, arg3, ...)
```

- **First argument**: What `this` should point to
- **Remaining arguments**: Arguments for the function (passed individually)

**Example 1: Basic Usage**

```javascript
let user = {
  firstName: "John",
  lastName: "Doe",
  printFullName: function () {
    console.log(`${this.firstName} ${this.lastName}`);
  },
};

user.printFullName(); // John Doe

let user2 = {
  firstName: "Mark",
  lastName: "Smith",
};

// Borrow printFullName from user and use it with user2
user.printFullName.call(user2); // Mark Smith
```

**What happened?**

```
user.printFullName.call(user2)
                        ↑
                        └─ this will be user2 instead of user
```

**Example 2: With Arguments**

```javascript
let user = {
  firstName: "John",
  lastName: "Doe",
};

function printFullName(city, country) {
  console.log(`${this.firstName} ${this.lastName} from ${city}, ${country}`);
}

let user2 = {
  firstName: "Mark",
  lastName: "Smith",
};

// Call with user
printFullName.call(user, "Rio", "Brazil");
// "John Doe from Rio, Brazil"

// Call with user2
printFullName.call(user2, "NJ", "USA");
// "Mark Smith from NJ, USA"
```

**Breaking it down:**

```
printFullName.call(user, "Rio", "Brazil")
                    ↑      ↑       ↑
                    │      │       └─ country argument
                    │      └───────── city argument
                    └──────────────── this = user
```

**Why is this useful?**

Instead of creating the same function for each user:

```javascript
// ✗ Repetitive approach
let user = {
  firstName: "John",
  printFullName: function (city, country) {
    console.log(`${this.firstName} ${this.lastName} from ${city}, ${country}`);
  },
};

let user2 = {
  firstName: "Mark",
  printFullName: function (city, country) {
    console.log(`${this.firstName} ${this.lastName} from ${city}, ${country}`);
  },
};
```

We write it once and reuse it:

```javascript
// ✓ Reusable approach
function printFullName(city, country) {
  console.log(`${this.firstName} ${this.lastName} from ${city}, ${country}`);
}

printFullName.call(user, "Rio", "Brazil");
printFullName.call(user2, "NJ", "USA");
```

**The `apply()` Method**

The `apply()` method is almost identical to `call()`, but with ONE key difference: how you pass arguments.

**Syntax:**

```javascript
functionName.apply(thisValue, [arg1, arg2, arg3, ...])
```

- **First argument**: What `this` should point to
- **Second argument**: An **array** of arguments for the function

**Example:**

```javascript
let user = {
  firstName: "John",
  lastName: "Doe",
};

function printFullName(city, country) {
  console.log(`${this.firstName} ${this.lastName} from ${city}, ${country}`);
}

let user2 = {
  firstName: "Mark",
  lastName: "Smith",
};

// Using apply - arguments in an array
printFullName.apply(user, ["Rio", "Brazil"]);
// "John Doe from Rio, Brazil"

printFullName.apply(user2, ["NJ", "USA"]);
// "Mark Smith from NJ, USA"
```

**Difference between call() and apply():**

```javascript
// call() - arguments passed individually
printFullName.call(user, "Rio", "Brazil");

// apply() - arguments passed as an array
printFullName.apply(user, ["Rio", "Brazil"]);
```

**When to use apply()?**

Use `apply()` when you already have arguments in an array:

```javascript
function sum(a, b, c) {
  return a + b + c;
}

let numbers = [1, 2, 3];

// With apply - perfect when you have an array
let result = sum.apply(null, numbers); // 6

// With call - would need to spread the array
let result = sum.call(null, ...numbers); // 6
```

**Real-world example with apply():**

```javascript
// Finding max number in an array
let numbers = [5, 6, 2, 3, 7, 1, 9];

// Math.max expects individual arguments, not an array
// Math.max(5, 6, 2, 3, 7, 1, 9) ✓
// Math.max([5, 6, 2, 3, 7, 1, 9]) ✗

let max = Math.max.apply(null, numbers);
console.log(max); // 9

// Modern alternative: spread operator
let max = Math.max(...numbers); // 9
```

**The `bind()` Method**

The `bind()` method is different from `call()` and `apply()`. Instead of calling the function immediately, it creates a **new function** with `this` permanently set.

**Syntax:**

```javascript
let newFunction = functionName.bind(thisValue, arg1, arg2, ...)
```

- **Returns**: A new function (doesn't execute immediately)
- **First argument**: What `this` should point to
- **Remaining arguments**: Arguments for the function

**Example 1: Basic Usage**

```javascript
let user = {
  firstName: "John",
  lastName: "Doe",
};

function printFullName(city, country) {
  console.log(`${this.firstName} ${this.lastName} from ${city}, ${country}`);
}

// bind() returns a new function
let printUserName = printFullName.bind(user, "Rio", "Brazil");

// Call it later
printUserName(); // "John Doe from Rio, Brazil"
```

**Key difference from call() and apply():**

```javascript
// call() - Executes immediately
printFullName.call(user, "Rio", "Brazil"); // Runs now!

// bind() - Returns a function, executes later
let printUserName = printFullName.bind(user, "Rio", "Brazil");
printUserName(); // Runs when you call it
```

**Example 2: Multiple Users**

```javascript
let user = {
  firstName: "John",
  lastName: "Doe",
};

let user2 = {
  firstName: "Mark",
  lastName: "Smith",
};

function printFullName(city, country) {
  console.log(`${this.firstName} ${this.lastName} from ${city}, ${country}`);
}

// Create specialized functions
let printUser1 = printFullName.bind(user, "Rio", "Brazil");
let printUser2 = printFullName.bind(user2, "NJ", "USA");

// Use them whenever needed
printUser1(); // "John Doe from Rio, Brazil"
printUser2(); // "Mark Smith from NJ, USA"

// Can call multiple times
printUser1(); // "John Doe from Rio, Brazil"
printUser1(); // "John Doe from Rio, Brazil"
```

**Why is bind() useful?**

**Use Case 1: Event Handlers**

```javascript
let user = {
  name: "John",
  greet: function () {
    console.log(`Hello, ${this.name}`);
  },
};

// Problem: Loses context
setTimeout(user.greet, 1000); // Hello, undefined

// Solution: Use bind
setTimeout(user.greet.bind(user), 1000); // Hello, John
```

**Use Case 2: Partial Application (function currying)**

You can fix some arguments now and provide others later:

```javascript
function multiply(a, b) {
  return a * b;
}

// Fix first argument
let double = multiply.bind(null, 2);
let triple = multiply.bind(null, 3);

console.log(double(5)); // 10 (2 * 5)
console.log(double(10)); // 20 (2 * 10)

console.log(triple(5)); // 15 (3 * 5)
console.log(triple(10)); // 30 (3 * 10)
```

**Comparison Table**

| Method    | Executes Immediately | Arguments Format | Returns         | Use When                         |
| --------- | -------------------- | ---------------- | --------------- | -------------------------------- |
| `call()`  | ✓ Yes                | Individual       | Function result | Execute now with specific `this` |
| `apply()` | ✓ Yes                | Array            | Function result | Have arguments in array          |
| `bind()`  | ✗ No                 | Individual       | New function    | Need function for later use      |

**Visual Comparison**

```javascript
let user = { name: "John" };

function greet(greeting) {
  return `${greeting}, ${this.name}`;
}

// call() - Execute immediately
let result1 = greet.call(user, "Hello");
console.log(result1); // "Hello, John"

// apply() - Execute immediately with array
let result2 = greet.apply(user, ["Hello"]);
console.log(result2); // "Hello, John"

// bind() - Get function, execute later
let greetUser = greet.bind(user, "Hello");
let result3 = greetUser();
console.log(result3); // "Hello, John"
```

**Real-World Examples**

**Example 1: Form Validation**

```javascript
function validateInput(fieldName, value) {
  if (!value) {
    console.log(`${fieldName} is required for ${this.username}`);
    return false;
  }
  return true;
}

let user1 = { username: "john_doe" };
let user2 = { username: "sarah_smith" };

// Create validators for each user
let validateUser1 = validateInput.bind(user1);
let validateUser2 = validateInput.bind(user2);

validateUser1("email", ""); // "email is required for john_doe"
validateUser2("password", ""); // "password is required for sarah_smith"
```

**Example 2: API Requests**

```javascript
function makeRequest(endpoint, params) {
  console.log(`${this.method} request to ${this.baseURL}${endpoint}`);
  console.log("Params:", params);
}

let api = {
  baseURL: "https://api.example.com",
  method: "GET",
};

// Create specialized request functions
let getUsers = makeRequest.bind(api, "/users");
let getPosts = makeRequest.bind(api, "/posts");

getUsers({ page: 1 });
// "GET request to https://api.example.com/users"
// "Params: { page: 1 }"

getPosts({ limit: 10 });
// "GET request to https://api.example.com/posts"
// "Params: { limit: 10 }"
```

**Example 3: Method Borrowing**

```javascript
let person1 = {
  firstName: "John",
  lastName: "Doe",
  getFullName: function () {
    return `${this.firstName} ${this.lastName}`;
  },
};

let person2 = {
  firstName: "Jane",
  lastName: "Smith",
  // No getFullName method!
};

// Borrow method from person1
let name = person1.getFullName.call(person2);
console.log(name); // "Jane Smith"
```

**Common Mistakes**

**Mistake 1: Forgetting `this` context**

```javascript
let obj = {
  value: 42,
  getValue: function () {
    return this.value;
  },
};

// ✗ Loses context
let getValue = obj.getValue;
console.log(getValue()); // undefined

// ✓ Preserves context
let getValue = obj.getValue.bind(obj);
console.log(getValue()); // 42
```

**Mistake 2: Using bind() when you want immediate execution**

```javascript
function greet(name) {
  console.log(`Hello, ${name}`);
}

// ✗ Wrong - bind() doesn't execute
greet.bind(null, "John"); // Nothing happens!

// ✓ Correct - call() executes immediately
greet.call(null, "John"); // "Hello, John"

// ✓ Or execute the bound function
let boundGreet = greet.bind(null, "John");
boundGreet(); // "Hello, John"
```

**Mistake 3: Confusing call() and apply() argument format**

```javascript
function sum(a, b, c) {
  return a + b + c;
}

let numbers = [1, 2, 3];

// ✗ Wrong - call() expects individual arguments
sum.call(null, numbers); // NaN (trying to add an array)

// ✓ Correct - apply() expects an array
sum.apply(null, numbers); // 6

// ✓ Or spread with call()
sum.call(null, ...numbers); // 6
```

**Key Takeaways**

1. **call(), apply(), bind()** all control the `this` value

2. **call()** - Execute immediately, arguments individually

```javascript
func.call(thisValue, arg1, arg2);
```

3. **apply()** - Execute immediately, arguments as array

```javascript
func.apply(thisValue, [arg1, arg2]);
```

4. **bind()** - Returns new function, arguments individually

```javascript
let newFunc = func.bind(thisValue, arg1, arg2);
newFunc(); // Execute later
```

5. **Use for method borrowing** and function reusability

6. **bind() is useful** for event handlers and partial application

7. **Modern alternative**: Arrow functions for preserving `this`

---

## Async and Defer Attributes in JavaScript

Understanding how to optimally load external scripts in the browser.

**Note:** The correct spelling of the attribute is **`defer`**, not `differ`. So it should be written as:

```html
<script defer src="./script.js"></script>
```

**What are Async and Defer?**ḥ

Async and defer are **boolean attributes** used with the `<script>` tag. They help us control how external scripts are loaded and executed in the browser.

Their main job is to make sure loading scripts doesn't slow down your webpage.

**Why Do We Need Them?**

When a browser loads an HTML page, it reads the code from top to bottom (this is called **HTML parsing**). If it encounters a script tag, it might have to stop everything just to load and run that script. Async and defer help us avoid that.

**How HTML Parsing Works**

Think of HTML parsing like reading a book. The browser reads your HTML line by line, building the page as it goes. When it hits a script tag, different things happen depending on whether you use async, defer, or neither.

**Without Async or Defer (Default Behavior)**

```html
<html>
  <head>
    <script src="./script.js"></script>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

**What happens step by step:**

1. Browser starts parsing HTML
2. Encounters `<script>` tag
3. **HTML parsing STOPS completely**
4. Browser fetches `script.js` from the source
5. Browser executes `script.js`
6. Only THEN does HTML parsing continue
7. Rest of the page builds

**Visual Flow:**

```
HTML Parsing → STOP → Fetch script.js → Execute script.js → Resume HTML Parsing
```

**Why is this bad?**

If the script takes a long time to fetch (slow server, big file), the user sees a blank page until everything is done. This makes the page feel slow.

**With the `async` Attribute**

```html
<html>
  <head>
    <script async src="./script.js"></script>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

**What happens step by step:**

1. Browser starts parsing HTML
2. Encounters `<script async>` tag
3. HTML parsing **continues** while fetching the script in parallel
4. Once the script is fetched, **HTML parsing stops temporarily**
5. Script gets executed
6. HTML parsing resumes again

**Visual Flow:**

```
HTML Parsing ──────────────────→ STOP → Execute script.js → Resume
                ↕
         Fetching script.js (in parallel)
```

**Simple analogy:**

Think of it like cooking:

- HTML parsing = cooking rice
- Script fetching = ordering pizza

Without async: You stop cooking rice, go order pizza, wait for it to arrive, eat it, then continue cooking rice.

With async: You keep cooking rice while pizza is being delivered. When pizza arrives, you stop cooking rice briefly to eat it, then continue.

**With the `defer` Attribute**

```html
<html>
  <head>
    <script defer src="./script.js"></script>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

**What happens step by step:**

1. Browser starts parsing HTML
2. Encounters `<script defer>` tag
3. HTML parsing **continues** while fetching the script in parallel
4. HTML parsing finishes completely
5. **Only then** the fetched script gets executed

**Visual Flow:**

```
HTML Parsing ──────────────────→ Done! → Execute script.js
                ↕
         Fetching script.js (in parallel)
```

**Simple analogy:**

Think of it like a meeting:

- HTML parsing = your main work
- Script = a presentation you need to prepare

With defer: You keep doing your main work while the presentation downloads. Once your main work is completely done, you sit down and do the presentation.

**Comparison: All Three Together**

```html
<!-- No attribute: Blocks everything -->
<script src="./script1.js"></script>

<!-- Async: Fetches in parallel, executes as soon as fetched -->
<script async src="./script2.js"></script>

<!-- Defer: Fetches in parallel, executes after HTML is done -->
<script defer src="./script3.js"></script>
```

**Visual Comparison:**

```
Normal (no attribute):
HTML ──→ STOP → Fetch → Execute → Resume HTML ──→

Async:
HTML ──────────────────→ STOP → Execute → Resume HTML
         Fetch ────→ Done

Defer:
HTML ──────────────────────────────→ Done → Execute
         Fetch ────→ Done
```

**Multiple Scripts: Order of Execution**

This is where the difference between async and defer becomes really important.

**Multiple Scripts with Defer:**

```html
<script defer src="./script1.js"></script>
<script defer src="./script2.js"></script>
<script defer src="./script3.js"></script>
```

**What happens:**

1. All three scripts start fetching in parallel
2. HTML parsing continues
3. HTML parsing completes
4. Scripts execute **in order**: script1 → script2 → script3

**Defer maintains the order!** Even if script3 finishes fetching first, it will wait until script1 and script2 have executed.

```
Fetching:
script1 ─────────────→ Done
script2 ──────────→ Done
script3 ────→ Done (fetched first!)

Execution (after HTML done):
script1 → script2 → script3 (order maintained!)
```

**Multiple Scripts with Async:**

```html
<script async src="./script1.js"></script>
<script async src="./script2.js"></script>
<script async src="./script3.js"></script>
```

**What happens:**

1. All three scripts start fetching in parallel
2. HTML parsing continues
3. Whichever script finishes fetching first, executes first
4. **Order is NOT guaranteed!**

```
Fetching:
script1 ─────────────→ Done
script2 ──────────→ Done
script3 ────→ Done (fetched first!)

Execution (as soon as each one is fetched):
script3 → script2 → script1 (order NOT maintained!)
```

**Why does order matter?**

If script2 depends on script1 (uses something defined in script1), and script2 runs first, it will break!

```javascript
// script1.js
const config = { apiURL: "https://api.example.com" };

// script2.js (depends on script1)
fetch(config.apiURL); // Error if script2 runs before script1!
```

**When to Use What?**

**Use `defer` when:**

- Scripts depend on each other (order matters)
- Scripts need the DOM to be fully loaded
- You want predictable execution order
- Most common use case for general scripts

```html
<!-- These run in order after HTML is done -->
<script defer src="./utils.js"></script>
<script defer src="./app.js"></script>
<script defer src="./main.js"></script>
```

**Use `async` when:**

- Script is completely independent
- Script doesn't depend on other scripts
- Script doesn't need the DOM
- You want it to run as soon as possible

```html
<!-- Independent scripts, order doesn't matter -->
<script async src="./analytics.js"></script>
<script async src="./chat-widget.js"></script>
```

**Use neither (default) when:**

- Script must run before the rest of the page loads
- Script modifies the `<head>` section
- Very rare cases

**Real-World Example**

```html
<html>
  <head>
    <!-- Analytics: Independent, run ASAP -->
    <script async src="./analytics.js"></script>

    <!-- These depend on each other, run in order -->
    <script defer src="./utils.js"></script>
    <script defer src="./framework.js"></script>
    <script defer src="./app.js"></script>
  </head>
  <body>
    <h1>My Website</h1>
    <div id="app"></div>
  </body>
</html>
```

**Why this works:**

- `analytics.js` is independent, so async is fine
- `utils.js`, `framework.js`, and `app.js` depend on each other
- Defer makes sure they run in order after HTML is done

**Quick Summary Table**

| Feature                  | Default          | Async                    | Defer        |
| ------------------------ | ---------------- | ------------------------ | ------------ |
| Blocks HTML Parsing      | ✓ Yes            | ✓ Briefly (on execution) | ✗ No         |
| Fetches in Parallel      | ✗ No             | ✓ Yes                    | ✓ Yes        |
| Maintains Order          | ✓ Yes            | ✗ No                     | ✓ Yes        |
| Executes After HTML Done | ✗ No             | ✗ No                     | ✓ Yes        |
| Best For                 | Critical scripts | Independent scripts      | Most scripts |

**Common Mistakes**

**Mistake 1: Using async when scripts depend on each other**

```html
<!-- ✗ Wrong - app.js might run before utils.js! -->
<script async src="./utils.js"></script>
<script async src="./app.js"></script>

<!-- ✓ Correct - guaranteed order -->
<script defer src="./utils.js"></script>
<script defer src="./app.js"></script>
```

**Mistake 2: Using both async and defer together**

```html
<!-- ✗ Wrong - async takes priority, defer is ignored -->
<script async defer src="./script.js"></script>

<!-- ✓ Just use one -->
<script defer src="./script.js"></script>
```

**Mistake 3: Using async/defer with inline scripts**

```html
<!-- ✗ Wrong - async/defer only works with external scripts -->
<script async>
  console.log("This is inline");
</script>

<!-- ✓ Correct - use with src attribute -->
<script async src="./script.js"></script>
```

**Key Takeaways**

1. **Default (no attribute)** - Stops HTML parsing to fetch and execute script

2. **Async** - Fetches in parallel, executes as soon as fetched, doesn't guarantee order

3. **Defer** - Fetches in parallel, executes after HTML is fully parsed, maintains order

4. **Defer is better for most cases** - Especially when scripts depend on each other

5. **Async is for independent scripts** - Like analytics or chat widgets

6. **Both async and defer** only work with external scripts (with `src` attribute)

7. **Use defer by default** - Switch to async only when you're sure the script is independent

- ![async-differ](/js-basics-assets/async-differ.png)

---

## Debounce vs Throttling

This is the key difference you need to understand:

**Debounce:** Waits until events STOP for a certain time, then executes once

```
Events:    |||||||||         (user stops)
Debounce:                |--delay--|Execute!
                                    ↑
                         (only after stopping)
```

**Throttle:** Executes at regular intervals while events are happening

```
Events:    ||||||||||||||||||||||||||||||||||||
Throttle:  |Execute|     |Execute|     |Execute|
           ←delay→       ←delay→       ←delay→
           ↑             ↑             ↑
    (executes periodically while events continue)
```

**Simple analogy:**

**Debounce = Elevator door**

- Door waits for people to stop entering
- Only closes after no one has entered for a few seconds
- If someone enters, timer resets

**Throttle = Traffic light**

- Lets cars through at fixed intervals
- Every 30 seconds, regardless of how many cars are waiting
- Doesn't wait for cars to stop coming

**How Throttling Works**

Let's trace through a throttle with 300ms delay:

```
Time 0ms:
  User triggers event
  → flag = true
  → Function EXECUTES
  → flag = false
  → Timer starts (300ms)

Time 50ms:
  User triggers event
  → flag = false
  → Function IGNORED (not executed)

Time 100ms:
  User triggers event
  → flag = false
  → Function IGNORED

Time 200ms:
  User triggers event
  → flag = false
  → Function IGNORED

Time 300ms:
  Timer completes
  → flag = true (ready for next execution)

Time 350ms:
  User triggers event
  → flag = true
  → Function EXECUTES
  → flag = false
  → Timer starts again (300ms)
```

**Visual Flow:**

```
Events:     |  |  |  |  |  |  |  |  |  |  |  |  |
            ↓     ↓     ↓     ↓     ↓     ↓
Executed:   ✓     ✗     ✗     ✓     ✗     ✓
            |←--300ms-->|     |←--300ms-->|
```

Only the events at the start of each 300ms window execute. All others are ignored.

**JavaScript Implementation throttle**

```javascript
function throttle(fn, delay = 300) {
  let flag = true;

  return function (...args) {
    // If flag is false, we're in cooldown period
    if (!flag) {
      return; // Ignore this call
    }

    // Execute the function
    fn.apply(this, args);

    // Enter cooldown period
    flag = false;

    // After delay, exit cooldown period
    setTimeout(() => {
      flag = true;
    }, delay);
  };
}
```

**JavaScript Implementation Debounce**

```javascript
function getData() {
  let inputValue = document.getElementById("input").value;

  console.log("Fetching data...", inputValue);
}

function debounce(fn, delay = 300) {
  let timeout;
  return function () {
    clearTimeout(timeout);

    timeout = setTimeout(() => {
      fn.apply(this, arguments);
    }, delay);
  };
}

let debouncedFn = debounce(getData, 300);
```

**Breaking down the throttle code:**

**1. `let flag = true`:**

- Acts like a gate
- `true` = gate open (function can execute)
- `false` = gate closed (function calls ignored)

**2. `if (!flag) return`:**

- If we're in cooldown period (flag is false)
- Ignore this function call
- This is what makes it "throttle"

**3. `fn.apply(this, args)`:**

- Execute the actual function
- Pass through the correct context and arguments

**4. `flag = false`:**

- Close the gate
- Start cooldown period
- Ignore all calls until timer completes

**5. `setTimeout(() => { flag = true }, delay)`:**

- After the delay, open the gate again
- Allow the next function call to execute

**Using the Throttle Function**

```javascript
let count = 0;

function handleResize() {
  console.log(`Resize event occurred: ${count++}`);
}

// Create throttled version
let throttledResize = throttle(handleResize, 300);

// Use throttled version in event listener
window.addEventListener("resize", throttledResize);
```

**What happens when you resize the window:**

```
Without throttle:
  Resize event occurred: 0
  Resize event occurred: 1
  Resize event occurred: 2
  ... (hundreds of times)
  Resize event occurred: 347

With throttle (300ms):
  Resize event occurred: 0
  (300ms passes)
  Resize event occurred: 1
  (300ms passes)
  Resize event occurred: 2
  ... (only a few times)
```

**Real-World Examples**

**Example 1: Window Resize**

```javascript
function updateLayout() {
  console.log("Recalculating layout...");
  // Expensive layout calculations
  document.getElementById("width").textContent = window.innerWidth;
  document.getElementById("height").textContent = window.innerHeight;
}

let throttledLayout = throttle(updateLayout, 200);
window.addEventListener("resize", throttledLayout);
```

**Why throttle here?**

- Resize fires hundreds of times
- Layout calculations are expensive
- We don't need to update every single millisecond
- Once every 200ms is enough for smooth updates

**Example 2: Scroll Event**

```javascript
function checkScrollPosition() {
  const scrollPercent = (window.scrollY / document.body.scrollHeight) * 100;
  console.log(`Scrolled: ${scrollPercent.toFixed(1)}%`);

  // Update progress bar
  document.getElementById("progress").style.width = scrollPercent + "%";
}

let throttledScroll = throttle(checkScrollPosition, 100);
window.addEventListener("scroll", throttledScroll);
```

**Why throttle here?**

- Scroll events fire constantly while scrolling
- Updating progress bar every time is overkill
- Once every 100ms gives smooth visual feedback
- Saves CPU and prevents jank

**Example 3: Shooting Game**

```javascript
function shoot() {
  console.log("Bang! Bullet fired");
  // Create bullet element
  // Play sound effect
  // Handle game logic
}

// Limit shooting to once every 500ms (fire rate)
let throttledShoot = throttle(shoot, 500);

document.addEventListener("click", throttledShoot);
```

**Why throttle here?**

- Player might click rapidly
- We want to limit fire rate
- Creates game balance
- Prevents spam clicking

**Example 4: API Rate Limiting**

```javascript
function saveData(data) {
  console.log("Saving:", data);
  fetch("/api/save", {
    method: "POST",
    body: JSON.stringify(data),
  });
}

// Limit to one save per 2 seconds
let throttledSave = throttle(saveData, 2000);

// Auto-save on every change
document.getElementById("editor").addEventListener("input", function () {
  throttledSave(this.value);
});
```

**Why throttle here?**

- User might type constantly
- Don't want to spam the server
- API might have rate limits
- Saves bandwidth

**When to Use Debounce vs Throttle**

**Use Debounce when:**

- You want to wait until the user is DONE
- Execute only after activity stops
- Examples:
  - Search input (wait until done typing)
  - Form validation (validate after done typing)
  - Autosave (save after done editing)

**Use Throttle when:**

- You want to limit execution rate DURING activity
- Execute periodically while activity continues
- Examples:
  - Window resize (update layout while resizing)
  - Scroll events (update position while scrolling)
  - Mouse movement (track cursor while moving)
  - Game controls (limit action rate)

**Visual Comparison**

**Debounce - Search Input:**

```
User types: H e l l o
Events:     | | | | |        (user stops)
Debounce:               |--300ms--|Execute "Hello"
                                  ↑
                        (only after stopping)
```

**Throttle - Scroll Event:**

```
User scrolls: ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
Events:       |||||||||||||||||||
Throttle:     |Execute|  |Execute|  |Execute|
              ←200ms→    ←200ms→    ←200ms→
              ↑          ↑          ↑
     (executes periodically while scrolling)
```

**Different Throttle Intervals**

The delay value changes how often the function executes:

```javascript
// Very frequent updates (smooth but more CPU)
let throttled = throttle(fn, 50); // Every 50ms

// Balanced (good for most cases)
let throttled = throttle(fn, 100); // Every 100ms
let throttled = throttle(fn, 200); // Every 200ms

// Less frequent updates (less CPU, might feel choppy)
let throttled = throttle(fn, 500); // Every 500ms
let throttled = throttle(fn, 1000); // Every 1 second
```

**Common Mistakes**

**Mistake 1: Creating throttle inside event handler**

```javascript
// ✗ Wrong - creates new throttle every time!
window.addEventListener("resize", function () {
  throttle(handleResize, 300)(); // New throttle each time!
});

// ✓ Correct - create throttle ONCE
let throttledResize = throttle(handleResize, 300);
window.addEventListener("resize", throttledResize);
```

**Mistake 2: Using debounce when throttle is needed**

```javascript
// ✗ Wrong - won't update until user STOPS scrolling
let debouncedScroll = debounce(updateScrollPosition, 300);
window.addEventListener("scroll", debouncedScroll);

// ✓ Correct - updates WHILE scrolling (periodically)
let throttledScroll = throttle(updateScrollPosition, 300);
window.addEventListener("scroll", throttledScroll);
```

**Mistake 3: Using throttle when debounce is needed**

```javascript
// ✗ Wrong - will make API calls every 300ms while typing
let throttledSearch = throttle(searchAPI, 300);
input.addEventListener("input", throttledSearch);

// ✓ Correct - waits until user stops typing
let debouncedSearch = debounce(searchAPI, 300);
input.addEventListener("input", debouncedSearch);
```

**Quick Decision Guide**

Ask yourself: "Do I want the function to execute..."

**WHILE the event is happening?** → Use **Throttle**

- Window resize
- Scrolling
- Mouse movement
- Game controls

**AFTER the event stops?** → Use **Debounce**

- Search input
- Form validation
- Text editor autosave
- Window resize (if you only care about final size)

**Summary Table**

| Feature      | Debounce             | Throttle                     |
| ------------ | -------------------- | ---------------------------- |
| Executes     | After events stop    | During events (periodically) |
| Timing       | Resets on each event | Fixed intervals              |
| Use case     | Wait for completion  | Limit rate                   |
| Example      | Search input         | Scroll handler               |
| Mental model | "Wait until done"    | "Once per interval"          |

**Key Takeaways**

1. **Throttling limits execution rate** to once per interval

2. **Key difference from debounce:**
   - Throttle: Executes periodically WHILE events happen
   - Debounce: Executes AFTER events stop

3. **Implementation uses a flag:**
   - `flag = true` → function can execute
   - `flag = false` → ignore calls (cooldown)
   - Timer resets flag after delay

4. **Common use cases:**
   - Window resize
   - Scroll events
   - Mouse movement
   - Game controls (fire rate)

5. **Choose the right interval:**
   - 50-100ms for smooth updates
   - 200-300ms for balanced performance
   - 500ms+ for less critical updates

6. **Both are useful** - choose based on your specific needs

---

## Event Delegation in JavaScript

Understanding a powerful technique for improving performance when working with multiple elements.

**What is Event Delegation?**

Event delegation is a technique where instead of adding event listeners to multiple child elements, you add a single event listener to their parent element. The parent then handles events from all its children.

**The Problem Without Event Delegation**

Imagine you have a long list of items, and you want to add click handlers to each one:

```html
<ul>
  <li>React.js</li>
  <li>Next.js</li>
  <li>Node.js</li>
  <li>Angular</li>
  <li>jQuery</li>
  <!-- ... 100 more items ... -->
</ul>
```

**Bad approach (without delegation):**

```javascript
// ✗ Bad - Adding listener to each item individually
const items = document.querySelectorAll("li");

items.forEach((item) => {
  item.addEventListener("click", function () {
    console.log("Clicked:", this.textContent);
  });
});

// Problems:
// 1. 100+ event listeners = high memory usage
// 2. Slow performance for large lists
// 3. New items added later won't have listeners
```

**Why is this bad?**

If you have 100 list items:

- 100 separate event listeners are created
- Each listener takes up memory
- If you add new items dynamically, you need to attach listeners again
- More listeners = slower performance

**The Solution: Event Delegation**

Instead of adding listeners to all children, add ONE listener to the parent:

```javascript
// ✓ Good - Single listener on parent
const list = document.querySelector("ul");

list.addEventListener("click", function (event) {
  if (event.target.tagName === "LI") {
    console.log("Clicked:", event.target.textContent);
  }
});

// Benefits:
// 1. Only 1 event listener = less memory
// 2. Better performance
// 3. Automatically works with new items added later!
```

**How Does Event Delegation Work?**

It works because of **event bubbling**. When you click a child element, the event doesn't just happen on that element - it "bubbles up" through all parent elements.

**Visual representation:**

```html
<ul>
  ← Event bubbles up here (parent)
  <li>← You click here (child) Text</li>
</ul>
```

**Bubbling flow:**

```
User clicks <li>
    ↓
Event fires on <li>
    ↓
Event bubbles to <ul>
    ↓
<ul>'s listener catches it
    ↓
We check what was clicked using event.target
```

**Understanding event.target vs event.currentTarget**

These two properties are often confused. Here's the difference:

- **event.target** - The element that was actually clicked (child)
- **event.currentTarget** - The element that has the event listener (parent)

```html
<ul id="list">
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
```

```javascript
document.getElementById("list").addEventListener("click", function (event) {
  console.log("target:", event.target); // <li>Item 1</li>
  console.log("currentTarget:", event.currentTarget); // <ul id="list">
});
```

**Visual explanation:**

```
Click happens here → <li>Item 1</li> ← event.target (what you clicked)
                            ↓
                     Bubbles up to
                            ↓
Listener is here → <ul> ← event.currentTarget (where listener is attached)
```

**Complete Example**

```html
<ul onclick="handleClick(event)">
  <li data-id="react">React.js</li>
  <li data-id="next">Next.js</li>
  <li data-id="node">Node.js</li>
  <li data-id="angular">Angular</li>
  <li data-id="jquery">jQuery</li>
  <li data-id="vue">Vue.js</li>
  <li data-id="preact">Preact</li>
  <li data-id="svelte">Svelte</li>
  <li data-id="nuxt">Nuxt.js</li>
  <li data-id="remix">Remix</li>
</ul>
```

```javascript
function handleClick(event) {
  console.log("Clicked element:", event.target);
  // <li data-id="react">React.js</li>

  console.log("Parent element:", event.currentTarget);
  // <ul>...</ul>

  // Common use case: Get data from clicked element
  console.log("ID:", event.target.dataset.id);
  // "react"

  // Alternative way to get data attribute
  console.log("ID:", event.target.getAttribute("data-id"));
  // "react"
}
```

**Breaking down the example:**

**1. Single event listener on parent:**

```html
<ul onclick="handleClick(event)"></ul>
```

Only ONE listener for the entire list!

**2. event.target - What was clicked:**

```javascript
console.log(event.target);
// The specific <li> element that was clicked
```

**3. event.currentTarget - Where the listener is:**

```javascript
console.log(event.currentTarget);
// The <ul> element (parent with the listener)
```

**4. Accessing data attributes:**

```javascript
// Method 1: Using dataset property
event.target.dataset.id; // "react"

// Method 2: Using getAttribute
event.target.getAttribute("data-id"); // "react"
```

**Real-World Example 1: Todo List**

```html
<ul id="todoList">
  <li data-id="1">
    <span>Buy groceries</span>
    <button class="delete">Delete</button>
  </li>
  <li data-id="2">
    <span>Walk dog</span>
    <button class="delete">Delete</button>
  </li>
  <li data-id="3">
    <span>Study JavaScript</span>
    <button class="delete">Delete</button>
  </li>
</ul>
```

```javascript
document.getElementById("todoList").addEventListener("click", function (event) {
  // Check if delete button was clicked
  if (event.target.classList.contains("delete")) {
    const listItem = event.target.closest("li");
    const todoId = listItem.dataset.id;

    console.log("Deleting todo:", todoId);
    listItem.remove();
  }

  // Check if the todo text was clicked
  if (event.target.tagName === "SPAN") {
    console.log("You clicked:", event.target.textContent);
  }
});
```

**Why this is powerful:**

- ONE event listener handles all todos and buttons
- Works automatically with new todos added later
- No need to attach/detach listeners when adding/removing items

**Real-World Example 2: Image Gallery**

```html
<div id="gallery">
  <img src="cat1.jpg" data-full="cat1-large.jpg" alt="Cat 1" />
  <img src="cat2.jpg" data-full="cat2-large.jpg" alt="Cat 2" />
  <img src="cat3.jpg" data-full="cat3-large.jpg" alt="Cat 3" />
  <!-- 100 more images... -->
</div>
```

```javascript
document.getElementById("gallery").addEventListener("click", function (event) {
  if (event.target.tagName === "IMG") {
    const fullSizeUrl = event.target.dataset.full;
    openLightbox(fullSizeUrl);
  }
});

function openLightbox(url) {
  console.log("Opening image:", url);
  // Show full-size image in lightbox
}
```

**Benefits:**

- Only 1 listener for 100+ images
- Much better performance
- New images work automatically

**Real-World Example 3: Dynamic Content**

```html
<div id="container">
  <button class="action" data-action="save">Save</button>
  <button class="action" data-action="delete">Delete</button>
</div>

<button id="addButton">Add New Button</button>
```

```javascript
// Event delegation on container
document
  .getElementById("container")
  .addEventListener("click", function (event) {
    if (event.target.classList.contains("action")) {
      const action = event.target.dataset.action;
      console.log("Action:", action);
    }
  });

// Add new buttons dynamically
document.getElementById("addButton").addEventListener("click", function () {
  const newButton = document.createElement("button");
  newButton.className = "action";
  newButton.dataset.action = "share";
  newButton.textContent = "Share";

  document.getElementById("container").appendChild(newButton);
  // New button automatically works with event delegation!
});
```

**Why this is amazing:**

- Dynamically added buttons work without extra setup
- No need to attach listeners to new elements
- Clean and maintainable code

**Checking Which Element Was Clicked**

You often need to verify what specific element was clicked:

```javascript
list.addEventListener("click", function (event) {
  const clicked = event.target;

  // Method 1: Check tag name
  if (clicked.tagName === "LI") {
    console.log("A list item was clicked");
  }

  // Method 2: Check class
  if (clicked.classList.contains("special")) {
    console.log("A special item was clicked");
  }

  // Method 3: Check data attribute
  if (clicked.dataset.type === "product") {
    console.log("A product was clicked");
  }

  // Method 4: Use closest() to find parent
  const listItem = clicked.closest("li");
  if (listItem) {
    console.log("Clicked something inside an LI");
  }
});
```

**Using closest() for Complex Structures**

Sometimes you click on a child element inside your target:

```html
<ul id="list">
  <li>
    <img src="icon.png" />
    <span>Item text</span>
    <button>Delete</button>
  </li>
</ul>
```

If you click the `<img>`, `event.target` is the `<img>`, not the `<li>`. Use `closest()` to find the parent:

```javascript
document.getElementById("list").addEventListener("click", function (event) {
  // Find the closest <li> parent
  const listItem = event.target.closest("li");

  if (listItem) {
    console.log("You clicked somewhere in this item:", listItem);
  }
});
```

**Advantages of Event Delegation**

1. **Better Performance**
   - Fewer event listeners = less memory
   - Faster setup time for long lists

2. **Works with Dynamic Content**
   - New elements automatically get the functionality
   - No need to reattach listeners

3. **Cleaner Code**
   - One listener instead of hundreds
   - Easier to maintain

4. **Less Memory Usage**
   - Important for mobile devices
   - Scales better with large lists

**When to Use Event Delegation**

✅ **Use event delegation when:**

- You have many similar elements (list items, buttons, cards)
- Elements are added/removed dynamically
- You want better performance
- Elements share the same functionality

❌ **Don't use event delegation when:**

- You only have one or two elements
- Each element needs very different behavior
- The performance benefit isn't worth the complexity

**Common Mistakes**

**Mistake 1: Not checking what was clicked**

```javascript
// ✗ Wrong - assumes everything clicked is an LI
list.addEventListener("click", function (event) {
  console.log(event.target.textContent);
  // What if user clicks the UL itself?
});

// ✓ Correct - check first
list.addEventListener("click", function (event) {
  if (event.target.tagName === "LI") {
    console.log(event.target.textContent);
  }
});
```

**Mistake 2: Confusing target and currentTarget**

```javascript
// ✗ Wrong - currentTarget is always the parent
list.addEventListener("click", function (event) {
  console.log(event.currentTarget.textContent);
  // Always logs the entire list content!
});

// ✓ Correct - use target for the clicked element
list.addEventListener("click", function (event) {
  console.log(event.target.textContent);
  // Logs the clicked item's content
});
```

**Mistake 3: Not using stopPropagation carefully**

```javascript
// ✗ Can cause issues - stops delegation from working
listItem.addEventListener("click", function (event) {
  event.stopPropagation(); // Prevents bubbling!
  // Parent's delegated listener won't fire
});
```

**Key Takeaways**

1. **Event delegation = one listener on parent** instead of many on children

2. **Works because of event bubbling** - events travel up the DOM tree

3. **event.target** - what was clicked (child)
   **event.currentTarget** - where listener is attached (parent)

4. **Access data attributes** using:
   - `event.target.dataset.id`
   - `event.target.getAttribute("data-id")`

5. **Always check what was clicked** before acting on it

6. **Use closest()** to find parent elements when needed

7. **Main benefits:**
   - Better performance
   - Less memory
   - Works with dynamic content

---

## Prototype Inheritance in JavaScript

Understanding how objects inherit properties and methods from other objects in JavaScript.

**What is Prototype Inheritance?**

Prototype inheritance is a mechanism in JavaScript that allows objects to inherit properties and methods from other objects.

Unlike classical inheritance (like in Java or C++), JavaScript uses prototypes - objects can directly inherit from other objects.

**Simple Analogy:**

Think of it like a family tree:

- You inherit features from your parents
- Your parents inherited from their parents
- This forms a chain going back generations

In JavaScript:

- Objects inherit from other objects
- Those objects inherit from their prototypes
- This forms a **prototype chain**

**The Hidden [[Prototype]] Property**

Every object in JavaScript has a hidden property called `[[Prototype]]`. This property points to another object (or `null`).

**How to access it:**

```javascript
// Method 1: __proto__ (older way, but commonly used)
console.log(obj.__proto__);

// Method 2: Object.getPrototypeOf() (recommended)
console.log(Object.getPrototypeOf(obj));
```

**Note:** While `__proto__` is widely supported, `Object.getPrototypeOf()` is the official way to access the prototype.

**Simple Example**

```javascript
const animal = {
  eat: true,
  sleep: function () {
    console.log("Sleeping...");
  },
};

const rabbit = {
  run: true,
};

// Set animal as rabbit's prototype
rabbit.__proto__ = animal;

console.log(rabbit.run); // true (rabbit's own property)
console.log(rabbit.eat); // true (inherited from animal)
rabbit.sleep(); // "Sleeping..." (inherited method)
```

**What's happening here:**

```
rabbit object
  ├─ run: true (own property)
  └─ [[Prototype]] → animal object
                      ├─ eat: true
                      └─ sleep: function
```

**The Prototype Chain**

Objects can inherit from objects, which inherit from other objects, forming a chain:

```javascript
const livingBeing = {
  alive: true,
};

const animal = {
  eat: true,
};

const rabbit = {
  run: true,
};

// Create a chain
animal.__proto__ = livingBeing;
rabbit.__proto__ = animal;

console.log(rabbit.run); // true (own property)
console.log(rabbit.eat); // true (from animal)
console.log(rabbit.alive); // true (from livingBeing)
```

**Visual representation:**

```
rabbit
  ├─ run: true
  └─ [[Prototype]] → animal
                      ├─ eat: true
                      └─ [[Prototype]] → livingBeing
                                          ├─ alive: true
                                          └─ [[Prototype]] → Object.prototype
                                                              └─ [[Prototype]] → null
```

The chain ends when it reaches `null`.

**Object.create() Method**

The recommended way to set up prototype inheritance is using `Object.create()`:

```javascript
const animal = {
  eat: true,
  makeSound: function () {
    console.log("Some sound");
  },
};

// Create rabbit with animal as its prototype
const rabbit = Object.create(animal);
rabbit.run = true;

console.log(rabbit.run); // true (own property)
console.log(rabbit.eat); // true (inherited)
rabbit.makeSound(); // "Some sound" (inherited)
```

**What Object.create() does:**

```javascript
// This:
const rabbit = Object.create(animal);

// Is similar to:
const rabbit = {};
rabbit.__proto__ = animal;
```

But `Object.create()` is cleaner and recommended.

**Constructor Functions and Prototypes**

When you use constructor functions with `new`, JavaScript automatically sets up the prototype:

```javascript
function Animal(name) {
  this.name = name;
}

// Add methods to the prototype
Animal.prototype.eat = function () {
  console.log(`${this.name} is eating`);
};

Animal.prototype.sleep = function () {
  console.log(`${this.name} is sleeping`);
};

// Create instances
const dog = new Animal("Dog");
const cat = new Animal("Cat");

dog.eat(); // "Dog is eating"
cat.sleep(); // "Cat is sleeping"
```

**What happens with `new`:**

```javascript
const dog = new Animal("Dog");

// Behind the scenes:
// 1. Create a new empty object: {}
// 2. Set its [[Prototype]] to Animal.prototype
// 3. Call Animal() with 'this' pointing to the new object
// 4. Return the new object
```

**Visual representation:**

```
dog
  ├─ name: "Dog"
  └─ [[Prototype]] → Animal.prototype
                      ├─ eat: function
                      ├─ sleep: function
                      └─ [[Prototype]] → Object.prototype
```

**Classes and Prototypes**

ES6 classes for the most part are just syntactic sugar over constructor functions and prototypes:

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  eat() {
    console.log(`${this.name} is eating`);
  }

  sleep() {
    console.log(`${this.name} is sleeping`);
  }
}

const dog = new Animal("Dog");
dog.eat(); // "Dog is eating"

// Under the hood, it still uses prototypes!
console.log(dog.__proto__ === Animal.prototype); // true
```

**Why Built-in Methods Work**

This is why arrays have methods like `map()`, `filter()`, strings have `includes()`, etc.

```javascript
const arr = [1, 2, 3];

// What JavaScript does internally:
// const arr = new Array(1, 2, 3);

// arr's prototype chain:
// arr → Array.prototype (has map, filter, etc.) → Object.prototype → null

arr.map((x) => x * 2); // Works because of Array.prototype.map
```

**Visual representation:**

```
arr = [1, 2, 3]
  └─ [[Prototype]] → Array.prototype
                      ├─ map: function
                      ├─ filter: function
                      ├─ reduce: function
                      └─ [[Prototype]] → Object.prototype
                                          ├─ toString: function
                                          ├─ hasOwnProperty: function
                                          └─ [[Prototype]] → null
```

**Same for strings:**

```javascript
const str = "hello";

// Internally: new String("hello")

str.toUpperCase(); // Works because of String.prototype.toUpperCase
str.includes("ell"); // Works because of String.prototype.includes
```

**Property Lookup Process**

When you access a property on an object, JavaScript searches in this order:

**Step 1:** Check the object itself
**Step 2:** Check the object's prototype
**Step 3:** Check the prototype's prototype
**Step 4:** Continue until property is found or reach `null`

```javascript
const animal = {
  eat: true,
};

const rabbit = Object.create(animal);
rabbit.run = true;

// Looking up rabbit.run:
console.log(rabbit.run);
// Step 1: Check rabbit itself → Found! Return true

// Looking up rabbit.eat:
console.log(rabbit.eat);
// Step 1: Check rabbit itself → Not found
// Step 2: Check rabbit's prototype (animal) → Found! Return true

// Looking up rabbit.fly:
console.log(rabbit.fly);
// Step 1: Check rabbit itself → Not found
// Step 2: Check animal → Not found
// Step 3: Check Object.prototype → Not found
// Step 4: Reach null → Return undefined
```

**Visual flow:**

```
rabbit.eat
    ↓
Check rabbit? No
    ↓
Check animal? Yes! → return true

rabbit.fly
    ↓
Check rabbit? No
    ↓
Check animal? No
    ↓
Check Object.prototype? No
    ↓
Reached null → return undefined
```

**Complete Example with Prototype Chain**

```javascript
const animal = {
  eat: true,
  walk: function () {
    console.log("Animal walks");
  },
};

// Create rabbit inheriting from animal
const rabbit = Object.create(animal);
rabbit.run = true;
rabbit.hop = function () {
  console.log("Rabbit hops");
};

// Create whiteRabbit inheriting from rabbit
const whiteRabbit = Object.create(rabbit);
whiteRabbit.color = "white";

// Property lookups:
console.log(whiteRabbit.color); // "white" (own property)
console.log(whiteRabbit.run); // true (from rabbit)
console.log(whiteRabbit.eat); // true (from animal)

whiteRabbit.hop(); // "Rabbit hops" (from rabbit)
whiteRabbit.walk(); // "Animal walks" (from animal)
```

**Prototype chain:**

```
whiteRabbit
  ├─ color: "white"
  └─ [[Prototype]] → rabbit
                      ├─ run: true
                      ├─ hop: function
                      └─ [[Prototype]] → animal
                                          ├─ eat: true
                                          ├─ walk: function
                                          └─ [[Prototype]] → Object.prototype
                                                              └─ [[Prototype]] → null
```

**Checking Properties**

You can check if a property belongs to the object itself or is inherited:

```javascript
const animal = {
  eat: true,
};

const rabbit = Object.create(animal);
rabbit.run = true;

// Check if property exists (including inherited)
console.log("run" in rabbit); // true
console.log("eat" in rabbit); // true

// Check if property is own (not inherited)
console.log(rabbit.hasOwnProperty("run")); // true
console.log(rabbit.hasOwnProperty("eat")); // false (inherited)
```

**Modifying Prototypes**

You can add properties to prototypes dynamically:

```javascript
function Animal(name) {
  this.name = name;
}

const dog = new Animal("Dog");
const cat = new Animal("Cat");

// Add method to prototype (affects all instances!)
Animal.prototype.makeSound = function () {
  console.log(`${this.name} makes a sound`);
};

dog.makeSound(); // "Dog makes a sound"
cat.makeSound(); // "Cat makes a sound"
// Both instances get the new method!
```

**Why is this powerful?**

Adding methods to the prototype means:

- All instances share the same method (memory efficient)
- New instances automatically get the method
- You can extend built-in objects (though not recommended)

**Common Patterns**

**Pattern 1: Inheritance with Constructor Functions**

```javascript
function Animal(name) {
  this.name = name;
}

Animal.prototype.eat = function () {
  console.log(`${this.name} is eating`);
};

function Dog(name, breed) {
  Animal.call(this, name); // Call parent constructor
  this.breed = breed;
}

// Set up inheritance
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.bark = function () {
  console.log("Woof!");
};

const myDog = new Dog("Rex", "Labrador");
myDog.eat(); // "Rex is eating" (inherited)
myDog.bark(); // "Woof!" (own method)
```

**Pattern 2: Inheritance with Classes (ES6+)**

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  eat() {
    console.log(`${this.name} is eating`);
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name); // Call parent constructor
    this.breed = breed;
  }

  bark() {
    console.log("Woof!");
  }
}

const myDog = new Dog("Rex", "Labrador");
myDog.eat(); // "Rex is eating"
myDog.bark(); // "Woof!"
```

**Common Mistakes**

**Mistake 1: Modifying prototype after creating instances**

```javascript
function Animal(name) {
  this.name = name;
}

const dog = new Animal("Dog");

// ✗ This won't work as expected
dog.prototype.eat = function () {
  console.log("Eating");
};

// ✓ Modify the constructor's prototype
Animal.prototype.eat = function () {
  console.log("Eating");
};
```

**Mistake 2: Overwriting prototype instead of extending it**

```javascript
function Animal(name) {
  this.name = name;
}

// ✗ Wrong - loses constructor reference
Animal.prototype = {
  eat: function () {},
};

// ✓ Correct - add to existing prototype
Animal.prototype.eat = function () {};
```

**Key Takeaways**

1. **Prototype inheritance** allows objects to inherit from other objects

2. **Every object has [[Prototype]]** accessible via `__proto__` or `Object.getPrototypeOf()`

3. **Prototype chain** is formed when objects inherit from other objects

4. **Property lookup** searches the object, then up the prototype chain

5. **Object.create()** is the recommended way to set up inheritance

6. **Constructor functions and classes** automatically set up prototypes

7. **Built-in methods** work because of prototypes (Array.prototype, String.prototype, etc.)

8. **Chain ends at null** - the final link in every prototype chain

---

# Generator Functions in JavaScript

Understanding functions that can pause and resume their execution.

**What are Generator Functions?**

Generator functions are special functions that can pause their execution and resume later from the exact same point where they paused.

Unlike normal functions that run from start to finish, generators can stop midway, return a value, and continue from where they stopped when called again.

**How to Create a Generator Function**

Add an asterisk (`*`) after the `function` keyword:
```javascript
// Normal function
function regularFunction() {
  return "Hello";
}

// Generator function (notice the *)
function* generatorFunction() {
  yield "Hello";
}
```

**The `yield` Keyword**

`yield` is a special keyword that:
1. Can only be used with generator function
2. Returns a value
3. Pauses the function at that point
4. Remembers where it paused

Think of `yield` like a pause button that also hands you something.

**The `next()` Method**

To execute a generator function step by step, use the `.next()` method:
```javascript
function* simpleGenerator() {
  yield 1;
  yield 2;
  yield 3;
}

const gen = simpleGenerator();

console.log(gen.next());  // { value: 1, done: false }
console.log(gen.next());  // { value: 2, done: false }
console.log(gen.next());  // { value: 3, done: false }
console.log(gen.next());  // { value: undefined, done: true }
```

**Understanding the Return Value**

Each `.next()` call returns an object with two properties:

- **value**: The value that was `yield`ed
- **done**: `true` if the generator is finished, `false` otherwise
```javascript
const result = gen.next();
console.log(result.value);  // The yielded value
console.log(result.done);   // Is the generator done?
```

**Simple Example: Counting**
```javascript
function* print() {
  yield 1;
  yield 2;
  yield 3;
}

const printValues = print();

console.log(printValues.next());  // { value: 1, done: false }
console.log(printValues.next());  // { value: 2, done: false }
console.log(printValues.next());  // { value: 3, done: false }
console.log(printValues.next());  // { value: undefined, done: true }
```

**Step-by-step execution:**
```
1. Create generator: const printValues = print()
   (Nothing executes yet!)

2. First next():
   → Executes until first yield
   → Returns { value: 1, done: false }
   → Pauses

3. Second next():
   → Resumes from where it paused
   → Executes until second yield
   → Returns { value: 2, done: false }
   → Pauses

4. Third next():
   → Resumes from where it paused
   → Executes until third yield
   → Returns { value: 3, done: false }
   → Pauses

5. Fourth next():
   → Resumes, but no more yields
   → Returns { value: undefined, done: true }
   → Generator is finished
```

**Visual Flow:**
```
function* print() {
    yield 1;     ← First next() stops here
    yield 2;     ← Second next() stops here
    yield 3;     ← Third next() stops here
}                ← Fourth next() reaches the end
```

**Real-World Example 1: ATM Flow**
```javascript
function* atmFlow() {
  yield "Please select your language";
  yield "Please select your account type";
  yield "Please enter the amount you want to withdraw";
  yield "Please enter your pin";
}

const atmSteps = atmFlow();

console.log(atmSteps.next().value);  // "Please select your language"
// User selects language...

console.log(atmSteps.next().value);  // "Please select your account type"
// User selects account type...

console.log(atmSteps.next().value);  // "Please enter the amount you want to withdraw"
// User enters amount...

console.log(atmSteps.next().value);  // "Please enter your pin"
// User enters pin...
```

**Why is this useful?**

Instead of showing all steps at once, the ATM shows one step at a time, waiting for user input before moving to the next step. This is perfect for generators!

**Real-World Example 2: ID Generator**
```javascript
function* idGenerator() {
  let id = 0;
  
  while (true) {  // Infinite loop!
    yield id;
    id++;
  }
}

const generateId = idGenerator();

console.log(generateId.next().value);  // 0
console.log(generateId.next().value);  // 1
console.log(generateId.next().value);  // 2
console.log(generateId.next().value);  // 3
// Can keep calling forever!
```

**Why doesn't the infinite loop crash?**

Because the generator pauses at each `yield`! It only continues when you call `.next()` again.

**How it works:**
```
Call 1: next()
  → id = 0
  → yield 0 (pause here)
  → Returns { value: 0, done: false }

Call 2: next()
  → Resume from pause
  → id++ → id = 1
  → Loop again
  → yield 1 (pause here)
  → Returns { value: 1, done: false }

And so on...
```

**Extracting Just the Value**

Instead of getting the whole object, you can get just the value:
```javascript
function* numbers() {
  yield 10;
  yield 20;
  yield 30;
}

const gen = numbers();

console.log(gen.next().value);  // 10
console.log(gen.next().value);  // 20
console.log(gen.next().value);  // 30
```

**Using Generators in Loops**

You can use `for...of` to automatically iterate through all yielded values:
```javascript
function* numbers() {
  yield 1;
  yield 2;
  yield 3;
}

for (const num of numbers()) {
  console.log(num);
}
// Output:
// 1
// 2
// 3
```

**How it works:**

`for...of` automatically calls `.next()` until `done` is `true`, and gives you just the values.

**Passing Values to Generators**

You can pass values into a generator using `.next(value)`:
```javascript
function* conversation() {
  const name = yield "What is your name?";
  const age = yield "What is your age?";
  return `${name} is ${age} years old`;
}

const chat = conversation();

console.log(chat.next().value);        // "What is your name?"
console.log(chat.next("John").value);  // "What is your age?"
console.log(chat.next(25).value);      // "John is 25 years old"
```

**Step by step:**
```
1. next()
   → Executes to first yield
   → Returns "What is your name?"

2. next("John")
   → Resumes, assigns "John" to name
   → Executes to second yield
   → Returns "What is your age?"

3. next(25)
   → Resumes, assigns 25 to age
   → Reaches return statement
   → Returns "John is 25 years old"
```

**Real-World Example 3: Pagination**
```javascript
function* paginate(items, pageSize) {
  for (let i = 0; i < items.length; i += pageSize) {
    yield items.slice(i, i + pageSize);
  }
}

const items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const pages = paginate(items, 3);

console.log(pages.next().value);  // [1, 2, 3]
console.log(pages.next().value);  // [4, 5, 6]
console.log(pages.next().value);  // [7, 8, 9]
console.log(pages.next().value);  // [10]
console.log(pages.next().value);  // undefined
```

**Real-World Example 4: Reading Large Files**
```javascript
function* readFileInChunks(fileContent, chunkSize) {
  let position = 0;
  
  while (position < fileContent.length) {
    yield fileContent.slice(position, position + chunkSize);
    position += chunkSize;
  }
}

const file = "This is a very long file content that we want to read in chunks...";
const reader = readFileInChunks(file, 10);

console.log(reader.next().value);  // "This is a "
console.log(reader.next().value);  // "very long "
console.log(reader.next().value);  // "file conte"
// And so on...
```

**Why use this?**

For large files, you don't load everything into memory at once. Process it chunk by chunk!

**Real-World Example 5: Task Queue**
```javascript
function* taskQueue() {
  yield "Connecting to database...";
  yield "Fetching user data...";
  yield "Processing data...";
  yield "Saving results...";
  yield "Sending notification...";
  return "All tasks completed!";
}

const tasks = taskQueue();

// Simulate async task processing
function processNextTask() {
  const task = tasks.next();
  
  if (!task.done) {
    console.log(task.value);
    // Wait 1 second, then process next task
    setTimeout(processNextTask, 1000);
  } else {
    console.log(task.value);
  }
}

processNextTask();

// Output (one per second):
// Connecting to database...
// Fetching user data...
// Processing data...
// Saving results...
// Sending notification...
// All tasks completed!
```

**Checking if Generator is Done**
```javascript
function* countdown() {
  yield 3;
  yield 2;
  yield 1;
}

const count = countdown();

let result = count.next();
while (!result.done) {
  console.log(result.value);
  result = count.next();
}

// Output:
// 3
// 2
// 1
```

**Generator Delegation with yield***

You can delegate to another generator using `yield*`:
```javascript
function* generator1() {
  yield 1;
  yield 2;
}

function* generator2() {
  yield "a";
  yield* generator1();  // Delegate to generator1
  yield "b";
}

for (const value of generator2()) {
  console.log(value);
}

// Output:
// a
// 1
// 2
// b
```

**When to Use Generators**

✅ **Use generators when:**
- You need step-by-step execution
- Working with large datasets (process chunk by chunk)
- Implementing custom iterators
- Creating infinite sequences
- Managing state machines
- Pagination or lazy loading

❌ **Don't use generators when:**
- Simple sequential operations (regular functions are fine)
- You need all values immediately
- The complexity isn't worth it

**Generators vs Regular Functions**

| Feature | Regular Function | Generator Function |
|---------|-----------------|-------------------|
| Syntax | `function name()` | `function* name()` |
| Execution | Runs to completion | Can pause and resume |
| Returns | Single value | Multiple values (via yield) |
| Control | No control after start | Full control with next() |
| Use case | Normal operations | Step-by-step execution |

**Common Mistakes**

**Mistake 1: Forgetting the asterisk**
```javascript
// ✗ Wrong - this is a regular function
function generatorFunction() {
  yield 1;  // SyntaxError!
}

// ✓ Correct
function* generatorFunction() {
  yield 1;
}
```

**Mistake 2: Calling generator like a regular function**
```javascript
function* numbers() {
  yield 1;
  yield 2;
}

// ✗ Wrong - doesn't execute anything
const result = numbers();
console.log(result);  // [object Generator] (not the values!)

// ✓ Correct - use next() to get values
const gen = numbers();
console.log(gen.next().value);  // 1
console.log(gen.next().value);  // 2
```

**Mistake 3: Expecting all values at once**
```javascript
function* numbers() {
  yield 1;
  yield 2;
  yield 3;
}

// ✗ Wrong - generators don't return arrays
const result = numbers();
console.log(result);  // [object Generator]

// ✓ Correct - iterate or call next()
for (const num of numbers()) {
  console.log(num);
}
```

**Key Takeaways**

1. **Generators are special functions** created with `function*`

2. **yield pauses execution** and returns a value

3. **next() resumes execution** from where it paused

4. **Returns an object** with `{ value, done }`

5. **Perfect for step-by-step execution** and lazy evaluation

6. **Can handle infinite sequences** because they're lazy

7. **Use for...of** to easily iterate through all values

8. **Can pass values in** using next(value)

---

## SOLID Principles in JavaScript

Understanding the five principles that help you write better, more maintainable code.

**What are SOLID Principles?**

SOLID is an acronym for five design principles that help developers write more maintainable, reusable, scalable, and modular code.

These principles were originally designed for object-oriented programming, but many concepts apply to JavaScript and functional programming too.

**The Five Principles:**

1. **S** - Single Responsibility Principle
2. **O** - Open/Closed Principle
3. **L** - Liskov Substitution Principle
4. **I** - Interface Segregation Principle
5. **D** - Dependency Inversion Principle

Let's explore each one with examples.

**1. Single Responsibility Principle (SRP)**

**Definition:** Each class (or function/component) should have only ONE reason to change. It should focus on doing ONE thing well.

**Important:** This doesn't mean one method or one property! It means one responsibility or one concern.

**Common misconception:**

❌ "One class should have only one method"
✓ "One class should have one responsibility, but can have multiple methods related to that responsibility"

**Example of ONE responsibility:**

A `User` class managing users can have:
- `addUser()`
- `editUser()`
- `deleteUser()`
- `getUser()`

All these methods relate to the SAME responsibility: **managing users**. That's still following SRP!

**Bad Example: Violating SRP**
```javascript
class Animal {
  walk() {
    console.log("I can walk");
  }

  eat() {
    console.log("I can eat");
  }

  fly() {
    console.log("I can fly");
  }
}

const dog = new Animal();
const eagle = new Animal();

dog.walk();  // ✓ Makes sense
dog.fly();   // ✗ Dogs can't fly!
```

**What's wrong here?**

The `Animal` class is trying to handle ALL animals, even though not all animals can fly. This violates SRP because:
- Some animals walk
- Some animals fly
- Some do both
- Trying to handle all cases in one class creates confusion

**Another bad example:**
```javascript
class User {
  walk() {
    console.log("User can walk");
  }

  talk() {
    console.log("User can talk");
  }

  eat() {
    console.log("User can eat");
  }

  sleep() {
    console.log("User can sleep");
  }

  cook() {
    console.log("User can cook");
  }
}
```

**What's wrong here?**

Not all users can cook! Only chefs or people who learned to cook can. By putting `cook()` in the base `User` class, we're saying EVERY user can cook, which isn't true.

**Good Example: Following SRP**
```javascript
class Animal {
  walk() {
    console.log("I can walk");
  }

  eat() {
    console.log("I can eat");
  }
}

class Bird extends Animal {
  fly() {
    console.log("I can fly");
  }
}

const dog = new Animal();
const eagle = new Bird();

dog.walk();   // ✓ Works
dog.eat();    // ✓ Works
// dog.fly(); // ✗ Not available - correct!

eagle.walk(); // ✓ Works (inherited)
eagle.eat();  // ✓ Works (inherited)
eagle.fly();  // ✓ Works
```

**Why is this better?**

- `Animal` class: Responsible for common animal behaviors (walk, eat)
- `Bird` class: Responsible for bird-specific behaviors (fly)
- Each class has a clear, single responsibility
- No confusion about what each animal can or cannot do

**Another good example:**
```javascript
class User {
  walk() {
    console.log("User can walk");
  }

  talk() {
    console.log("User can talk");
  }

  eat() {
    console.log("User can eat");
  }

  sleep() {
    console.log("User can sleep");
  }
}

class Chef extends User {
  cook() {
    console.log("Chef can cook");
  }
}

const regularUser = new User();
const chef = new Chef();

regularUser.walk();  // ✓ Works
// regularUser.cook(); // ✗ Not available - correct!

chef.walk();  // ✓ Works (inherited)
chef.cook();  // ✓ Works
```

**Why is this better?**

- `User` class: Handles basic user abilities
- `Chef` class: Adds cooking ability only to chefs
- Clear separation of concerns

**Visual Comparison:**

**Bad (violating SRP):**
```
Animal class
├─ walk()
├─ eat()
└─ fly() ← Problem: Not all animals fly!
```

**Good (following SRP):**
```
Animal class
├─ walk()
└─ eat()

Bird class (extends Animal)
├─ walk() (inherited)
├─ eat() (inherited)
└─ fly() ← Only birds fly!
```

**SRP in React Components**
```javascript
// ✗ Bad - Component does too many things
function UserDashboard() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  
  // Fetching data
  useEffect(() => {
    fetchUsers();
  }, []);
  
  // API call
  const fetchUsers = async () => {
    const response = await fetch('/api/users');
    const data = await response.json();
    setUsers(data);
  };
  
  // Validation logic
  const validateUser = (user) => {
    return user.email.includes('@');
  };
  
  // Rendering logic
  return (
    <div>
      {/* Complex rendering logic */}
    </div>
  );
}
```

**What's wrong?**

This component is responsible for:
1. Fetching data
2. Validating data
3. Rendering UI

Too many responsibilities!
```javascript
// ✓ Good - Separated concerns

// 1. API service (handles fetching)
const userService = {
  fetchUsers: async () => {
    const response = await fetch('/api/users');
    return response.json();
  }
};

// 2. Validation utility (handles validation)
const userValidator = {
  isValidEmail: (email) => email.includes('@')
};

// 3. Component (only handles rendering)
function UserDashboard() {
  const [users, setUsers] = useState([]);
  
  useEffect(() => {
    userService.fetchUsers().then(setUsers);
  }, []);
  
  return (
    <div>
      {users.map(user => (
        <UserCard key={user.id} user={user} />
      ))}
    </div>
  );
}
```

**Benefits of SRP:**

1. **Easier to understand** - Each class/function has one clear purpose
2. **Easier to test** - Test one thing at a time
3. **Easier to maintain** - Changes to one responsibility don't affect others
4. **More reusable** - Focused classes can be reused in different contexts
5. **Reduces bugs** - Less coupling means fewer unexpected side effects

**Real-World Example: User Management System**

**Bad approach:**
```javascript
class UserManager {
  createUser(data) {
    // Validate data
    if (!data.email.includes('@')) {
      throw new Error('Invalid email');
    }
    
    // Save to database
    database.save(data);
    
    // Send welcome email
    emailService.send(data.email, 'Welcome!');
    
    // Log activity
    logger.log('User created:', data.id);
    
    // Update analytics
    analytics.track('user_created');
  }
}
```

**Problems:**
- Handles validation
- Handles database operations
- Handles email sending
- Handles logging
- Handles analytics

One class, FIVE responsibilities!

**Good approach:**
```javascript
// 1. Validation service
class UserValidator {
  validate(data) {
    if (!data.email.includes('@')) {
      throw new Error('Invalid email');
    }
    return true;
  }
}

// 2. Database service
class UserRepository {
  save(data) {
    return database.save(data);
  }
}

// 3. Email service
class EmailService {
  sendWelcomeEmail(email) {
    return emailService.send(email, 'Welcome!');
  }
}

// 4. Logger service
class Logger {
  log(message) {
    logger.log(message);
  }
}

// 5. Analytics service
class Analytics {
  track(event) {
    analytics.track(event);
  }
}

// 6. User manager (coordinates other services)
class UserManager {
  constructor(validator, repository, emailService, logger, analytics) {
    this.validator = validator;
    this.repository = repository;
    this.emailService = emailService;
    this.logger = logger;
    this.analytics = analytics;
  }
  
  createUser(data) {
    this.validator.validate(data);
    const user = this.repository.save(data);
    this.emailService.sendWelcomeEmail(user.email);
    this.logger.log('User created:', user.id);
    this.analytics.track('user_created');
    return user;
  }
}
```

**Benefits:**
- Each class has ONE clear responsibility
- Easy to test each service independently
- Can reuse services in different contexts
- Can modify one service without affecting others

**How to Identify SRP Violations**

Ask yourself:

1. **"Can I describe this class in one sentence without using 'and'?"**
   - ✗ "This class manages users AND sends emails AND logs activities"
   - ✓ "This class manages users"

2. **"If I need to change X, do I need to change this class?"**
   - If multiple different reasons require changes, you're violating SRP

3. **"How many different teams might need to modify this class?"**
   - If multiple teams (frontend, backend, analytics) need to touch it, it probably has too many responsibilities

**Common Mistakes**

**Mistake 1: Confusing SRP with "one method per class"**
```javascript
// ✗ Wrong interpretation
class UserAdder {
  addUser(user) { /* ... */ }
}

class UserEditor {
  editUser(user) { /* ... */ }
}

class UserDeleter {
  deleteUser(userId) { /* ... */ }
}

// This is too granular!
```
```javascript
// ✓ Correct - One responsibility, multiple related methods
class UserManager {
  addUser(user) { /* ... */ }
  editUser(user) { /* ... */ }
  deleteUser(userId) { /* ... */ }
}

// All methods relate to the same responsibility: user management
```

**Mistake 2: Over-engineering**
```javascript
// ✗ Too much - simple functions don't always need classes
class Logger {
  log(message) {
    console.log(message);
  }
}

// ✓ Better - just use a function
function log(message) {
  console.log(message);
}
```

Don't over-apply SOLID. Use it where it makes sense!

**Key Takeaways**

1. **Single Responsibility = One reason to change**

2. **One responsibility can have multiple methods** related to that responsibility

3. **Example:** User management (add, edit, delete users) is ONE responsibility

4. **Benefits:** Easier to understand, test, maintain, and reuse

5. **Ask:** "What is this class/function responsible for?" If you say "and" multiple times, you're violating SRP

6. **Don't over-engineer** - Apply principles where they add value

7. **Applies to:** Classes, functions, components, and modules

---

**2.Open/Closed Principle (OCP)**

Understanding the second SOLID principle: Open for extension, closed for modification.

**What is the Open/Closed Principle?**

The Open/Closed Principle states that:
- **Open for extension** - You can add new functionality
- **Closed for modification** - You shouldn't modify existing code

In simple terms: When you need to add new features, you should be able to do so by adding new code, not by changing existing code.

**Why is this important?**

When you modify existing code:
- You might break things that already work
- You need to retest everything
- Other developers using your code might face issues
- Bugs can be introduced in previously working features

When you extend instead:
- Existing code remains unchanged and stable
- Less risk of breaking things
- Easier to add new features
- Old functionality continues to work as before

**Simple Analogy:**

Think of a power outlet:
- **Closed for modification**: The outlet stays the same
- **Open for extension**: You can plug in different devices without changing the outlet

You don't modify the outlet every time you want to use a new device. You just plug the new device in!

**Bad Example: Violating OCP**
```javascript
class Shape {
  constructor(type) {
    this.type = type;
  }

  draw() {
    switch(this.type) {
      case "circle":
        console.log("Drawing a circle");
        break;
      case "triangle":
        console.log("Drawing a triangle");
        break;
      case "rectangle":
        console.log("Drawing a rectangle");
        break;
      case "square":
        console.log("Drawing a square");
        break;
    }
  }
}

const circle = new Shape("circle");
const triangle = new Shape("triangle");
const square = new Shape("square");

circle.draw();    // "Drawing a circle"
triangle.draw();  // "Drawing a triangle"
```

**What's wrong here?**

Every time you want to add a new shape (like pentagon, hexagon, etc.), you have to:
1. **Modify** the `Shape` class
2. Add a new case to the switch statement
3. Risk breaking existing shapes
4. Retest all shapes

**Timeline of changes:**
```
Week 1: Add circle, triangle, square
  → Modify Shape class

Week 2: Need pentagon
  → Modify Shape class again (add new case)

Week 3: Need hexagon
  → Modify Shape class again (add new case)

Week 4: Need octagon
  → Modify Shape class again (add new case)
  → Oops! Broke triangle while adding octagon!
```

Every new shape requires modifying the same class. This violates OCP!

**Good Example: Following OCP**
```javascript
class Shape {
  draw() {
    throw new Error("Draw method should be implemented");
  }
}

class Circle extends Shape {
  draw() {
    console.log("Drawing a circle");
  }
}

class Triangle extends Shape {
  draw() {
    console.log("Drawing a triangle");
  }
}

class Square extends Shape {
  draw() {
    console.log("Drawing a square");
  }
}

const circle = new Circle();
const triangle = new Triangle();
const square = new Square();

circle.draw();    // "Drawing a circle"
triangle.draw();  // "Drawing a triangle"
```

**Why is this better?**

To add a new shape, you just create a new class:
```javascript
// Adding pentagon - NO modification to existing code!
class Pentagon extends Shape {
  draw() {
    console.log("Drawing a pentagon");
  }
}

const pentagon = new Pentagon();
pentagon.draw();  // Works!
```

**Benefits:**
- No modification to existing `Shape`, `Circle`, `Triangle`, or `Square` classes
- No risk of breaking existing shapes
- No need to retest old shapes
- Easy to add new shapes anytime

**Timeline with OCP:**
```
Week 1: Add Circle, Triangle, Square classes
  → Create new classes

Week 2: Need Pentagon
  → Create new Pentagon class (NO modification to others)

Week 3: Need Hexagon
  → Create new Hexagon class (NO modification to others)

Week 4: Need Octagon
  → Create new Octagon class (NO modification to others)
  → All old shapes still work perfectly!
```

**Comparison:**

**Bad (violating OCP):**
```
Shape class (gets modified every time)
  ├─ draw() with switch statement
  │    ├─ case "circle"
  │    ├─ case "triangle"
  │    ├─ case "square"
  │    └─ case "pentagon" ← Added by modifying existing code
```

**Good (following OCP):**
```
Shape class (never modified)
  └─ draw() (base method)

Circle class (extends Shape)
  └─ draw() (circle implementation)

Triangle class (extends Shape)
  └─ draw() (triangle implementation)

Pentagon class (new, extends Shape) ← Added without modifying anything!
  └─ draw() (pentagon implementation)
```

**Real-World Example: Fetch Function**

**Bad approach (violating OCP):**
```javascript
async function fetchData(url) {
  if (url === "/api/users") {
    const result = await fetch(url, {
      headers: { "Authorization": "Bearer token" }
    });
    return result;
  }
  
  if (url === "/api/posts") {
    const result = await fetch(url, {
      headers: { "Content-Type": "application/json" }
    });
    return result;
  }
  
  if (url === "/api/comments") {
    const result = await fetch(url, {
      method: "POST",
      headers: { "Authorization": "Bearer token" }
    });
    return result;
  }
  
  const result = await fetch(url);
  return result;
}
```

**Problems:**

Every time a new endpoint needs different configuration, you have to:
1. Modify the `fetchData` function
2. Add a new `if` statement
3. Risk breaking existing fetch calls
4. The function keeps growing and growing

**Good approach (following OCP):**
```javascript
async function fetchData(url, options = {}) {
  const result = await fetch(url, options);
  return result;
}

// Usage - EXTEND by passing different options
fetchData("/api/users", {
  headers: { "Authorization": "Bearer token" }
});

fetchData("/api/posts", {
  headers: { "Content-Type": "application/json" }
});

fetchData("/api/comments", {
  method: "POST",
  headers: { "Authorization": "Bearer token" }
});

// Simple call without options
fetchData("/api/data");
```

**Why is this better?**

- Function never needs to be modified
- Each call can pass different options to extend functionality
- No risk of breaking existing calls
- Much cleaner and more flexible

**Another Example: Payment Processing**

**Bad approach:**
```javascript
class PaymentProcessor {
  processPayment(amount, method) {
    switch(method) {
      case "credit_card":
        console.log(`Processing $${amount} via Credit Card`);
        // Credit card logic
        break;
      case "paypal":
        console.log(`Processing $${amount} via PayPal`);
        // PayPal logic
        break;
      case "bitcoin":
        console.log(`Processing $${amount} via Bitcoin`);
        // Bitcoin logic
        break;
      // Need to add Stripe? Modify this class!
      // Need to add Apple Pay? Modify this class!
    }
  }
}
```

**Good approach:**
```javascript
class PaymentMethod {
  process(amount) {
    throw new Error("Process method must be implemented");
  }
}

class CreditCardPayment extends PaymentMethod {
  process(amount) {
    console.log(`Processing $${amount} via Credit Card`);
    // Credit card specific logic
  }
}

class PayPalPayment extends PaymentMethod {
  process(amount) {
    console.log(`Processing $${amount} via PayPal`);
    // PayPal specific logic
  }
}

class BitcoinPayment extends PaymentMethod {
  process(amount) {
    console.log(`Processing $${amount} via Bitcoin`);
    // Bitcoin specific logic
  }
}

// Easy to add new payment methods without modifying existing code!
class StripePayment extends PaymentMethod {
  process(amount) {
    console.log(`Processing $${amount} via Stripe`);
    // Stripe specific logic
  }
}

// Usage
const paymentMethods = [
  new CreditCardPayment(),
  new PayPalPayment(),
  new BitcoinPayment(),
  new StripePayment()
];

paymentMethods.forEach(method => method.process(100));
```

**OCP in React Components**

**Bad approach:**
```javascript
function Button({ type }) {
  if (type === "primary") {
    return <button className="btn-primary">Primary</button>;
  }
  
  if (type === "secondary") {
    return <button className="btn-secondary">Secondary</button>;
  }
  
  if (type === "danger") {
    return <button className="btn-danger">Danger</button>;
  }
  
  // Need to add "success" button? Modify this component!
  
  return <button>Default</button>;
}
```

**Good approach:**
```javascript
function Button({ className, children, ...props }) {
  return (
    <button className={className} {...props}>
      {children}
    </button>
  );
}

// Extend without modifying Button component
<Button className="btn-primary">Primary</Button>
<Button className="btn-secondary">Secondary</Button>
<Button className="btn-danger">Danger</Button>
<Button className="btn-success">Success</Button>
<Button className="btn-warning">Warning</Button>
```

**Achieving OCP: Common Techniques**

**1. Using Parameters/Arguments**
```javascript
// ✗ Bad - needs modification for each case
function calculateDiscount(customerType) {
  if (customerType === "regular") return 0.05;
  if (customerType === "premium") return 0.10;
  if (customerType === "vip") return 0.20;
}

// ✓ Good - pass the discount rate
function calculateDiscount(discountRate) {
  return discountRate;
}

calculateDiscount(0.05);  // Regular
calculateDiscount(0.10);  // Premium
calculateDiscount(0.20);  // VIP
calculateDiscount(0.30);  // New tier - no modification needed!
```

**2. Using Inheritance**
```javascript
class Animal {
  makeSound() {
    throw new Error("Implement makeSound");
  }
}

class Dog extends Animal {
  makeSound() {
    return "Woof!";
  }
}

class Cat extends Animal {
  makeSound() {
    return "Meow!";
  }
}

// Add new animal without modifying existing code
class Cow extends Animal {
  makeSound() {
    return "Moo!";
  }
}
```

**3. Using Composition**
```javascript
class Logger {
  constructor(writer) {
    this.writer = writer;
  }
  
  log(message) {
    this.writer.write(message);
  }
}

class ConsoleWriter {
  write(message) {
    console.log(message);
  }
}

class FileWriter {
  write(message) {
    // Write to file
  }
}

// Extend without modifying Logger
const consoleLogger = new Logger(new ConsoleWriter());
const fileLogger = new Logger(new FileWriter());

// Add new writer type without modifying Logger
class DatabaseWriter {
  write(message) {
    // Write to database
  }
}

const dbLogger = new Logger(new DatabaseWriter());
```

**When to Apply OCP**

✅ **Apply OCP when:**
- You anticipate frequent additions (new shapes, payment methods, etc.)
- Changes would require modifying core functionality
- You want to make your code more maintainable
- Multiple developers work on the same codebase

❌ **Don't over-apply when:**
- Requirements are stable and won't change
- Adding abstraction adds unnecessary complexity
- YAGNI (You Aren't Gonna Need It) principle applies

**Common Mistakes**

**Mistake 1: Over-engineering simple cases**
```javascript
// ✗ Overkill for a simple greeting
class Greeter {
  greet() {
    throw new Error("Implement greet");
  }
}

class EnglishGreeter extends Greeter {
  greet() { return "Hello"; }
}

// ✓ Better - just use a parameter
function greet(language) {
  return language === "en" ? "Hello" : "Bonjour";
}
```

**Mistake 2: Creating too many classes too early**

Don't create abstractions until you need them. Start simple, refactor when you see the pattern.

**Key Takeaways**

1. **Open for extension, closed for modification** - Add new functionality without changing existing code

2. **Extend don't modify** - Create new classes/functions instead of modifying old ones

3. **Common techniques:**
   - Pass parameters/options
   - Use inheritance
   - Use composition

4. **Benefits:**
   - Existing code stays stable
   - Less risk of bugs
   - Easier to add features
   - Better maintainability

5. **Don't over-apply** - Use when it adds value, not for everything

---

**3. Liskov Substitution Principle (LSP)**

The Liskov Substitution Principle states that:

**A subclass should be able to replace its parent class without breaking the application's functionality.**

In simpler terms: If you have a parent class and a child class, you should be able to use the child class anywhere you're using the parent class, and everything should still work correctly.

**Simple Analogy:**

Think of USB devices:
- All USB devices can be plugged into a USB port
- A USB mouse, keyboard, or drive should work in any USB port
- If you replace a USB mouse with a USB keyboard, the port still works
- If a device breaks the port or causes errors, it violates this principle

**The Key Rule:**

**Child classes should:**
- Do everything the parent class can do
- Not break any of the parent class's functionality
- Not throw unexpected errors where the parent doesn't
- Maintain the same behavior contracts

**Bad Example: Violating LSP**
```javascript
class Father {
  walk() {
    console.log("Father is walking");
  }
}

class Son extends Father {
  walk() {
    throw new Error("Son cannot walk");
  }
}

class YoungerSon extends Father {
  walk() {
    console.log("Younger son is walking");
  }
}

function makeWalk(person) {
  person.walk();  // Expects this to work for any person
}

const father = new Father();
const son = new Son();
const youngerSon = new YoungerSon();

makeWalk(father);     // ✓ Works: "Father is walking"
makeWalk(youngerSon); // ✓ Works: "Younger son is walking"
makeWalk(son);        // ✗ Breaks: Error thrown!
```

**What's wrong here?**

The `Son` class throws an error in `walk()`, but the parent `Father` class doesn't. This breaks LSP because:

1. We expect `makeWalk()` to work with any person
2. It works with `Father` and `YoungerSon`
3. But it breaks with `Son`
4. We cannot safely replace `Father` with `Son`

**Visual representation:**
```
makeWalk(Father) → ✓ Works
makeWalk(YoungerSon) → ✓ Works
makeWalk(Son) → ✗ Throws error (violates LSP!)
```

**Why this matters:**

If you're writing code that expects a `Father` object:
```javascript
function dailyRoutine(person) {
  person.walk();  // Should work for Father and all children
  // ... rest of routine
}

// This should work with any child of Father
dailyRoutine(new Father());
dailyRoutine(new YoungerSon());
dailyRoutine(new Son());  // ✗ Crashes!
```

The code breaks when you use `Son`, even though it's a valid child of `Father`. This is a LSP violation.

**Good Example: Following LSP**

**Approach 1: Handle gracefully**
```javascript
class Father {
  walk() {
    console.log("Father is walking");
  }
}

class Son extends Father {
  walk() {
    console.log("Son cannot walk yet");
    // Doesn't throw error, handles gracefully
  }
}

class YoungerSon extends Father {
  walk() {
    console.log("Younger son is walking");
  }
}

function makeWalk(person) {
  person.walk();
}

makeWalk(new Father());     // "Father is walking"
makeWalk(new Son());        // "Son cannot walk yet" ✓ Works!
makeWalk(new YoungerSon()); // "Younger son is walking"
```

**Why this works:**

All implementations of `walk()` succeed without errors. They might do different things, but they all work. You can safely replace `Father` with any child class.

**Approach 2: Better class design**
```javascript
class Person {
  constructor(name, canWalk) {
    this.name = name;
    this.canWalk = canWalk;
  }
  
  walk() {
    if (this.canWalk) {
      console.log(`${this.name} is walking`);
    } else {
      console.log(`${this.name} cannot walk yet`);
    }
  }
}

class Father extends Person {
  constructor() {
    super("Father", true);
  }
}

class Son extends Person {
  constructor() {
    super("Son", false);  // Indicate that son can't walk yet
  }
}

class YoungerSon extends Person {
  constructor() {
    super("Younger Son", true);
  }
}

// All work perfectly!
makeWalk(new Father());     // "Father is walking"
makeWalk(new Son());        // "Son cannot walk yet"
makeWalk(new YoungerSon()); // "Younger son is walking"
```

**Real-World Example 1: Birds**

**Bad approach (violating LSP):**
```javascript
class Bird {
  fly() {
    console.log("Bird is flying");
  }
}

class Sparrow extends Bird {
  fly() {
    console.log("Sparrow is flying");
  }
}

class Penguin extends Bird {
  fly() {
    throw new Error("Penguins can't fly!");
  }
}

function makeBirdFly(bird) {
  bird.fly();  // Expects all birds to fly
}

makeBirdFly(new Sparrow());  // ✓ Works
makeBirdFly(new Penguin());  // ✗ Breaks! (LSP violation)
```

**Good approach (following LSP):**
```javascript
class Bird {
  move() {
    console.log("Bird is moving");
  }
}

class FlyingBird extends Bird {
  fly() {
    console.log("Flying in the air");
  }
  
  move() {
    this.fly();
  }
}

class FlightlessBird extends Bird {
  walk() {
    console.log("Walking on ground");
  }
  
  move() {
    this.walk();
  }
}

class Sparrow extends FlyingBird {}
class Penguin extends FlightlessBird {}

function makeBirdMove(bird) {
  bird.move();  // All birds can move
}

makeBirdMove(new Sparrow());  // "Flying in the air"
makeBirdMove(new Penguin());  // "Walking on ground"
// Both work! ✓
```

**Why this works:**

- All birds can `move()` (common behavior)
- Some fly, some walk (specific behavior)
- No bird throws an error
- You can safely replace any bird with another

**Real-World Example 2: Shapes and Area**

**Bad approach:**
```javascript
class Shape {
  area() {
    return 0;
  }
}

class Rectangle extends Shape {
  constructor(width, height) {
    super();
    this.width = width;
    this.height = height;
  }
  
  area() {
    return this.width * this.height;
  }
}

class Circle extends Shape {
  constructor(radius) {
    super();
    this.radius = radius;
  }
  
  area() {
    throw new Error("Circle area calculation not implemented!");
    // This breaks LSP!
  }
}

function printArea(shape) {
  console.log("Area:", shape.area());
}

printArea(new Rectangle(5, 10));  // ✓ Works
printArea(new Circle(5));         // ✗ Breaks!
```

**Good approach:**
```javascript
class Shape {
  area() {
    throw new Error("area() must be implemented by subclass");
  }
}

class Rectangle extends Shape {
  constructor(width, height) {
    super();
    this.width = width;
    this.height = height;
  }
  
  area() {
    return this.width * this.height;
  }
}

class Circle extends Shape {
  constructor(radius) {
    super();
    this.radius = radius;
  }
  
  area() {
    return Math.PI * this.radius * this.radius;
  }
}

function printArea(shape) {
  console.log("Area:", shape.area());
}

printArea(new Rectangle(5, 10));  // Area: 50
printArea(new Circle(5));         // Area: 78.54
// Both work! ✓
```

**Real-World Example 3**

```javascript
// ✗ Bad
class Vehicle {
  startEngine() {
    console.log("Engine started");
    return true;
  }
}

class Car extends Vehicle {}

class Bicycle extends Vehicle {
  startEngine() {
    throw new Error("Bicycles don't have engines!");
  }
}

function startAllVehicles(vehicles) {
  vehicles.forEach(v => v.startEngine());
}
```

```javascript
// ✓ Good
class Vehicle {
  start() {
    console.log("Vehicle started");
  }
}

class MotorizedVehicle extends Vehicle {
  startEngine() {
    console.log("Engine started");
  }
  
  start() {
    this.startEngine();
  }
}

class NonMotorizedVehicle extends Vehicle {
  start() {
    console.log("Ready to go!");
  }
}

class Car extends MotorizedVehicle {}
class Bicycle extends NonMotorizedVehicle {}

function startAllVehicles(vehicles) {
  vehicles.forEach(v => v.start());  // All work!
}

const vehicles = [new Car(), new Bicycle()];
startAllVehicles(vehicles);
// Engine started
// Ready to go!
```

**Real-World Example 4: Payment Methods**

**Bad approach:**
```javascript
class PaymentMethod {
  process(amount) {
    console.log(`Processing payment of $${amount}`);
    return true;
  }
}

class CreditCard extends PaymentMethod {
  process(amount) {
    console.log(`Charging credit card $${amount}`);
    return true;
  }
}

class Cash extends PaymentMethod {
  process(amount) {
    throw new Error("Cannot process cash payments online!");
    // Breaks LSP!
  }
}

function processPayment(paymentMethod, amount) {
  if (paymentMethod.process(amount)) {
    console.log("Payment successful");
  }
}

processPayment(new CreditCard(), 100);  // ✓ Works
processPayment(new Cash(), 100);        // ✗ Breaks!
```

**Good approach:**
```javascript
class PaymentMethod {
  process(amount) {
    throw new Error("process() must be implemented");
  }
  
  isOnlineSupported() {
    return false;
  }
}

class OnlinePayment extends PaymentMethod {
  isOnlineSupported() {
    return true;
  }
}

class OfflinePayment extends PaymentMethod {
  isOnlineSupported() {
    return false;
  }
  
  process(amount) {
    console.log(`Processing offline payment of $${amount}`);
    return false;
  }
}

class CreditCard extends OnlinePayment {
  process(amount) {
    console.log(`Charging credit card $${amount}`);
    return true;
  }
}

class Cash extends OfflinePayment {
  process(amount) {
    console.log(`Cash payment of $${amount} - requires in-person payment`);
    return false;
  }
}

function processPayment(paymentMethod, amount) {
  if (!paymentMethod.isOnlineSupported()) {
    console.log("This payment method requires in-person payment");
    return;
  }
  
  if (paymentMethod.process(amount)) {
    console.log("Payment successful");
  }
}

processPayment(new CreditCard(), 100);  // Works
processPayment(new Cash(), 100);        // Handled gracefully
```

**LSP Rules to Follow**

**1. Child class must accept same input types as parent**
```javascript
// ✗ Bad
class Parent {
  doSomething(value) {
    // Accepts any value
  }
}

class Child extends Parent {
  doSomething(value) {
    if (typeof value !== 'number') {
      throw new Error("Only numbers!");  // Stricter than parent
    }
  }
}

// ✓ Good
class Child extends Parent {
  doSomething(value) {
    // Accepts any value, like parent
  }
}
```

**2. Child class should return compatible types**
```javascript
// ✗ Bad
class Parent {
  getValue() {
    return 42;  // Returns number
  }
}

class Child extends Parent {
  getValue() {
    return "42";  // Returns string - different type!
  }
}

// ✓ Good
class Child extends Parent {
  getValue() {
    return 100;  // Returns number, like parent
  }
}
```

**3. Child class shouldn't throw new exceptions**
```javascript
// ✗ Bad
class Parent {
  calculate(x) {
    return x * 2;  // Doesn't throw
  }
}

class Child extends Parent {
  calculate(x) {
    if (x < 0) {
      throw new Error("No negatives!");  // New exception!
    }
    return x * 2;
  }
}

// ✓ Good
class Child extends Parent {
  calculate(x) {
    return Math.abs(x) * 2;  // Handles negatives without throwing
  }
}
```

**When LSP is Violated**

Signs that you're violating LSP:

1. **Throwing exceptions in child classes** where parent doesn't
2. **Returning different types** than parent
3. **Requiring stricter inputs** than parent
4. **Changing behavior unexpectedly** from parent
5. **Needing type checks** before using objects
```javascript
// If you're doing this, you're probably violating LSP:
function doSomething(obj) {
  if (obj instanceof SpecificChild) {
    // Special handling for this child
  } else {
    // Normal handling
  }
}
```

**Key Takeaways**

1. **Child should replace parent** without breaking anything

2. **Same inputs, compatible outputs** - maintain the contract

3. **Don't throw new errors** where parent doesn't

4. **Handle edge cases gracefully** - don't break expectations

5. **If you need type checking**, you probably violated LSP

6. **Better class design** prevents LSP violations

7. **LSP ensures** your inheritance hierarchy makes sense

---

**4. Interface Segregation Principle (ISP)**

The Interface Segregation Principle states that:

**No class should be forced to implement methods or properties it doesn't use.**

In simpler terms: Create specific, focused interfaces rather than one large, general-purpose interface. Don't make classes depend on things they don't need.

**Simple Analogy:**

Think of a restaurant menu:
- **Bad**: One giant menu with breakfast, lunch, dinner, drinks, desserts all together (overwhelming)
- **Good**: Separate menus for breakfast, lunch, dinner (focused, easy to use)

You wouldn't force someone who just wants coffee to look through the entire lunch menu. Similarly, don't force a class to implement methods it doesn't need.

**Note on Interfaces:**

While JavaScript doesn't have built-in interfaces like TypeScript, the principle still applies to:
- Base classes that child classes extend
- Object shapes and contracts
- Function parameters
- Component props in React

**Bad Example: Violating ISP**
```typescript
// TypeScript example (but principle applies to JavaScript too)
interface IPerson {
  name: string;
  age: number;
  hobby: string;
  fly: boolean;  // ← Not all persons can fly!
}

class Person implements IPerson {
  name: string;
  age: number;
  hobby: string;
  fly: boolean;  // ← Forced to have this even though it doesn't make sense
  
  constructor(name: string, age: number, hobby: string) {
    this.name = name;
    this.age = age;
    this.hobby = hobby;
    this.fly = false;  // ← What do we even put here?
  }
}
```

**What's wrong here?**

- Regular people can't fly
- But the interface forces them to have a `fly` property
- We're including something that doesn't belong
- This clutters the interface with unnecessary properties

**Visual representation:**
```
IPerson interface
├─ name ✓ (needed)
├─ age ✓ (needed)
├─ hobby ✓ (needed)
└─ fly ✗ (NOT needed for regular Person!)
```

**Good Example: Following ISP**
```typescript
interface IPerson {
  name: string;
  age: number;
  hobby: string;
}

interface IPersonWhoCanFly {
  fly: boolean;
}

class Person implements IPerson {
  name: string;
  age: number;
  hobby: string;
  
  constructor(name: string, age: number, hobby: string) {
    this.name = name;
    this.age = age;
    this.hobby = hobby;
  }
}

class FlyingPerson implements IPerson, IPersonWhoCanFly {
  name: string;
  age: number;
  hobby: string;
  fly: boolean;
  
  constructor(name: string, age: number, hobby: string) {
    this.name = name;
    this.age = age;
    this.hobby = hobby;
    this.fly = true;
  }
}
```

**Why this is better:**

- Regular people only implement `IPerson` (what they need)
- Flying people implement both interfaces (exactly what they need)
- Each interface is focused and specific
- No class is forced to have properties it doesn't use

**Visual representation:**
```
IPerson interface
├─ name ✓
├─ age ✓
└─ hobby ✓

IPersonWhoCanFly interface
└─ fly ✓

Person → uses IPerson only
FlyingPerson → uses both IPerson and IPersonWhoCanFly
```

**Real-World Example: Office Equipment**

**Bad approach (violating ISP):**
```javascript
class MultiFunctionDevice {
  print() {
    console.log("Printing...");
  }

  scan() {
    console.log("Scanning...");
  }

  fax() {
    console.log("Faxing...");
  }
}

class Printer extends MultiFunctionDevice {
  print() {
    console.log("Printing...");
  }

  scan() {
    throw new Error("Printer cannot scan");
  }

  fax() {
    throw new Error("Printer cannot fax");
  }
}

class Scanner extends MultiFunctionDevice {
  print() {
    throw new Error("Scanner cannot print");
  }

  scan() {
    console.log("Scanning...");
  }

  fax() {
    throw new Error("Scanner cannot fax");
  }
}
```

**What's wrong?**

- `Printer` is forced to have `scan()` and `fax()` methods it can't use
- `Scanner` is forced to have `print()` and `fax()` methods it can't use
- Methods throw errors because the device doesn't support those features
- Violates LSP (Liskov Substitution Principle) too!

**Timeline of problems:**
```
User: "Let me use this MultiFunctionDevice to print"
  → Uses Printer → ✓ Works

User: "Let me use this MultiFunctionDevice to scan"
  → Uses Printer → ✗ Error! "Printer cannot scan"

User: "But it's a MultiFunctionDevice, why can't it scan?"
  → Because we forced Printer to inherit methods it can't use
```

**Good approach (following ISP):**
```javascript
// Separate, focused classes
class PrinterService {
  print() {
    console.log("Printing...");
  }
}

class ScannerService {
  scan() {
    console.log("Scanning...");
  }
}

class FaxService {
  fax() {
    console.log("Faxing...");
  }
}

// Devices only inherit what they need
class Printer extends PrinterService {
  print() {
    console.log("Basic printer: Printing...");
  }
}

class Scanner extends ScannerService {
  scan() {
    console.log("Basic scanner: Scanning...");
  }
}

// Multi-function device uses composition
class MultiFunctionDevice {
  constructor() {
    this.printer = new PrinterService();
    this.scanner = new ScannerService();
    this.fax = new FaxService();
  }

  print() {
    this.printer.print();
  }

  scan() {
    this.scanner.scan();
  }

  fax() {
    this.fax.fax();
  }
}

// Usage
const printer = new Printer();
printer.print();  // ✓ Works
// printer.scan(); // ✗ Not available (correct!)

const scanner = new Scanner();
scanner.scan();   // ✓ Works
// scanner.print(); // ✗ Not available (correct!)

const mfd = new MultiFunctionDevice();
mfd.print();  // ✓ Works
mfd.scan();   // ✓ Works
mfd.fax();    // ✓ Works
```

**Why this is better:**

- Each device only has methods it can actually use
- No forced implementations
- No throwing errors
- Clear, focused classes
- Easy to add new devices

**Visual comparison:**

**Bad (violating ISP):**
```
MultiFunctionDevice
├─ print()
├─ scan()
└─ fax()
      ↓
Printer (inherits ALL)
├─ print() ✓ (works)
├─ scan() ✗ (throws error!)
└─ fax() ✗ (throws error!)
```

**Good (following ISP):**
```
PrinterService
└─ print()
      ↓
Printer (inherits ONLY what it needs)
└─ print() ✓ (works)
```

**ISP in JavaScript (without TypeScript)**

Even without interfaces, you can follow ISP:

**Bad approach:**
```javascript
class Employee {
  work() { console.log("Working"); }
  code() { console.log("Coding"); }
  design() { console.log("Designing"); }
  manage() { console.log("Managing"); }
}

class Developer extends Employee {
  work() { console.log("Working"); }
  code() { console.log("Coding"); }
  design() { throw new Error("Developer doesn't design"); }
  manage() { throw new Error("Developer doesn't manage"); }
}
```

**Good approach:**
```javascript
class Employee {
  work() { console.log("Working"); }
}

class Developer extends Employee {
  code() { console.log("Coding"); }
}

class Designer extends Employee {
  design() { console.log("Designing"); }
}

class Manager extends Employee {
  manage() { console.log("Managing"); }
}
```

**ISP in React Components**

**Bad approach (violating ISP):**
```javascript
// Component expects ALL these props, even if not needed
function UserProfile({
  name,
  email,
  address,
  phoneNumber,
  creditCard,
  socialSecurity,
  bankAccount
}) {
  return (
    <div>
      <h1>{name}</h1>
      <p>{email}</p>
    </div>
  );
}

// Using the component - forced to pass all props!
<UserProfile
  name="John"
  email="john@example.com"
  address={null}          // Don't need this
  phoneNumber={null}      // Don't need this
  creditCard={null}       // Don't need this
  socialSecurity={null}   // Don't need this
  bankAccount={null}      // Don't need this
/>
```

**Good approach (following ISP):**
```javascript
// Component only asks for what it needs
function UserProfile({ name, email }) {
  return (
    <div>
      <h1>{name}</h1>
      <p>{email}</p>
    </div>
  );
}

// Separate component for sensitive info
function UserSensitiveInfo({ creditCard, socialSecurity, bankAccount }) {
  return (
    <div>
      {/* Display sensitive info */}
    </div>
  );
}

// Clean usage
<UserProfile name="John" email="john@example.com" />
```

**Another React Example:**

**Bad approach:**
```javascript
function Button({
  text,
  onClick,
  onHover,
  onFocus,
  onBlur,
  onDoubleClick,
  onRightClick,
  onMouseEnter,
  onMouseLeave
}) {
  return <button onClick={onClick}>{text}</button>;
}

// Only using onClick, but forced to be aware of all events
<Button
  text="Click me"
  onClick={handleClick}
  onHover={undefined}
  onFocus={undefined}
  // ... all these undefined values!
/>
```

**Good approach:**
```javascript
function Button({ text, onClick }) {
  return <button onClick={onClick}>{text}</button>;
}

// Clean and focused
<Button text="Click me" onClick={handleClick} />

// If you need more events, create a specialized component
function InteractiveButton({ text, onClick, onHover }) {
  return (
    <button onClick={onClick} onMouseEnter={onHover}>
      {text}
    </button>
  );
}
```

**Real-World Example: Database Operations**

**Bad approach:**
```javascript
class Database {
  connect() { /* ... */ }
  disconnect() { /* ... */ }
  read() { /* ... */ }
  write() { /* ... */ }
  update() { /* ... */ }
  delete() { /* ... */ }
  backup() { /* ... */ }
  restore() { /* ... */ }
}

class ReadOnlyDatabase extends Database {
  write() { throw new Error("Read-only!"); }
  update() { throw new Error("Read-only!"); }
  delete() { throw new Error("Read-only!"); }
  backup() { throw new Error("Not supported"); }
  restore() { throw new Error("Not supported"); }
}
```

**Good approach:**
```javascript
class DatabaseConnection {
  connect() { /* ... */ }
  disconnect() { /* ... */ }
}

class ReadOperations extends DatabaseConnection {
  read() { /* ... */ }
}

class WriteOperations extends DatabaseConnection {
  write() { /* ... */ }
  update() { /* ... */ }
  delete() { /* ... */ }
}

class BackupOperations extends DatabaseConnection {
  backup() { /* ... */ }
  restore() { /* ... */ }
}

// Use composition for full database
class FullDatabase {
  constructor() {
    this.read = new ReadOperations();
    this.write = new WriteOperations();
    this.backup = new BackupOperations();
  }
}

// Read-only database only uses what it needs
class ReadOnlyDatabase extends ReadOperations {}
```

**When to Apply ISP**

✅ **Apply ISP when:**
- You have large interfaces with many methods
- Not all classes need all methods
- You're forcing classes to implement unused methods
- You're throwing errors in "not supported" methods

❌ **Don't over-apply when:**
- Interface is already small and focused
- All implementing classes genuinely need all methods
- Splitting would create unnecessary complexity

**Benefits of ISP**

1. **Cleaner code** - Classes only have what they need
2. **Easier to understand** - Clear, focused interfaces
3. **Less coupling** - Changes to one interface don't affect others
4. **Better testability** - Smaller, focused units to test
5. **Prevents errors** - No "not supported" exceptions

**Key Takeaways**

1. **Don't force classes to implement what they don't use**

2. **Create small, focused interfaces** instead of large, general ones

3. **"Fat interfaces"** with many methods are a code smell

4. **If throwing "not supported" errors**, you're violating ISP

5. **Composition over inheritance** often helps follow ISP

6. **In React**, keep component props focused and minimal

7. **Benefits**: Cleaner, more maintainable, less coupled code

---