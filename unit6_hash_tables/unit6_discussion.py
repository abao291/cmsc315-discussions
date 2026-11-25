"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")

    # Create an empty dictionary to store basketball player statistics
    player_stats = {}

    # Python dictionaries use hashing to store and retrieve key-value pairs
    # Each player ID is a unique key and points scored is its associated value

    # Insert five basketball players and their points scored
    player_stats[101] = 25
    player_stats[102] = 18
    player_stats[103] = 32
    player_stats[104] = 12
    player_stats[105] = 21

    # Display the contents of the dictionary
    print("Basketball player statistics:")
    print(player_stats)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # Retrieve player statistics using their unique player IDs
    # The dictionary uses hashing to locate the associated values
    # without having to search through every entry

    print("Player 101 points:", player_stats[101])
    print("Player 103 points:", player_stats[103])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    # Display the dictionary before updating
    print("Before update:", player_stats)

    # Update the points scored by player 102
    # Assigning a new value to an existing key replaces its previous value
    # without creating a duplicate entry

    player_stats[102] = 24

    # Display the dictionary after updating
    print("After update:", player_stats)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    # Display the dictionary before deletion
    print("Before deletion:", player_stats)

    # Remove player 104 from the dictionary
    # Deleting a key also removes its associated value

    del player_stats[104]

    # Display the dictionary after deletion
    print("After deletion:", player_stats)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Look up a missing player
    # The get() method returns a default value instead of raising a KeyError

    print("\nEdge Case 1: Lookup a missing player")
    print("Player 999:", player_stats.get(999, "Player not found"))

    # Edge Case 2: Safely delete a missing player
    # Check whether the key exists before attempting to delete it

    print("\nEdge Case 2: Delete a missing player")

    if 999 in player_stats:
        del player_stats[999]
        print("Player 999 removed")
    else:
        print("Player 999 does not exist")

    # Edge Case 3: Perform a lookup on an empty dictionary
    # The get() method safely handles lookups when no entries exist

    print("\nEdge Case 3: Lookup in an empty dictionary")

    empty_stats = {}

    print("Empty dictionary:", empty_stats)
    print("Player 101:", empty_stats.get(101, "Player not found"))

    # Display the final dictionary and number of remaining entries
    print("\nFinal player statistics:", player_stats)
    print("Total players:", len(player_stats))



if __name__ == "__main__":
    main()