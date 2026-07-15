# Intersection of Two Linked Lists (Using Hash Map)

## Problem

Given the heads of two singly linked lists `headA` and `headB`, return the node where the two linked lists intersect.

If the two linked lists do not intersect, return:

```js
null;
```

### Example

```text
List A

4 -> 1
       \
        8 -> 4 -> 5
       /
5 -> 6 -> 1

List B
```

Output:

```text
8
```

Because both linked lists start sharing the exact same node from `8`.

---

## Important Observation

Intersection means:

```text
Same Node Reference
```

NOT:

```text
Same Value
```

Example:

```text
A: 1 -> 2 -> 3

B: 4 -> 2 -> 5
```

The value `2` appears in both lists.

But:

```text
They are different nodes in memory.
```

So this is:

```text
NOT an intersection.
```

---

## Intuition

We need to find whether a node from List A already exists somewhere in List B.

A simple approach:

1. Store all nodes of List B inside a Map.
2. Traverse List A.
3. If any node already exists in the Map:
   - That node is the intersection point.
4. Return that node.

If no node matches:

```js
return null;
```

---

## Code

```js
var getIntersectionNode = function (headA, headB) {
  const map = new Map();

  while (headB) {
    map.set(headB, 1);
    headB = headB.next;
  }

  while (headA) {
    if (map.has(headA)) {
      return headA;
    }

    headA = headA.next;
  }

  return null;
};
```

---

## Approach

### Step 1

Store every node of List B in a Map.

```js
map.set(node, 1);
```

---

### Step 2

Traverse List A.

For every node:

```js
if (map.has(node))
```

then:

```text
This exact node already exists in List B.
```

Return it immediately.

---

### Step 3

If traversal finishes:

```js
return null;
```

---

# Dry Run

## Input

```text
List A

4 -> 1
       \
        8 -> 4 -> 5
       /
5 -> 6 -> 1

List B
```

---

## Step 1: Store List B in Map

Traverse:

```text
5 -> 6 -> 1 -> 8 -> 4 -> 5
```

Store nodes:

| Step | Current Node | Map Contents  |
| ---- | ------------ | ------------- |
| 1    | 5            | {5}           |
| 2    | 6            | {5,6}         |
| 3    | 1            | {5,6,1}       |
| 4    | 8            | {5,6,1,8}     |
| 5    | 4            | {5,6,1,8,4}   |
| 6    | 5            | {5,6,1,8,4,5} |

Map now contains all node references from List B.

---

## Step 2: Traverse List A

List A:

```text
4 -> 1 -> 8 -> 4 -> 5
```

---

### Visit Node 4

Check:

```js
map.has(node4);
```

Result:

```js
false;
```

Continue.

---

### Visit Node 1

Check:

```js
map.has(node1);
```

Result:

```js
false;
```

Continue.

---

### Visit Node 8

Check:

```js
map.has(node8);
```

Result:

```js
true;
```

Return:

```text
Node 8
```

Intersection found.

---

## Dry Run Table

| Step | Current Node (A) | Exists In Map? | Action        |
| ---- | ---------------- | -------------- | ------------- |
| 1    | 4                | ❌             | Continue      |
| 2    | 1                | ❌             | Continue      |
| 3    | 8                | ✅             | Return Node 8 |

---

## Visualization

### List A

```text
4 -> 1
       \
        8 -> 4 -> 5
```

### List B

```text
5 -> 6 -> 1
            \
             8 -> 4 -> 5
```

Notice:

```text
Both lists share the same node 8.
```

Not just the same value.

The actual memory reference is the same.

---

## Example Where Values Match But No Intersection

### List A

```text
1 -> 2 -> 3
```

### List B

```text
4 -> 2 -> 5
```

Looks like:

```text
2 appears in both lists
```

But actually:

```text
Node(2) in A ≠ Node(2) in B
```

Different memory locations.

Visualization:

```text
A: NodeA(2)

B: NodeB(2)
```

Therefore:

```text
No intersection.
```

Return:

```js
null;
```

---

## Why Store Node References?

Notice:

```js
map.set(headB, 1);
```

We store:

```text
Node Reference
```

NOT:

```js
map.set(headB.val, 1);
```

because values can repeat.

Only identical node references indicate an actual intersection.

---

## Why This Works

If two linked lists intersect:

```text
They share all nodes after the intersection point.
```

So eventually while traversing List A:

```text
We will reach a node already stored from List B.
```

At that moment:

```js
map.has(headA);
```

becomes:

```js
true;
```

and we return the intersection node.

---

## Dry Run (No Intersection)

### List A

```text
1 -> 2 -> 3
```

### List B

```text
4 -> 5 -> 6
```

---

### Store List B

```text
Map = {4,5,6}
```

---

### Traverse List A

| Node | Exists In Map? |
| ---- | -------------- |
| 1    | ❌             |
| 2    | ❌             |
| 3    | ❌             |

Traversal ends.

Return:

```js
null;
```

---

## Time Complexity

### Store List B

```text
O(m)
```

### Traverse List A

```text
O(n)
```

Total:

```text
O(n + m)
```

---

## Space Complexity

```text
O(m)
```

Map stores all nodes of List B.

---

## Pattern

```text
Hashing / Visited Nodes
```

Commonly used when:

- Detecting intersections
- Detecting duplicates
- Detecting cycles
- Tracking visited nodes

---

## Interview Follow-up

A common follow-up is:

```text
Can you solve this using O(1) space?
```

Answer:

```text
Yes.
```

Using the Two Pointer approach.

That solution gives:

```text
Time  : O(n + m)
Space : O(1)
```

while this Hash Map solution uses:

```text
Time  : O(n + m)
Space : O(m)
```

---

## Revision Notes

- Store all nodes of List B inside a Map.
- Traverse List A.
- If a node already exists in the Map → intersection found.
- Store node references, not values.
- Same value does not mean same node.
- Time: `O(n + m)`
- Space: `O(m)`

### Key Check

```js
if (map.has(headA)) {
  return headA;
}
```

### Core Idea

```text
Store List B Nodes
        ↓
Traverse List A
        ↓
First Matching Node
        ↓
Intersection Found
```
