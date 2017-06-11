from bstree import BSTree
from generate import read_file, write_file
from util import shuffled_ints, random_ints, powers_of
import random, math

outputdebug = False

def debug(msg):
    if outputdebug:
        print (msg)

class Node():
    def __init__(self, key):
        self.key = key[1]
        self.people=' '.join(key)
        self.left = None
        self.right = None


class AVLTree():
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return (self.height == 0)

    def insert(self, key):
        tree = self.node
        newnode = Node(key)

        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")

        elif key[1] < tree.key:
            self.node.left.insert(key)

        elif key[1] > tree.key:
            self.node.right.insert(key)

        else:
            self.node.people=self.node.people+' '+' '.join(key)

        self.rebalance()

    def rebalance(self):
        '''
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()



    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' right')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T


    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T


    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def search(self, key):
        if self.node != None:
            if self.node.key == key:
                return self.node.people
            elif key < self.node.key:
                return self.node.left.search(key)
            elif key > self.node.key:
                return self.node.right.search(key)
        else:
            return 'There is no such person'

    def TreeSearch(self, keys):
        for key in keys:
            self.search(key)



    def check_balanced(self):
        if self == None or self.node == None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())


    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''
        self.update_heights()  # Must update heights before balances
        self.update_balances()
        if(self.node != None):
            print( '-' * level * 2, pref, self.node.people, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')


def CreateTree(inlist):
    a=AVLTree()
    for i in inlist:
        i = i.split(' ')
        a.insert(i)
    return a


# Usage example
if __name__ == "__main__":
    a = AVLTree()
    print ("----- Inserting -------")
    inlist = read_file("records_1e1.txt")
    for i in inlist:
        i=i.split(' ')
        a.insert(i)
    a.display()
    print(a.search('Aarons'))

