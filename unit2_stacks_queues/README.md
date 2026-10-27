# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.


# Unit 2: Stacks and Queues

## Project Overview

For this assignment, I implemented stack and queue data structures in Python. I chose a robotics control scenario to demonstrate how these structures could be used to organize robot movement history and process incoming commands.

## Implementation

### Stack - Robot Movement History

I implemented the stack using a Python list. The stack followed the Last-In, First-Out (LIFO) principle, meaning the most recently added item was removed first.

I implemented the following methods:

- `push()` added a movement to the stack.
- `pop()` removed and returned the most recent movement.
- `peek()` returned the most recent movement without removing it.
- `is_empty()` checked whether the stack contained any items.

I demonstrated LIFO behavior by recording four robot movements and retrieving them in reverse order. This simulated how a robotics system could review its movement history.

### Queue - Robot Command Scheduler

I implemented the queue using Python's `collections.deque` library. The queue followed the First-In, First-Out (FIFO) principle, meaning the earliest added item was removed first.

I implemented the following methods:

- `enqueue()` added a command to the queue.
- `dequeue()` removed and returned the earliest command.
- `front()` returned the next command without removing it.
- `is_empty()` checked whether the queue contained any items.

I demonstrated FIFO behavior by adding four robot commands and processing them in the order they were received.

## Testing and Edge Cases

I tested both data structures using multiple values, empty structures, and structures containing only one item.

I verified that:

- Stack movements were retrieved in reverse order.
- Queue commands were processed in their original order.
- Removing or accessing an item from an empty structure returned an informative message instead of crashing.
- Removing the only item from a stack or queue left the structure empty.

The program executed successfully in IntelliJ IDEA and finished with exit code 0.

## Time and Space Complexity

Both structures used O(n) space, where n represented the number of stored movements or commands. As more items were added, the memory required increased proportionally.

The stack's push operation took O(1) amortized time, while pop and peek took O(1) time. The queue's enqueue, dequeue, and front operations also took O(1) time.

## Running the Program

I ran the program using Python 3.13 in IntelliJ IDEA. The program could also be executed from the project directory using:

`python3 unit2_stacks_queues/unit2_discussion.py`

The program printed the robot movement history in LIFO order, the robot commands in FIFO order, and the results of the edge case tests.


## Results and Conclusions

The program successfully demonstrated the differences between stacks and queues using a robotics control scenario.

The stack retrieved robot movements in reverse order, demonstrating Last-In, First-Out (LIFO) behavior. The queue processed robot commands in the order they were added, demonstrating First-In, First-Out (FIFO) behavior.

I also tested several edge cases, including attempting to remove items from empty structures and removing the only item from a stack or queue. All tests produced the expected results, and the program completed successfully without errors.

Overall, this assignment helped demonstrate how stacks and queues could be used for different purposes in a robotics system. The stack was useful for storing movement history, while the queue was useful for organizing and processing commands in a predictable order.

