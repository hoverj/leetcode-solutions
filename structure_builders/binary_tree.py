from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -------------------------
# LeetCode List -> Tree
# -------------------------
def list_to_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# -------------------------
# Tree -> LeetCode List
# -------------------------
def tree_to_list(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    # Remove unnecessary trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


# -------------------------
# Level Printer
# -------------------------
def print_levels(root):
    if root is None:
        print("<empty>")
        return

    queue = deque([root])
    level = 0

    while queue:
        if all(node is None for node in queue):
            break

        values = []
        size = len(queue)

        for _ in range(size):
            node = queue.popleft()

            if node is None:
                values.append("·")
                queue.append(None)
                queue.append(None)
            else:
                values.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        print(f"Level {level}: {'  '.join(values)}")
        level += 1
