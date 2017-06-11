class BSTreeNode(object):
    """Binary search tree node (subtree)"""

    def __init__(self, item, key, left=None, right=None):
        """
        Tree node constructor.

        :param item: node's item
        :param key: item's key
        :param left (BSTreeNode): left child (subtree)
        :param right (BSTreeNode): right child (subtree)
        """
        self.item = item
        self.key = key
        self.left = left
        self.right = right

    def insert(self, item, key):
        """
        Assign item to this node if keys are equal.
        Else insert item into the corresponding subtree.
        If there is no corresponding subtree, create it.

        :param item: item to insert
        :param key: item's key
        """
        if key == self.key:
            self.item = item
        else:
            if key < self.key:
                if self.left:
                    self.left.insert(item, key)
                else:
                    self.left = BSTreeNode(item, key)
            else:
                if self.right:
                    self.right.insert(item, key)
                else:
                    self.right = BSTreeNode(item, key)

    def find(self, key):
        """
        Return node's item if keys are equal.
        Else search in the corresponding subtree and return result.
        Else, if there is no subtree, return None.

        :param key: key of the item to find
        :return: item or None
        """
        if self.key == key:
            return self.item
        if self.left:
            if key < self.key:
                return self.left.find(key)
        if self.right:
            if key > self.key:
                return self.right.find(key)
        return None

    def remove(self, key):
        """
        Return modified subtree with item with the key removed.

        :param key: key of the item to remove
        :return: modified subtree or old subtree
        """
        if key == self.key:
            if (self.left is None) and (self.right is None):
                return None
            if (self.left is None) and self.right:
                return self.right
            if (self.right is None) and self.left:
                return self.left
            buf = self
            while buf.left or buf.right:
                if buf.left:
                    buf = buf.left
                elif buf.right:
                    buf = buf.right
            self.item = buf.item
            self.key = buf.key
            buf = None
        else:
            if key < self.key:
                self.left = self.left.remove(key)
            if key > self.key:
                self.right = self.right.remove(key)
        return self

    def size(self):
        """
        Return number of items in the subtree.

        :return: number of items in the subtree
        """
        res = 1
        if self.left:
            res += self.left.size()
        if self.right:
            res += self.right.size()
        return res

    def height(self):
        """
        Return height of the subtree.

        :return: height of the subtree
        """
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max([left_height, right_height])
