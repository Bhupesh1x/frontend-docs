## Design Linked List

```js
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
```

**code**

```js
/**
 * Create a node constructor function which takes val and next
 * This can be use to create new node objects
 */
var ListNode = function (val, next) {
  this.val = val;
  this.next = next;
};

/**
 * Create a MyLinkedList constructor function
 * This can be use to create new LinkedList
 * It initialize the head initially to null and size to 0
 */
var MyLinkedList = function () {
  this.head = null;
  this.size = 0;
};

/**
 * Function to get the value at the given index
 * Return -1 if index is invalid
 * Start from head and move index times
 * curr will reach the required node
 * Return the value of that node
 */
MyLinkedList.prototype.get = function (index) {
  if (index < 0 || index >= this.size) return -1;

  let curr = this.head;

  for (let i = 0; i < index; i++) {
    curr = curr.next;
  }

  return curr.val;
};

/**
 * Function to add a node at the beginning of the linked list
 * Create a new node
 * Point the new node next to current head
 * Update head to the new node
 * Increase the size
 */
MyLinkedList.prototype.addAtHead = function (val) {
  let node = new ListNode(val);

  node.next = this.head;
  this.head = node;

  this.size++;
};

/**
 * Function to add a node at the end of the linked list
 * If list is empty, make the new node the head
 * Otherwise traverse till the last node
 * Connect the last node to the new node
 * Increase the size
 */
MyLinkedList.prototype.addAtTail = function (val) {
  let node = new ListNode(val);

  if (this.head === null) {
    this.head = node;
    this.size++;
    return;
  }

  let curr = this.head;

  while (curr.next) {
    curr = curr.next;
  }

  curr.next = node;
  this.size++;
};

/**
 * Function to insert a node at a given index
 * Return if index is invalid
 * If index is 0, insert at head
 * If index equals size, insert at tail
 * Otherwise go to index - 1 position
 * Insert the node by updating pointers
 * Increase the size
 */
MyLinkedList.prototype.addAtIndex = function (index, val) {
  let node = new ListNode(val);

  if (index < 0 || index > this.size) return;

  if (index === 0) {
    this.addAtHead(val);
    return;
  }

  if (index === this.size) {
    this.addAtTail(val);
    return;
  }

  let curr = this.head;

  for (let i = 0; i < index - 1; i++) {
    curr = curr.next;
  }

  node.next = curr.next;
  curr.next = node;

  this.size++;
};

/**
 * Function to delete a node at a given index
 * Return if index is invalid
 * If deleting the head, move head to next node
 * Otherwise go to index - 1 position
 * Skip the target node by updating pointers
 * Decrease the size
 */
MyLinkedList.prototype.deleteAtIndex = function (index) {
  if (index < 0 || index >= this.size) return;

  if (index == 0) {
    this.head = this.head.next;
    this.size--;
    return;
  }

  let curr = this.head;

  for (let i = 0; i < index - 1; i++) {
    curr = curr.next;
  }

  curr.next = curr.next.next;
  this.size--;
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */
```
