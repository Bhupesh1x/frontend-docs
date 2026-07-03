# Linked List

## What is a Linked List?

A Linked List is a linear data structure where elements are stored in separate nodes.

Unlike arrays, nodes are **not stored next to each other in memory**. Each node stores:

1. Data (value)
2. Reference (pointer) to the next node

Example:

[10 | •] → [20 | •] → [30 | null]

---

## Why do we need a Linked List?

Arrays work great when we need fast access using an index.

But arrays have some problems:

- Inserting at the beginning is expensive.
- Deleting from the beginning is expensive.
- Resizing may be needed when size grows.

Linked Lists solve these problems by connecting nodes using references.

---

## Node Structure

### Singly Linked List Node

[value | next]

Example:

[5 | •]

The node stores:

- value = 5
- next = reference to next node

---

### Doubly Linked List Node

[prev | value | next]

Example:

[null | 5 | •]

The node stores:

- prev = reference to previous node
- value = 5
- next = reference to next node

---

## Types of Linked Lists

### 1. Singly Linked List

Each node stores:

- value
- next reference

Example:

[10 | •] → [20 | •] → [30 | null]

Can only move in forward direction.

---

### 2. Doubly Linked List

Each node stores:

- prev reference
- value
- next reference

Example:

null ← [10] ⇄ [20] ⇄ [30] → null

Can move:

- Forward
- Backward

---

## Head

Head is the first node of the linked list.

Example:

Head
↓
[10] → [20] → [30]

Head helps us start traversing the list.

---

## Tail

Tail is the last node of the linked list.

Example:

[10] → [20] → [30]
↑
Tail

The tail node's next pointer is null.

---

## Traversal

To visit every node, start from head and keep moving to next.

Example:

Head
↓
[10] → [20] → [30] → null

Traversal order:

10 → 20 → 30

Time Complexity: O(n)

---

## Linked List vs Array

| Feature                    | Linked List             | Array                                     |
| -------------------------- | ----------------------- | ----------------------------------------- |
| Storage                    | Non-contiguous          | Contiguous                                |
| Size                       | Dynamic                 | Usually fixed (Dynamic arrays can resize) |
| Access by Index            | O(n)                    | O(1)                                      |
| Insert/Delete at Beginning | Easy                    | Costly                                    |
| Insert/Delete in Middle    | Easier if node is known | Costly because shifting is needed         |
| Extra Memory               | Needed for pointers     | No extra pointers                         |
| Cache Friendly             | No                      | Yes                                       |

---

## Time Complexities

### Array

| Operation       | Time |
| --------------- | ---- |
| Access by Index | O(1) |
| Search          | O(n) |
| Insert          | O(n) |
| Delete          | O(n) |

### Linked List

| Operation                        | Time |
| -------------------------------- | ---- |
| Access by Index                  | O(n) |
| Search                           | O(n) |
| Insert at Head                   | O(1) |
| Delete at Head                   | O(1) |
| Insert/Delete (if node is known) | O(1) |

---

## When to Use Array?

Use Array when:

- Fast index access is needed.
- Size does not change much.
- Memory efficiency is important.
- Frequent random access is required.

Examples:

- Storing marks of students.
- Lookup tables.
- Fixed-size collections.

---

## When to Use Linked List?

Use Linked List when:

- Frequent insertion/deletion is required.
- Size is unknown beforehand.
- Data keeps growing and shrinking.
- We mainly traverse data sequentially.

Examples:

- Browser history.
- Music playlist.
- Undo/Redo operations.
- LRU Cache (with Doubly Linked List).

---

## Easy Way to Remember

Array:

- Fast Access ✅
- Slow Insert/Delete ❌

Linked List:

- Slow Access ❌
- Fast Insert/Delete ✅
