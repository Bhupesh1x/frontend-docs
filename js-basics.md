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


## Hoisting in JavaScript

**What is Hoisting?**  
Hoisting refers to JavaScript’s ability to access variables and functions **even before they are declared**.  
This happens because JavaScript allocates memory for them before execution starts.

---

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

---

**Variables vs Functions**  
- Function declarations are fully hoisted — you can call them before defining them.  
- Variables are hoisted but set to `undefined`.  
- Arrow functions and function expressions behave like variables, so they also start off as `undefined`.

---

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

## How Functions Work in JavaScript

Functions are the heart of JavaScript. We can think of them as **mini programs** that run inside the main program and have their own execution flow.

---

**Execution Context and Call Stack**  
When a JavaScript program starts running, a **Global Execution Context (GEC)** is created and pushed onto the **call stack**.  
Just like any execution context, it goes through two phases:
- Memory Creation Phase
- Code Execution Phase

---

**What Happens When a Function Is Called**  
During the code execution phase, when JavaScript encounters a function call:
- A **new execution context** is created for that function.
- This execution context is pushed on top of the call stack.
- Execution control moves to the **first line of the function body**.

Inside this function execution context:
- Memory is allocated for the function’s variables and parameters.
- The function has access to its **own memory** and also to its **parent (outer) scope**.

---

**Function Completion**  
Once the function finishes executing:
- Its execution context is removed (popped) from the call stack.
- Control returns back to the execution context below it.

This push-and-pop behavior of execution contexts is what allows JavaScript to manage multiple function calls efficiently.

## Shortest Program in JavaScript

**What is the Shortest Program?**  
In JavaScript, the shortest program is an **empty file**. Even when there is nothing to execute, JavaScript still performs its internal setup.

---

**What JavaScript Does Internally**  
When an empty file runs:
- A **Global Execution Context (GEC)** is created.
- It is pushed into the **call stack**.
- The **global object (`window` in browsers)** is created.
- The `this` keyword is set to refer to the global object.

---

**Execution Completion**  
Since there is no code to execute:
- The execution phase completes immediately.
- The global execution context is popped out of the call stack.

---

**Global Scope**  
- Any variables or functions declared in the global scope are attached to the global object.
- The global scope includes everything that is **not inside any function**.
- The variables and functions can be accessed using window.a or directly as a as it is in global scope.

---

**Example**

```js
var x = 10;
console.log(x); // 10
console.log(window.x); // 10
console.log(this.x); // 10
```


## Undefined vs Not Defined in JavaScript

**What does `undefined` mean?**  
In JavaScript, `undefined` is a **special value**. It acts as a placeholder for variables that have been **declared but not yet assigned a value**.

When JavaScript allocates memory during the memory creation phase, variables are initialized with `undefined` until a value is assigned during execution.

---

**What does `not defined` mean?**  
`not defined` means that a variable or function **does not exist in the program at all**.  
It was never declared, so no memory was allocated for it.

---

**Key Difference**  
- `undefined` → variable is declared and has memory, but no value yet  
- `not defined` → variable is not declared and has no memory  

Although you *can* manually assign `undefined` as a value, its main purpose is to indicate that a variable exists but hasn’t been assigned yet.

---

**Example**

```js
console.log(a); // undefined
var a = 10;
console.log(a); // 10

console.log(x); // ReferenceError: x is not defined
```

## The Scope Chain in JavaScript

**What is Scope?**  
Scope defines what variables and functions can be accessed at a particular place in the code.

---

**Execution Context and Lexical Environment**  
Whenever an execution context is created in JavaScript, it contains:
- Its own **local memory**
- A **lexical environment**

The lexical environment is a reference to the local memory + lexical environment of it's **parent scope** — the place where the function is physically available in the code.

---

**What is the Scope Chain?**  
The whole chain of:
- Execution context local memory + lexical environment forms a scope chain
forms the **scope chain**.

This chain determines what variables and functions are accessible in the current scope.

---

**How JavaScript Resolves Variables**  
When JavaScript tries to access a variable or function:
1. It first looks in the current local scope.
2. If not found, it looks in it's lexical environment.
3. This process continues up the chain until the **global scope** is reached.
4. If JavaScript cannot find the variable or function anywhere in the scope chain, it throws a `ReferenceError` saying the identifier is not defined.

