
"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Adds new values to the top so the last value added is removed first
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Checks if the stack is empty to prevent an error when removing a value
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Returns the most recently added value without removing it
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        # Returns True when the stack contains no values
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Adds new values to the back so the first value added is removed first
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Checks if the queue is empty to prevent an error when removing a value
        if self.is_empty():
            return "Queue is empty"
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Returns the oldest value in the queue without removing it
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        # Returns True when the queue contains no values
        return len(self.items) == 0



def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO: ROBOT MOVEMENT HISTORY ===")

    movements = Stack()

    # Record four robot movements in the order they occurred
    for movement in [
        "Rotate base left",
        "Raise robotic arm",
        "Extend arm forward",
        "Close gripper"
    ]:
        movements.push(movement)
        print("Recorded movement:", movement)

    # Preview the most recently recorded movement
    print("\nMost recent movement:", movements.peek())
    print("\nReviewing movements in reverse order (LIFO):")

    # Remove movements starting with the most recent
    while not movements.is_empty():
        print("Last recorded movement:", movements.pop())

    # Test empty stack operations
    print("Pop from empty stack:", movements.pop())
    print("Peek at empty stack:", movements.peek())

    # Test a stack containing only one movement
    single_stack = Stack()
    single_stack.push("Open gripper")
    print("\nSingle movement removed:", single_stack.pop())
    print("Is single-item stack now empty?", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: ROBOT COMMAND SCHEDULER ===")

    commands = Queue()

    # Add commands in the order they should be executed
    for command in [
        "Initialize robot",
        "Move to starting position",
        "Pick up object",
        "Return to home position"
    ]:
        commands.enqueue(command)
        print("Queued command:", command)

    # Preview the next command without removing it
    print("\nNext command:", commands.front())
    print("\nExecuting commands in FIFO order:")

    # Execute commands in the order they were added
    while not commands.is_empty():
        print("Executing:", commands.dequeue())

    # Test empty queue operations
    print("Dequeue from empty queue:", commands.dequeue())
    print("Front of empty queue:", commands.front())

    # Test a queue containing only one command
    single_queue = Queue()
    single_queue.enqueue("Stop robot")
    print("\nSingle command removed:", single_queue.dequeue())
    print("Is single-item queue now empty?", single_queue.is_empty())


if __name__ == "__main__":
    main()
