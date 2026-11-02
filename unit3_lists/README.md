# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?



# Unit 3 Discussion: List Operations

## Overview

This assignment explored insertion, deletion, and searching operations using Python lists. I created a Basketball Roster Manager to demonstrate how players could be added, removed, and searched within a roster.

## Implementation

The program used three functions to manage the basketball roster:

- `insert_at()` inserted a player at a specified index using Python's `insert()` method
- `delete_at()` removed a player using `pop()` after validating the index
- `search_value()` performed a linear search and returned the player's index or `-1` if the player was not found

## Testing

The program was tested using the following operations:

- Inserted players at the beginning, middle, and end of the roster
- Deleted players from the beginning, middle, and end of the roster
- Searched for existing and missing players
- Tested deletion using an invalid index
- Tested deletion from an empty list
- Tested insertion into an empty list

All tests produced the expected results, and the program finished with exit code 0.

## Time and Space Complexity

- **Insertion:** O(n) for insertion at the beginning or middle due to element shifting, and O(1) amortized for insertion at the end
- **Deletion:** O(n) for deletion at the beginning or middle, and O(1) for deletion at the end
- **Searching:** O(n) in the worst case because the program searched through the list sequentially
- **Space Complexity:** O(n) for storing the basketball roster, with O(1) auxiliary space for the search and deletion functions

## Results and Conclusions

The Basketball Roster Manager successfully demonstrated insertion, deletion, and searching operations using Python lists. The program also handled invalid indices and empty lists without crashing.

This assignment helped demonstrate how the position of an element affected the performance of list operations, especially when inserting or deleting items from larger lists.
