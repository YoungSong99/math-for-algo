"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

height = 3 / 2

       1
      / \
     2   3  
     / \
    4   5
    /
   6

Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

1. understand the problm
height of left node + height of right node = diameter

2. question
       1
      / 
     2   
     / 
    4   
    /
   6
- when there is only root or there is no root: output 0

3. Implementation:

"""
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = None
        self.right = None

def getDiameter(node):
    #return the height from root.left and root.right
    def getHeight(node):
        #basecase
        if not node:
            return 0
        return max(getHeight(node.left), getHeight(node.right)) + 1

    # add height of left node and right node to find diameter
    return getHeight(node.left) + getHeight(node.right)

"""

       1
      / \
     2   3  
     / \
    4   5
    /
   6

"""



