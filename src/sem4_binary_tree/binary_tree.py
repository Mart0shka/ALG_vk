class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.balance_factor = None


def get_array_from_tree(root):
    """
    По сути обход в ширину
    """
    current_roots = [root]
    arr = []
    while len(current_roots)>0:
        queue = []

        for current in current_roots:
            arr.append(current.data)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        current_roots = queue

    return arr