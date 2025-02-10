class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def in_order_traversal(tree: BinaryTree)-> list:
        if tree is None:
            return []
        else:
            return (in_order_traversal(tree.left) + [tree.key] + in_order_traversal(tree.right))
def pre_order_traversal(tree: BinaryTree)-> list:
    if tree is None:
        return []
    else:
        return ([tree.key] +pre_order_traversal(tree.left)+ pre_order_traversal(tree.right))
def post_order_traversal(tree: BinaryTree)-> list:
    if tree is None:
        return []
    else:
        return (post_order_traversal(tree.left)+ post_order_traversal(tree.right)+[tree.key])

def binary_tree_from_tuple(tree_tuple):
            if isinstance(tree_tuple, tuple) and len(tree_tuple) == 3:
                node =BinaryTree(tree_tuple[1])
                node.right = binary_tree_from_tuple(tree_tuple[2])
                node.left = binary_tree_from_tuple(tree_tuple[0])
            elif tree_tuple is None:
                node = None
            else:
                node = BinaryTree(tree_tuple)
            return node


def main()->None:
    tree_tuple: tuple = ((1,2,None), 5,(7,8,9))
    tree: BinaryTree = binary_tree_from_tuple(tree_tuple)
    print(f"In-order traversal 'Left->Root->Right': {in_order_traversal(tree=tree)}")
    print(f"Post-order traversal 'Left->Right->Root': {post_order_traversal(tree)}")
    print(f"Pre-order traversal 'Root->Right->Left': {pre_order_traversal(tree)}")


if __name__ =="__main__":
    main()
