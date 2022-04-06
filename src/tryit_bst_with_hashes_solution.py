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
            self._size += 1
            self.root = BST.Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, data, node):
        if data < node.data:
            # The data belongs on the "less than" side.
            if node.less_than is None:
                # We found an empty spot
                node.less_than = BST.Node(data)
                self._size += 1
            else:
                # Need to keep looking. Call _insert
                # recursively on the "less than" sub-tree.
                self._insert(data, node.less_than)
        elif data == node.data and not self.allow_dups:
            # Early return prevents incrementing size
            return
        else:
            # The data belongs on the "greater than" side.
            # If duplicates are allowed, they will be put on this side.
            if node.greater_than is None:
                # We found an empty spot
                node.greater_than = BST.Node(data)
                self._size += 1
            else:
                # Need to keep looking. Call _insert
                # recursively on the "greater than" sub-tree.
                self._insert(data, node.greater_than)

    def remove(self, value):
        """Remove a node from the BST.

        Removal of a node will require cleanup, especially if
        that node has children.
        """
        if self.root is None:
            return
        if self._size == 1:
            self.root = None
            self._size = 0
            return
        self._remove(value, self.root, None)
        self._size -= 1


    def _remove(self, data, node, parent):
        # Data not in tree
        if node is None:
            return
        if data < node.data:
            self._remove(data, node.less_than, node)
        elif data > node.data:
            self._remove(data, node.greater_than, node)
        # Node is our target for removal
        else:
            # Removal of leaf nodes
            if node.less_than is None and node.greater_than is None:
                self._disown_child(node, parent)
            # Remove root node
            elif node == self.root:
                new_root, new_root_parent = self._get_new_root(node.less_than, parent)
                self._disown_child(new_root, new_root_parent)
                new_root.less_than = self.root.less_than
                new_root.greater_than = self.root.greater_than
                self.root = new_root
            # Remove node with only one child
            elif node.less_than is None:
                self._disown_child(node, parent, node.greater_than)
            elif node.greater_than is None:
                self._disown_child(node, parent, node.less_than)
            # Removal of nodes with two children
            else:
                replacement_node, replacement_parent_node = self._get_new_root(node.less_than, node)
                self._disown_child(replacement_node, replacement_parent_node)
                self._disown_child(node, parent, replacement_node)
                replacement_node.less_than = node.less_than
                replacement_node.greater_than = node.greater_than

    @staticmethod
    def _disown_child(node, parent, replacement=None):
        if parent.less_than == node:
            parent.less_than = replacement
        elif parent.greater_than == node:
            parent.greater_than = replacement

    def _get_new_root(self, node, parent):
        if node.greater_than is None:
            return (node, parent)
        return self._get_new_root(node.greater_than, node)

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

    # Implement full tree rebalancing! (Optional)
    def rebalance_tree(self):
        """Rebalance the whole tree.

        This should extract all nodes into a list
        and give the BST a new ideal height.
        """
        pass

    # Rebalance starting from a specific node! (Optional)
    # Make sure to call this method on node insertion or removal.
    def _rebalance_subtree(self, node):
        pass


def implement_basic_bst_hash_tree():
    """Implement a BST that contains hashes of some objects of your choice.
    Add several hashes to the tree.
    Print the tree height.
    Remove at least one of the hashes in the tree.
    List the number of items in the tree.
    Print the tree height.
    Print out each node in reverse order.
    Finally, print out each node in order.

    Remember that Python has the builtin hash() function.
    """
    pass


# All tests are below this point

# Name Search Tree Example
name_bst = BST()
name_bst.insert('Ronald')
name_bst.insert('Bruh')
name_bst.insert('Dylan')
name_bst.insert('Ana')
name_bst.insert('Victor')
name_bst.insert('Willard')
name_bst.insert('Thomas')

# True
print('Bruh' in name_bst)
assert 'Bruh' in name_bst

# ['Ana', 'Bruh', 'Dylan', 'Ronald', 'Thomas', 'Victor', 'Willard']
print(name_bst.traverse_forward())
assert name_bst.traverse_forward() == \
    ['Ana', 'Bruh', 'Dylan', 'Ronald', 'Thomas', 'Victor', 'Willard']

name_bst.remove('Bruh')

# ['Ana', 'Dylan', 'Ronald', 'Thomas', 'Victor', 'Willard']
print(name_bst.traverse_forward())
assert name_bst.traverse_forward() == ['Ana', 'Dylan', 'Ronald', 'Thomas', 'Victor', 'Willard']

# 3
print(name_bst.height())
assert name_bst.height() == 3

# 6
print(name_bst.size)
assert name_bst.size == 6

name_bst.insert('Zester')
name_bst.insert('Zilliam')

# 5 or 4 if AVL balancing is implemented, 7 if not (Optional)
name_bst.rebalance_tree()
print(name_bst.height())
assert name_bst.height() > 4 and name_bst.height() < 7

name_bst.remove('Zester')

# ['Ana', 'Dylan', 'Ronald', 'Thomas', 'Victor', 'Willard', 'Zilliam']
print(name_bst.traverse_forward())
assert name_bst.traverse_forward() ==  \
    ['Ana', 'Dylan', 'Ronald', 'Thomas', 'Victor', 'Willard', 'Zilliam']

name_bst.remove('Ronald')

# ['Ana', 'Dylan', 'Thomas', 'Victor', 'Willard', 'Zilliam']
print(name_bst.traverse_forward())
assert name_bst.traverse_forward() == ['Ana', 'Dylan', 'Thomas', 'Victor', 'Willard', 'Zilliam']

name_bst.rebalance_tree()

# 4
print(name_bst.height())
assert name_bst.height() == 4


# Run challenge code
implement_basic_bst_hash_tree()