The global execution context’s lexical environment points to `null`, which marks the end of the scope chain.

---  

**Example**

```js

function a() {
  function b() {
    console.log(b)  // 10
  }
  b()
}
let b = 10;
a();
```

---

- ![the-scope-chain](./js-basics-assets/the-scope-chain.png)

## let, const vs var in JavaScript

**Overview**  
`let`, `const`, and `var` differ mainly in three areas:
- Hoisting
- Strictness (redeclaration & initialization)
- Scope

---

**Hoisting Behavior**  
All three keywords are hoisted, meaning memory is allocated before code execution starts.

- Variables declared with `var` are initialized with `undefined` and attached to the global object.
- `let` and `const` are also hoisted and initialized with `undefined`, but they are stored in a separate memory space (script scope).
- Accessing `let` or `const` before initialization results in a `ReferenceError`. As they are in `Temporal dead zone` till they are initialized. They can be accessed only after initialized some value in it. 

---

**Temporal Dead Zone (TDZ)**  
The time between hoisting and initialization of `let` and `const` variables is called the **Temporal Dead Zone**.

During this period:
- Variables exist in memory
- But cannot be accessed

Moving variable declarations to the top of the scope helps reduce the TDZ.

---

**Example**

```js

console.log(b); // Reference error


console.log(a); // undefined

var a = 10;

let b = 10;

console.log(a); // 10
console.log(b); // 10

```


---

**Strictness Rules**  
- `var` allows redeclaration in the same scope.
- `let` and `const` do not allow redeclaration in the same scope and will throw an error.

`const` is stricter than `let`:
- It must be declared and initialized in the same statement.
- Reassignment is not allowed.
- `let` allows declaration first and initialization later.

---

**Example**

```js

var a = 10;

var a = "Hello world"; // allowed

let x;

x =  10;  // allowed: Can be declared first and initialized letter.

let x = "Hello world"; // Error: cannot redeclare the let variables


const b = 20; // allowed

const b;

b = 10;  // Syntax error: variable declared with const should be declared and initialized in the same statement.

```

---

**Scope Differences**  
- `var` is **function-scoped**.
- `let` and `const` are **block-scoped**.

This means:
- `let` and `const` variables are accessible only within the block `{}` they are declared in.
- `var` variables can be accessed outside blocks (if not inside a function).

---

**Example**

```js

if(true) {
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

---

**Why Blocks Are Needed**  
Statements like `if` do not require `{}` by syntax, but blocks are used when we want to execute **multiple statements** instead of just one.

---

**Block Scope vs Function Scope**  
- Variables declared with `let` and `const` inside `{}` are **block-scoped**.
- They cannot be accessed outside the block.
- `var` is **function-scoped**, not block-scoped.

This means:
- `var` declared inside a block still belongs to the enclosing function or global scope.
- `let` and `const` declared in the global scope are stored in the **script scope**, not on the global object.

---

**Shadowing**  
Shadowing occurs when a variable declared in an inner scope has the same name as a variable in an outer scope.

In such cases:
- The inner variable **shadows** the outer one inside that block.
- Outside the block, the original variable remains unchanged for let and const in block scope.

---

**Illegal Shadowing**  
Shadowing must respect scope rules.

For example:
- A `let` variable declared in an outer scope **cannot** be shadowed by a `var` in an inner scope.
- This is called **illegal shadowing** and results in an error.

---

**Scope Rules Still Apply**  
Blocks follow the same rules of:
- Scope
- Lexical environment
- Scope chain

Arrow functions follow the same scoping rules as regular functions.

---

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

---

**How Closures Work**  
In JavaScript, every function has access to its **lexical environment** (outer scope).  
Even if a function is returned and executed in a different scope, it still remembers the variables and functions from the scope where it was originally created.

A function along with the reference to its outer scope forms a **closure**.

---

**Why Closures Are Powerful**  
Closures become more interesting when a function is returned or passed around and executed elsewhere.  
Even then, the function continues to hold references to variables in its lexical environment.

These referenced values are **not garbage collected**, because they may be needed later.

---

**Common Use Cases of Closures**  
Closures are commonly used in:
- Functions like `once`
- Memoization
- Data hiding and encapsulation
- Asynchronous code (callbacks, timers, promises)

---

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
