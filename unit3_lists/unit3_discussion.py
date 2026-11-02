
"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert the player at the requested position
    # Existing elements at or after the index shift one position right
    # Inserting at the beginning or middle takes O(n) time due to shifting
    # Inserting at the end is typically O(1) amortized
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Reject invalid indices to prevent unexpected removals or errors
    if index < 0 or index >= len(lst):
        return None

    # Remove the player and shift later elements one position left
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Check players sequentially because the roster is not sorted
    # Linear search takes O(n) time in the worst case
    for index, player in enumerate(lst):
        if player == value:
            return index

    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    roster = ["Michael Jordan", "LeBron James"]
    print("Original roster:", roster)

    # Add a player at the beginning of the lineup
    insert_at(roster, 0, "Steph Curry")
    print("After inserting Steph Curry at the beginning:", roster)

    # Add a player in the middle of the lineup
    insert_at(roster, len(roster) // 2, "Klay Thompson")
    print("After inserting Klay Thompson in the middle:", roster)

    # Add a player at the end of the lineup
    insert_at(roster, len(roster), "Kobe Bryant")
    print("After inserting Kobe Bryant at the end:", roster)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Remove the first player from the lineup
    removed = delete_at(roster, 0)
    print("Removed from beginning:", removed)
    print("Updated roster:", roster)

    # Remove a player from the middle
    removed = delete_at(roster, len(roster) // 2)
    print("Removed from middle:", removed)
    print("Updated roster:", roster)

    # Remove the last player
    removed = delete_at(roster, len(roster) - 1)
    print("Removed from end:", removed)
    print("Updated roster:", roster)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for an existing player
    player = "Michael Jordan"
    index = search_value(roster, player)
    print(f"Searching for {player}: Found at index {index}")

    # Search for a player not currently on the roster
    player = "Kobe Bryant"
    index = search_value(roster, player)
    print(f"Searching for {player}: Index {index} (not found)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Attempt to delete using an invalid index
    print("Delete at invalid index 100:", delete_at(roster, 100))

    # Attempt to delete from an empty roster
    empty_roster = []
    print("Delete from empty roster:", delete_at(empty_roster, 0))

    # Insert into an empty roster
    insert_at(empty_roster, 0, "Steph Curry")
    print("Insert Steph Curry into empty roster:", empty_roster)

    # Search for a player not present in the roster
    print("Search for missing player:", search_value(roster, "Kobe Bryant"))


if __name__ == "__main__":
    main()
