class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def in_order_traversal(self)-> list:
            if self is None:
                return []
            else:
                return (BinaryTree.in_order_traversal(self.left) + [self.key] + BinaryTree.in_order_traversal(self.right))
    def pre_order_traversal(self)-> list:
        if self is None:
            return []
        else:
            return ([self.key] + BinaryTree.pre_order_traversal(self.left)+ BinaryTree.pre_order_traversal(self.right))
    def post_order_traversal(self)-> list:
        if self is None:
            return []
        else:
            return (BinaryTree.post_order_traversal(self.left)+ BinaryTree.post_order_traversal(self.right)+[self.key])
    def tuple_from_tree(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        else:
            return BinaryTree.tuple_from_tree(self.left),self.key, BinaryTree.tuple_from_tree(self.right)
    def height_of_tree(self):
        if self is None:
            return 0
        else:
            return 1 + max(BinaryTree.height_of_tree(self.left), BinaryTree.height_of_tree(self.right))
    def size_of_tree(self):
        if self is None:
            return 0
        else:
            return 1 + BinaryTree.size_of_tree(self.left) + BinaryTree.size_of_tree(self.right)
    @staticmethod
    def binary_tree_from_tuple(tree_tuple):
                if isinstance(tree_tuple, tuple) and len(tree_tuple) == 3:
                    node =BinaryTree(tree_tuple[1])
                    node.right = BinaryTree.binary_tree_from_tuple(tree_tuple[2])
                    node.left = BinaryTree.binary_tree_from_tuple(tree_tuple[0])
                elif tree_tuple is None:
                    node = None
                else:
                    node = BinaryTree(tree_tuple)
                return node
    def __str__(self):
        return "<{}>".format(self.tuple_from_tree())


def main()->None:
    tree_tuple: tuple = ((1,2,None), 5,(7,8,9))
    tree: BinaryTree = BinaryTree.binary_tree_from_tuple(tree_tuple)
    print(f"In-order traversal 'Left->Root->Right': {tree.in_order_traversal()}")
    print(f"Post-order traversal 'Left->Right->Root': {tree.post_order_traversal()}")
    print(f"Pre-order traversal 'Root->Right->Left': {tree.pre_order_traversal()}")
    print(f"Height of tree: {tree.height_of_tree()}")
    print(f"Size of tree: {tree.size_of_tree()}")
    print(tree)


if __name__ =="__main__":
    main()
