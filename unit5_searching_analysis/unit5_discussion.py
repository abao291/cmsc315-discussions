"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""
import time

def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Check each player ID from the beginning of the list
    for index in range(len(lst)):

        # Return the index when the target player ID is found
        if lst[index] == target:
            return index

    # Return -1 if the player ID does not exist
    # Linear search is O(n) because it may check every element
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Set the starting and ending boundaries
    left = 0
    right = len(lst) - 1

    # Continue searching while the range is valid
    while left <= right:

        # Find the middle index of the current search range
        mid = (left + right) // 2

        # Return the index if the player ID is found
        if lst[mid] == target:
            return mid

        # Search the right half if the target is larger
        elif lst[mid] < target:
            left = mid + 1

        # Search the left half if the target is smaller
        else:
            right = mid - 1

    # Return -1 if the player ID was not found
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")
    print("Basketball Player ID Search System")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset
    # 2. Test both linear search and binary search
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results

    print("\n=== SMALL DATASET TEST ===")

    # Create a sorted list of basketball player IDs
    player_ids = [20, 30, 40, 50, 60, 70, 80]

    print("Player IDs:", player_ids)

    # Search for an existing player ID
    target = 60

    print("\nSearching for player ID:", target)
    print("Linear Search:", linear_search(player_ids, target))
    print("Binary Search:", binary_search(player_ids, target))

    # Both algorithms return index 4 because player ID 60 exists

    # Search for a player ID that does not exist
    target = 90

    print("\nSearching for player ID:", target)
    print("Linear Search:", linear_search(player_ids, target))
    print("Binary Search:", binary_search(player_ids, target))

    # Both algorithms return -1 because player ID 90 is not found

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset
    # 2. Test both search algorithms
    # 3. Compare the results
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger

    print("\n=== LARGE DATASET TEST ===")

    # Simulate a large basketball player database
    large_player_ids = list(range(1, 1000001))

    # Search for the last player ID to demonstrate worst-case linear search
    target = 1000000

    print("Total Player IDs:", len(large_player_ids))
    print("Searching for player ID:", target)

    # Measure linear search execution time
    start = time.perf_counter()
    linear_result = linear_search(large_player_ids, target)
    linear_time = time.perf_counter() - start

    # Measure binary search execution time
    start = time.perf_counter()
    binary_result = binary_search(large_player_ids, target)
    binary_time = time.perf_counter() - start

    print("\nLinear Search Result:", linear_result)
    print("Linear Search Time:", f"{linear_time:.8f}", "seconds")

    print("\nBinary Search Result:", binary_result)
    print("Binary Search Time:", f"{binary_time:.8f}", "seconds")

    # Linear search checks each ID until it reaches the last element
    # Binary search repeatedly eliminates half of the remaining IDs
    # Binary search is generally faster for large sorted datasets

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    # Both algorithms return -1 because there are no IDs to search
    empty_list = []

    print("\nEmpty List:")
    print("Linear Search:", linear_search(empty_list, 50))
    print("Binary Search:", binary_search(empty_list, 50))

    # Edge Case 2: Single-element list
    # Both algorithms return index 0 when the target matches
    single_player = [50]

    print("\nSingle-Element List:")
    print("Linear Search:", linear_search(single_player, 50))
    print("Binary Search:", binary_search(single_player, 50))

    # Edge Case 3: First element
    # Both algorithms return index 0 for player ID 20
    print("\nFirst Player ID:")
    print("Linear Search:", linear_search(player_ids, 20))
    print("Binary Search:", binary_search(player_ids, 20))

    # Edge Case 4: Last element
    # Both algorithms return index 6 for player ID 80
    print("\nLast Player ID:")
    print("Linear Search:", linear_search(player_ids, 80))
    print("Binary Search:", binary_search(player_ids, 80))


if __name__ == "__main__":
    main()
