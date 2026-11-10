"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        # Store the value associated with this node
        self.value = value

        # Initialize both child references to None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        # The root is None until the first value is inserted
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Begin insertion at the root of the tree
        # Smaller values belong on the left and larger values on the right
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: create a new node when an empty position is found
        if node is None:
            return Node(value)

        # Insert smaller values into the left subtree
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Insert larger values into the right subtree
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Begin searching at the root of the tree
        # A BST can skip entire subtrees based on value comparisons
        # Searching a balanced BST takes O(log n) time
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base case: an empty subtree means the value was not found
        if node is None:
            return False

        # Base case: return True when the value matches the current node
        if value == node.value:
            return True

        # Search the left subtree for smaller values
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Search the right subtree for larger values
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Create an empty list to store the traversal results
        values = []

        # Begin the recursive traversal at the root
        self._inorder_recursive(self.root, values)

        # Return the values in sorted order
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # Stop recursion when an empty child is reached
        if node is None:
            return

        # Visit smaller values first so the results are sorted
        self._inorder_recursive(node.left, values)

        # Add the current node's value to the results
        values.append(node.value)

        # Visit larger values in the right subtree
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    # Create a new binary search tree
    tree = BST()

    # Insert seven basketball player IDs into the tree
    player_ids = [50, 30, 70, 20, 40, 60, 80]

    # BST insertion compares values to determine the correct subtree
    # Smaller values go left and larger values go right
    # This reduces the search space at each step in a balanced tree
    for player_id in player_ids:
        tree.insert(player_id)
        print("Inserted player ID:", player_id)

    # Display the root and its immediate children
    print("Root:", tree.root.value)
    print("Left child:", tree.root.left.value)
    print("Right child:", tree.root.right.value)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # In-order traversal visits left, root, then right
    # Smaller values are visited before larger values
    print("Sorted player IDs:", tree.inorder())

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Search for two player IDs that exist in the tree
    # Both searches should return True
    print("Searching for player ID 30:", tree.search(30))
    print("Searching for player ID 60:", tree.search(60))

    # Search for two player IDs that do not exist
    # Both searches should return False
    print("Searching for player ID 25:", tree.search(25))
    print("Searching for player ID 90:", tree.search(90))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Traverse an empty BST
    # An empty tree has no nodes, so traversal returns an empty list
    empty_tree = BST()
    print("In-order traversal of empty tree:", empty_tree.inorder())

    # Edge case 2: Search an empty BST
    # Searching an empty tree returns False
    print("Searching for 50 in empty tree:", empty_tree.search(50))

    # Edge case 3: Insert a duplicate value
    # Duplicate values are ignored by our insertion function
    tree.insert(30)
    print("After inserting duplicate ID 30:", tree.inorder())

    # Edge case 4: Create a BST with only one node
    # A single-node tree has a root but no children
    single_tree = BST()
    single_tree.insert(100)
    print("Single-node tree traversal:", single_tree.inorder())
    print("Searching for 100 in single-node tree:", single_tree.search(100))



if __name__ == "__main__":
    main()