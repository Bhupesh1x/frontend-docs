## Stack And Queues Introduction

**Stack**

- Stack is a Data structure which has Last In First Out (LIFO) flow. So the element added at the end will come out first.

- It has methods like push(add), pop(remove) and peek/top

- Examples: stack of books, undo feature, Browsing history

**Queue**

- Queue is a Data structure which has First In First Out (FIFO) flow. So the element added at the first will come out first.

- It has methods like enqueue(add), dequeue(remove) and peek/front

- Examples: Ticket counter, os task scheduling, queue in general

![stack-and-queues](./assets/stack-and-queues.png)

---

**Why do we need them**

- Stack and queues help us organize the data logically (based on the problem need).

- When the order of the operations matter then we use stack and queues generally.

- When we need to optimize the time and space for the specific cases

**Use cases**

- Recursion - Stack
- Level order traversal in trees - Queues
- BFS - Queues
- DFS (Depth first search) - Stack

**What is stack and queue in code**

- We use arrays only for creating the stack and queues in js. But they are used with some restrictions.

**When we already have arrays why do we need stack and queues**

- Restricted access (Top only): We can't just directly use the index to find the element in the stack and queues.

- Cannot modify random index directly like array.

- stack === array but with restricted access.

- Arrays don't enforce discipline they are used for general purpose storage. But stack and queues does enforce discipline.

**Comparisons with other data structures**

Feature: Stack | Queue | Array | Linked List | HashMap |
Order: LIFO | FIFO | Indexed | Sequential | Key-Based |
Random Access: Not Allowed | Not Allowed | Allowed | Not Allowed | Allowed
Insert/Delete: Top Only | Front/Back Only | Anywhere (slow) | Anywhere | By Key
Time Complexity: O(1) | O(1) | varies | O(1) insert | O(1)
Use case: Backtracking | Scheduling | General purpose | Dynamic size | Lookup
