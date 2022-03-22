"""Demonstrate the use and balancing of a BST.
"""
class BST:
    """Binary Search Tree Class

    Almost all of the methods as seen in the reading are accessible in this class.
    """

    class Node:
        """The fundamental object that makes up parts of the tree.
        """

        def __init__(self, data):
            self.data = data
            self.less_than = None
            self.greater_than = None

    def __init__(self, allow_dups=False):
        self._size = 0
        self.root = None
        self.allow_dups = allow_dups

    # Make it so the size is correctly tracked!
    def insert(self, value):
        """Insert a value into the BST.

        Args:
            value (any comparable): value to insert to BST
        """
        if self.root is None:
            self.root = BST.Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, data, node):
        if data < node.data:
            # The data belongs on the "less than" side.
            if node.less_than is None:
                # We found an empty spot
                node.less_than = BST.Node(data)
            else:
                # Need to keep looking. Call _insert
                # recursively on the "less than" sub-tree.
                self._insert(data, node.less_than)
        elif data == node.data and not self.allow_dups:
            # Early return prevents incrementing size
            return
        else:
            # The data belongs on the "greater than" side.
            if node.greater_than is None:
                # We found an empty spot
                node.greater_than = BST.Node(data)
            else:
                # Need to keep looking. Call _insert
                # recursively on the "greater than" sub-tree.
                self._insert(data, node.greater_than)
        self._size += 1

    def __contains__(self, value):
        """
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(value, self.root)

    def _contains(self, value, node):
        """
        This functon will search for a node that contains
        'data'.  The current sub-tree being search is
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        if node is None:
            return False
        if node.data == value:
            return True
        if value < node.data:
            return self._contains(value, node.less_than)
        return self._contains(value, node.greater_than)

    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)

    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will
        provide the data in the current node, and finally we will
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.less_than)
            yield node.data
            yield from self._traverse_forward(node.greater_than)

    def traverse_forward(self):
        """Visit all nodes from smallest to largest.

            Returns: nodes (list)
        """
        nodes = []
        for node in self:
            nodes.append(node)
        return nodes

    def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from
        the root of the BST.  This function is called when a the
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """
        yield from self._traverse_reverse(self.root)

    def _traverse_reverse(self, node):
        """
        Does a backwards traversal (reverse in-order traversal) through the
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the right
        side (thus getting the larger numbers first), then we will
        provide the data in the current node, and finally we will
        traverse on the left side (thus getting the smaller numbers last).

        This function is intended to be called the first time by
        the __reversed__ function.
        """
        if node is not None:
            yield from self._traverse_reverse(node.greater_than)
            yield node.data
            yield from self._traverse_reverse(node.less_than)

    def traverse_reverse(self):
        """Visit all nodes from largest to smallest.

            Returns: nodes (list)
        """
        nodes = []
        for node in reversed(self):
            nodes.append(node)
        return nodes

    def _partial_height(self, node):
        """Get the tree height starting from a specific node.
        """
        if self.root is None:
            return 0
        return self._get_height(node)

    def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree
        (represented by 'node') is 1 plus the height of either the
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by
        get_height.
        """
        if node is None:
            return 0
        left_height = self._get_height(node.less_than) + 1
        right_height = self._get_height(node.greater_than) + 1

        if left_height > right_height:
            return left_height
        return right_height

    def height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.

        If the tree is empty, then return 0.  Otherwise, call
        _get_height on the root which will recursively determine the
        height of the tree.
        """
        return self._partial_height(self.root)

    def __len__(self):
        """Allow use on len() on the BST to get the size.
        """
        return self._size

    @property
    def size(self):
        """Return the size of the BST.
        """
        return self._size

    @property
    def empty(self):
        """Returns True if the root node is empty.
        """
        return self.root is None


    # Implement the removal function!
    def remove(self, value):
        """Remove a node from the BST.

        Removal of a node will require cleanup, especially if
        that node has children.
        """
        pass

    # Implement full tree rebalancing!
    def rebalance_tree(self):
        """Rebalance the whole tree.

        This should extract all nodes into a list
        and give the BST a new ideal height.
        """
        pass

    # (Optional) Rebalance starting from a specific node!
    def _rebalance_subtree(self, node):
        pass


def implement_basic_bst_hash_tree():
    """Implement a BST that contains hashes of some objects.
    After creating the tree, rebalance it using the method above.
    Remove one of the hashes in the tree.
    Rebalance again.
    Finally, print out each node.

    Remember that Python has the builtin hash() function.
    """
    pass


# Name Search Tree Example
name_bst = BST()
name_bst.insert('Ronald')
name_bst.insert('Dylan')
name_bst.insert('Ana')
name_bst.insert('Bruh')
name_bst.insert('Victor')
name_bst.insert('Willard')
name_bst.insert('Thomas')

# True
print('Bruh' in name_bst)

# ['Ana', 'Bruh', 'Dylan', 'Ronald', 'Thomas', 'Victor', 'Willard']
print(name_bst.traverse_forward())

name_bst.remove('Bruh')

# ['Ana', 'Dylan', 'Ronald', 'Thomas', 'Victor', 'Willard']
print(name_bst.traverse_forward())

# 3
print(name_bst.height())

# 6
print(name_bst.size)

name_bst.insert('Zester')
name_bst.insert('Zilliam')

# 5
print(name_bst.height())

# ['Ana', 'Dylan', 'Ronald', 'Thomas', 'Victor', 'Willard', 'Zester', 'Zilliam']
print(name_bst.traverse_forward())

name_bst.rebalance_tree()

# 4
print(name_bst.height())


# Run challenge code
implement_basic_bst_hash_tree()