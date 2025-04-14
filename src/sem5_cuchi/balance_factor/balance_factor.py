def calculate_heights_and_balances(node):
    if node is None:
        return 0

    left_height = calculate_heights_and_balances(node.left)
    right_height = calculate_heights_and_balances(node.right)

    node.balance_factor = left_height - right_height

    return 1 + max(left_height, right_height)