"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys

sys.path.append('../stack')
sys.path.append('../queue')

from stack import Stack
from queues import Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        else:
            if value <= self.value:
                if self.left is not None:
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return self.value

        elif target >= self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        max = self
        while max.right is not None:
            max = max.right
        return max.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    def delete(self, value):
        if self.value == value:
                self.value = self.right
                self.right = self.right.right

        elif target >= self.value:
            if self.right is not None:
                return self.right.delete(target)
            else:
                return "Value not in the BST"
        else:
            if self.left is not None:
                return self.left.delete(target)
            else:
                return "Value not in the BST"

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self:
            if self.left:
                self.left.in_order_print()
            print(self.value)
            if self.right:
                self.right.in_order_print()





    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        if self:
            queue = Queue()
            current_node = self
            
            queue.enqueue(current_node)

        # while the queue isn't empty
        # take out the first on the list and make it the current node then print it
        # If the current node has a left and a right, add it to the

            while len(queue) != 0:
                current_node = queue.dequeue()
                print(current_node.value)
            
                if current_node.left:
                    queue.enqueue(current_node.left)
                if current_node.right:
                    queue.enqueue(current_node.right)
                    

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = Stack()
        current_node = self

        stack.push(current_node)

        while len(stack) != 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)  
                
                      
    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass


