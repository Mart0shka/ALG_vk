from src.sem4_binary_tree.is_same_tree.is_same_tree import is_same_tree
def is_subtree(a,b):
    if b is None:
        return True

    if a is None:
        return False

    if is_same_tree(a,b):
        return True

    return is_subtree(a.left, b) or is_subtree(a.right, b)
