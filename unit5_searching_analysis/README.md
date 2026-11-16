# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.


## Implementation

For this assignment, I created a basketball player ID search system to demonstrate the differences between linear search and binary search. I used the same basketball-related theme from my previous assignments to show how different searching algorithms could be applied to player records.

I implemented linear search by checking each player ID sequentially until the target was found or the end of the list was reached. I implemented binary search by repeatedly checking the middle element of a sorted list and reducing the remaining search range by half.

## Testing and Results

I tested both algorithms using a small dataset containing seven basketball player IDs. Both algorithms successfully located an existing ID and returned -1 when searching for an ID that was not present.

I also created a larger dataset containing 1,000,000 sorted player IDs to compare execution times.

| Algorithm | Execution Time |
|---|---|
| Linear Search | 0.06193871 seconds |
| Binary Search | 0.00001190 seconds |

Both algorithms returned the correct index of 999999. However, binary search completed the search significantly faster.

I also tested several edge cases, including an empty list, a single-element list, and values at the first and last positions. Both algorithms returned the expected results for each test.

## Performance Analysis

I observed that linear search had a time complexity of O(n), since it potentially needed to examine every element in the dataset. Binary search had a time complexity of O(log n), since it eliminated approximately half of the remaining elements during each iteration.

Binary search performed better when searching the large sorted dataset. However, linear search remained useful for smaller or unsorted datasets because it did not require the data to be organized beforehand.

I concluded that choosing the appropriate searching algorithm depended on the dataset size, whether the data was sorted, and how frequently searches needed to be performed.
