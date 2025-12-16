# Queue Implementation in Python

This repository demonstrates two basic ways to implement a **Queue** data structure in Python:

1. **Using Arrays (Lists)**
2. **Using a Class-based Approach**

Both implementations showcase common queue operations such as **enqueue**, **dequeue**, **peek**, **isEmpty**, and **size**.

---

## Files in This Project

### 1. `QueueImplementationUsingArrays.py`

This file implements a queue using Python’s built-in list.

#### Operations Demonstrated:

* **Enqueue** – Add elements to the queue
* **Dequeue** – Remove the front element
* **Peek** – View the front element
* **IsEmpty** – Check if the queue is empty
* **Size** – Get the number of elements in the queue

#### Example Output:

```
queue:  ['a', 'b', 'c']
dequeue a
peak b
isEmpty False
size 2
```

#### Notes:

* Uses `append()` to add elements.
* Uses `pop(0)` to remove the front element.
* Simple and easy to understand, but not optimal for large queues due to shifting elements.

---

### 2. `QueueImplementationUsingClass.py`

This file implements a queue using an object-oriented approach with a `Queue` class.

#### Features:

* Encapsulates queue logic inside a class
* Provides reusable methods for queue operations
* Handles empty queue cases gracefully

#### Methods:

* `enqueue(element)` – Adds an element to the queue
* `dequeue()` – Removes and returns the front element
* `peek()` – Returns the front element without removing it
* `isEmpty()` – Checks if the queue is empty
* `size()` – Returns the size of the queue

#### Example Output:

```
queue: ['a', 'b', 'c']
dequeue a
peek b
IsEmpty False
Size 2
```

---

## How to Run

Make sure you have Python installed, then run either file:

```bash
python QueueImplementationUsingArrays.py
```

or

```bash
python QueueImplementationUsingClass.py
```

---

## Conclusion

* The **array-based implementation** is best for learning and small use cases.
* The **class-based implementation** is more structured and reusable.
* Both examples help understand how queues work internally in Python.