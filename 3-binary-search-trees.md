# Binary Search Trees

Binary Search Trees (BSTs) can be one of the harder data structures to internalize.
To better understand them, we can look at other similar data structures that use individual
concepts implemented in Binary Search Trees.

## Introduction

### Nodes and Linked Lists

The most fundamental part of a tree is a *node*. Nodes are structures that contain
data as well as point to other nodes. In it's simplest form, one node can point to a
single other node to create a *linked list*.

![diagram showing a linked list](pictures/nodes-linked-list.drawio.svg)

In this diagram, we see a *head* as well as a *tail* node. The head is a node that has nothing
pointing to it and is where the linked list begins. The tail node points to nothing else and is
the end of the linked list.

### Binary Trees

Nodes don't have to just point to one different node like in a linked list. Let's say we give
a node the ability to point to two different nodes:

![diagram showing a binary tree](pictures/binary-tree.drawio.svg)

This difference of being able to traverse in multiple directions is the key difference between
a linked list and a *binary tree*. We see that the tree only has a single *root* node but
has several *leaf* nodes. The reason for this is the parent-child relationship found in trees.
The root node is the *parent* of all nodes in the tree. As we traverse down the tree, we go
through a *child* of that node. When a node has no children, we have hit a leaf node.

### Binary Comparison for Searches

So now that we know how we get a binary tree, where does the whole "search" aspect come from?

Let's say we have a binary tree that has been populated with values. Values lower than the data
in the current node are pushed to the left, and values higher are pushed to the right.
Duplicates, if allowed, can be put in either branch as long as it is consistent.

![diagram showing a BST](pictures/bst-example.drawio.svg)

Let's try adding a value of **15**.

1. 15 is less than 21, so we traverse to the left child.
2. 15 is greater than 11, so we traverse to the right child.
3. We find that no child exists on the right, so we add a new node in place.

![diagram showing traversal of tree and addition of new node](pictures/bst-add-node-example.drawio.svg)

### Tree Balancing

In order to maintain optimal performance, a binary search tree must be *balanced*.
The diagrams in the above section show a balanced tree. But what does an unbalanced tree look like?

![diagram of an unbalanced tree](pictures/unbalanced-bst.drawio.svg)

Look familiar? Worst case scenario will effectively become a linked list, losing all the performance
benefits of a BST.

There a few different ways to balance a tree. If a tree is constantly adding data, an
[AVL Tree](https://en.wikipedia.org/wiki/AVL_tree) or other self-balancing may be an ideal solution:

![AVL Tree GIF](https://upload.wikimedia.org/wikipedia/commons/f/fd/AVL_Tree_Example.gif)

(Image licensed under CC-BY-SA 4.0 from
[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:AVL_Tree_Example.gif))

Another way to balance a tree is to extract all data into a sorted list and choose the middle node
and split the data left and right until all nodes are accounted for. The most effective way to do this
is using [recursion](#a-note-on-recursion).

### A Note on Recursion

Binary Search Trees preform some operations using recursive functions or methods.
This tutorial assumes you know what recursion is and how to use it.
If you need a refresher, check out [here](https://en.wikipedia.org/wiki/Recursion_(computer_science))
or a preferred resource of your choosing.

## Performance

|  Common Operation  |                                        Description                                        | Performance |
|:------------------:|:-----------------------------------------------------------------------------------------:|:-----------:|
| insert(value)      | Insert a value into the BST.                                                              | O(log n)    |
| remove(value)      | Remove a value from the BST.                                                              | O(log n)    |
| contains(value)    | Determine if a value is contained in a node in the BST.                                   | O(log n)    |
| traverse_forward() | Visit all nodes from smallest to largest.                                                 | O(n)        |
| traverse_reverse() | Visit all nodes from largest to smallest.                                                 | O(n)        |
| height(node)       | Get the height of the tree from a specific node.                                          | O(n)        |
| size()             | Return the size of the BST.                                                               | O(1)        |
| empty()            | Returns True if the root node is empty. This can also be done by checking the size for 0. | O(1)        |

## Example - Name Search Tree

All of the demonstrations of BSTs so far have simply shown integers.
However, as long as the data we want to insert into the tree can compared using less than
and greater than operators, we can insert other types of data into the tree.

We can take advantage of the fact that
[Python can compare strings this way](https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types)
to build a BST like so:

```python
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
```

## Try it yourself - BST Containing Hashes

Open the [try it yourself](src/tryit_bst_with_hashes.py) and complete
the challenges noted in the comments. Your output should match the comments
for the Name Search Tree Example.
