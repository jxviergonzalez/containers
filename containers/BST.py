'''
This file implements the Binary Search Tree data structure.
<<<<<<< HEAD
=======
The functions in this file are considerably harder than the
functions in the BinaryTree file.
>>>>>>> heap
'''

from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    '''
    The BST is a superclass of BinaryTree.
<<<<<<< HEAD
=======
    That means that the BST class "inherits" all of the
    methods from BinaryTree,
>>>>>>> heap
    and we don't have to reimplement them.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''
<<<<<<< HEAD
        super().__init__()
        if xs:
            self.insert_list(xs)

    def __iter__(self):
        self.index = 0
        self.list = self.to_list('inorder')
        return self

    def __next__(self):
        if self.index < super().__len__():
            value = self.list[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration()
=======
        self.root = None
        if xs:
            self.insert_list(xs)
>>>>>>> heap

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
<<<<<<< HEAD
=======
        Recall that the __repr__ function should return
        a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command BST([1,2,3])
        it's __repr__ will return "BST([1,2,3])"

        For the BST, type(self).__name__ will be the string "BST",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of BST
        will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
>>>>>>> heap
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def __eq__(self, t2):
        '''
        This method checks to see if the contents of self and t2 are equal.
        The expression `a == b` desugars to `a.__eq__(b)`.

        NOTE:
        We only care about "semantic" equality,
        and not "syntactic" equality.
        That is, we do not care about the tree structure itself,
        and only care about the contents of what the tree contains.

        HINT:
        Convert the contents of both trees into a sorted list,
        then compare those sorted lists for equality.
        '''
        if self is None or t2 is None:
            return False
        list_1 = self.to_list('inorder')
        list_2 = t2.to_list('inorder')
        if list_1 == list_2:
            return True
        else:
            return False

    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
<<<<<<< HEAD
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True
=======
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether
        insert/delete functions
        are actually working.
>>>>>>> heap
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        FIXME:
        The current implementation has a bug:
<<<<<<< HEAD
=======
        it only checks if the children of the current node are
        less than/greater than,
        rather than ensuring that all nodes to the left/right
        are less than/greater than.

        HINT:
        Use the _find_smallest and _find_largest functions to fix the bug.
        You should use the _ prefixed methods because those
        are static methods just like this one.
>>>>>>> heap
        '''
        if node is None:
            return True
        ret = True
        if node.left:
<<<<<<< HEAD
            if node.value >= BST._find_largest(node.left):
=======
            if node.left.value < node.value and \
               node.value > BST._find_largest(node.left):
>>>>>>> heap
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
<<<<<<< HEAD
            if node.value <= BST._find_smallest(node.right):
=======
            if node.right.value > node.value and \
               node.value < BST._find_smallest(node.right):
>>>>>>> heap
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        '''
        Inserts value into the BST.
        FIXME:
        Implement this function.
        HINT:
<<<<<<< HEAD
=======
        Create a staticmethod helper function following the
        pattern of _is_bst_satisfied.
>>>>>>> heap
        '''
        if self.root:
            BST._insert(self.root, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value):
<<<<<<< HEAD
        if value <= node.value:
=======
        if value < node.value:
>>>>>>> heap
            if node.left:
                BST._insert(node.left, value)
            else:
                node.left = Node(value)
        elif value > node.value:
            if node.right:
                BST._insert(node.right, value)
            else:
                node.right = Node(value)

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        FIXME:
        Implement this function.
        HINT:
        Repeatedly call the insert method.
<<<<<<< HEAD
        '''
        for x in xs:
            if self.root:
                BST._insert(self.root, x)
            else:
                self.root = Node(x)
=======
        You cannot get this method to work correctly until
        you have gotten insert to work correctly.
        '''
        for x in xs:
            BST.insert(self, value=x)
>>>>>>> heap

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.
        FIXME:
        Implement this function.
        '''
<<<<<<< HEAD
        if not self.root:
            return None
        else:
            return BST._find(value, self.root)
=======
        if self.root:
            ret = BST._find(value, self.root)
            if ret:
                return ret
            else:
                return False
        else:
            return False
>>>>>>> heap

    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        '''
<<<<<<< HEAD
        if node.value == value:
            return True
        elif value < node.value:
            if node.left:
                return BST._find(value, node.left)
            else:
                return False
        elif value > node.value:
            if node.right:
                return BST._find(value, node.right)
            else:
                return False
=======
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return BST._find(value, node.left)
        else:
            return BST._find(value, node.right)
>>>>>>> heap

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''
        if self.root is None:
            return None
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        '''
<<<<<<< HEAD
=======
        This is a helper function for find_smallest and not
        intended to be called directly by the user.
>>>>>>> heap
        '''
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.
        FIXME:
        Implement this function.
        HINT:
        Follow the pattern of the _find_smallest function.
        '''
        if self.root is None:
<<<<<<< HEAD
            return None
=======
            raise ValueError('Nothing in tree')
>>>>>>> heap
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        '''
<<<<<<< HEAD
        This is a helper function for find_largest and not intended
        to be called directly by the user.
=======
        This is a helper function for find_smallest and not
        intended to be called directly by the user.
>>>>>>> heap
        '''
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        '''
        Removes value from the BST.
        If value is not in the BST, it does nothing.
        FIXME:
        Implement this function.
        HINT:
<<<<<<< HEAD
        HINT:
        Use a recursive helper function.
        '''
        self.root = BST._remove(value, self.root)

    @staticmethod
    def _remove(value, node):
        if node is None:
            return node
        elif value > node.value:
            node.right = BST._remove(value, node.right)
            return node
        elif value < node.value:
            node.left = BST._remove(value, node.left)
            return node
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.value = BST._find_smallest(node.right)
                node.right = BST._remove(node.value, node.right)
=======
        You should have everything else working before you
        implement this function.

        HINT:
        Use a recursive helper function.
        '''
        if self.root is None:
            return
        else:
            self.root = BST._remove(self.root, value)

    @staticmethod
    def _remove(node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = BST._remove(node.left, value)
            return node
        elif value > node.value:
            node.right = BST._remove(node.right, value)
            return node
        if node.value == value:
            if node.left is None and node.right is None:
                node = None
                return node
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            else:
                succparent = node
                succ = node.right
                while succ.left is not None:
                    succparent = succ
                    succ = succ.left
                if succparent != node:
                    succparent.left = succ.right
                else:
                    succparent.right = succ.right
                node.value = succ.value
>>>>>>> heap
                return node

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.
        FIXME:
        Implement this function.
        HINT:
        See the insert_list function.
        '''
        for x in xs:
<<<<<<< HEAD
            self.root = BST._remove(x, self.root)
=======
            BST.remove(self, value=x)

    def __iter__(self):
        if self:
            return self.root.__iter__()
        else:
            my_list = []
            return my_list.__iter__()
>>>>>>> heap
