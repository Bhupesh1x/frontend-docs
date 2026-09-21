## Implement Stack using Queues

```md
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

- void push(int x) Pushes element x to the top of the stack.
- int pop() Removes the element on the top of the stack and returns it.
- int top() Returns the element on the top of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

- You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
```

**code**

```js
var MyStack = function () {
  // Initialize the two queues we'll need.
  // Two queues used so when we try to pop or peek we have to remove the values from queue to find the last which will be first to leave or returned from top for stack
  // So when we leave those we somehow need to get the previous values back so that's why 2 queues so that we can store the values in other queue while removing from first

  this.q1 = [];
  this.q2 = [];
};

/**
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function (x) {
  // In push we just push the values in q1 as they are same operations as array

  this.q1.push(x);
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function () {
  /**
   * For pop we first dequeue(shift - Remove from first) values till n - 1 place
   * And store it safely in the second queue we have
   * Now we dequeue the last element and store it in a variable so that we can return it at the end as pop returns the value removed
   * Now q1 is empty and q2 has the n - 1 values we had previously in q1.
   * We can make the q2 as main queue now. So we can just swap both the queues
   * Now just return the ans we stored in the variable
   */

  let n = this.q1.length;

  for (let i = 0; i < n - 1; i++) {
    this.q2.push(this.q1.shift());
  }

  const ans = this.q1.shift();

  // Swap the queue
  let temp = this.q1;
  this.q1 = this.q2;
  this.q2 = temp;

  return ans;
};

/**
 * @return {number}
 */
MyStack.prototype.top = function () {
  /**
   * For top we first dequeue(shift - Remove from first) values till n - 1 place
   * And store it safely in the second queue we have
   * Now we dequeue the last element and store it in a variable so that we can return it at the end as top returns the value at the top of stack now we can push this also in q2 as we want all the values intact in top
   * Now q1 is empty and q2 has all the values we had previously in q1.
   * We can make the q2 as main queue now. So we can just swap both the queues
   * Now just return the ans we stored in the variable
   */

  let n = this.q1.length;

  for (let i = 0; i < n - 1; i++) {
    this.q2.push(this.q1.shift());
  }

  let firstElem = this.q1.shift();

  this.q2.push(firstElem);

  // Swap the queue
  let temp = this.q1;
  this.q1 = this.q2;
  this.q2 = temp;

  return firstElem;
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function () {
  // Just check if the q1 (Our main queue) length is 0. If it is it's empty
  return this.q1.length === 0;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
```
