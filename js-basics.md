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
