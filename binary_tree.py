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
    def __repr__(self):
        return "{}".format(self.tuple_from_tree())
    def is_not_none(self, node):
        return [key for key in node if key is not None]

    def is_bst(self, min_val = float('-inf'), max_val= float('inf') ):
        if self is None:
            return True
        if min_val > self.key or self.key > max_val:
            return False
        else:
            left = BinaryTree.is_bst(self.left, min_val, self.key)
            right =BinaryTree.is_bst(self.right, self.key, max_val)
            return left and right
    def find_max_and_min(self, min_val =float('inf'), max_val = float('-inf'))-> tuple:
        if self is None:
            return min_val, max_val
        max_val = max(self.key, max_val)
        min_val = min(self.key, min_val)
        min_val, max_val =BinaryTree.find_max_and_min(self.left, min_val, max_val)
        min_val , max_val =BinaryTree.find_max_and_min(self.right, min_val, max_val)
        return min_val, max_val
    def breadth_first_traversal(self, breadth_first = []):
        if self is None:
            return []
        else:
            if self.key not in breadth_first:
                breadth_first.append(self.key)
            if self.left:
                breadth_first.append(self.left.key)
            if self.right:
                breadth_first.append(self.right.key)
            BinaryTree.breadth_first_traversal(self.left, breadth_first)
            BinaryTree.breadth_first_traversal(self.right, breadth_first)
        return breadth_first

def main()->None:
    tree_tuple: tuple = ((2,3,4), 5,(7,8,9))
    tree: BinaryTree = BinaryTree.binary_tree_from_tuple(tree_tuple)
    print(f"In-order traversal 'Left->Root->Right': {tree.in_order_traversal()}")
    print(f"Post-order traversal 'Left->Right->Root': {tree.post_order_traversal()}")
    print(f"Pre-order traversal 'Root->Left->Right': {tree.pre_order_traversal()}")
    print(f"Height of tree: {tree.height_of_tree()}")
    print(f"Size of tree: {tree.size_of_tree()}")
    print(tree)
    print(f"Tree is BST ? {tree.is_bst()}")
    print(f"Breadth First traversal: {tree.breadth_first_traversal()}")
    print(f"Minimum value  is {tree.find_max_and_min()[0]} and maximum value is: {tree.find_max_and_min()[1]}")


if __name__ =="__main__":
    main()
