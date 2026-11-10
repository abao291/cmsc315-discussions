# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.


# Unit 4 Discussion: Binary Search Trees

## Overview

For this assignment, I created a Binary Search Tree (BST) application in Python that organized basketball player IDs. The program demonstrated recursive insertion, searching, and in-order traversal. I also tested several edge cases to verify that the BST handled different situations correctly.

## Implementation

I implemented two classes, `Node` and `BST`. The `Node` class stored a value and references to its left and right children. The `BST` class contained methods for inserting values, searching for values, and performing an in-order traversal.

I inserted seven player IDs into the tree: `[50, 30, 70, 20, 40, 60, 80]`. Smaller values were placed in the left subtree, while larger values were placed in the right subtree. This insertion order created a balanced BST.

The program used recursion to insert and search for values. During insertion, each value was compared with the current node to determine which subtree to follow. Searching worked similarly, allowing the program to skip subtrees that could not contain the requested value.

## Testing

I tested the following operations:

- Inserted seven player IDs into the BST
- Performed an in-order traversal to display the IDs in sorted order
- Searched for two existing IDs, `30` and `60`, which returned `True`
- Searched for two missing IDs, `25` and `90`, which returned `False`
- Traversed an empty BST, which returned an empty list
- Searched an empty BST, which returned `False`
- Inserted a duplicate ID, which was ignored
- Created and searched a single-node BST

All tests produced the expected results, and the program completed without errors.

## Time and Space Complexity

I learned that BST performance depended on the shape of the tree. In a balanced BST, insertion and searching generally took O(log n) time because each comparison reduced the remaining search space.

However, inserting values in sorted order could create a skewed BST, causing insertion and searching to take O(n) time in the worst case.

In-order traversal took O(n) time because every node had to be visited. The traversal also required O(n) space to store the returned values.

## Results and Conclusions

The in-order traversal returned the player IDs in ascending order:

`[20, 30, 40, 50, 60, 70, 80]`

Completing this assignment helped me understand how BSTs organized data and how recursion was used to navigate through a tree. I also learned that insertion order could affect tree structure and search efficiency. While balanced BSTs offered efficient searching, an unbalanced tree could perform similarly to a linked list.
