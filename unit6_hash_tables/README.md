# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## Implementation Summary

### Design Approach

For this assignment, I created a basketball player statistics lookup system using a Python dictionary. Each player's unique ID served as the key, while the number of points scored served as the associated value. This scenario demonstrated how hash tables could be used to efficiently manage and retrieve player statistics.

### Hash Table Operations

- **Insertion:** I created an empty dictionary and populated it with five basketball players and their corresponding points scored.
- **Lookup:** I retrieved the points scored by players 101 and 103 using their unique player IDs.
- **Update:** I updated player 102's points from 18 to 24 without creating a duplicate entry.
- **Deletion:** I removed player 104 and its associated value from the dictionary.

### Edge Cases

I implemented and tested three edge cases to improve the reliability of the program:

- I used the `get()` method to retrieve a missing player without raising a `KeyError`.
- I checked whether a player ID existed before attempting to delete it.
- I performed a lookup on an empty dictionary and returned an appropriate message when the player was not found.

### Hash Table Performance and Collisions

I used Python's built-in dictionary, which handled hashing and collision resolution internally. A collision could occur when different keys mapped to the same initial storage location. Frequent collisions could increase the number of operations required to locate a value and reduce lookup efficiency.

Dictionary insertion, lookup, update, and deletion operations generally had an average time complexity of O(1). Compared to linear search, which had a time complexity of O(n), dictionaries provided a more efficient approach to retrieving player statistics as the number of records increased.

### Testing Results

I successfully executed the program and verified that all insertion, lookup, update, and deletion operations produced the expected results. All three edge cases were handled without errors. The final dictionary contained four players, and the program completed with exit code 0.